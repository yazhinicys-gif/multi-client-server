
import socket
import threading

HOST = "127.0.0.1"
PORT = 9999

def handle_client(client_socket, client_address):
    print(f"[CONNECTED] {client_address}")

    try:
        while True:
            message = client_socket.recv(1024)

            if not message:
                break

            text = message.decode()
            print(f"Client {client_address}: {text}")

            reply = f"Server received: {text}"
            client_socket.sendall(reply.encode())

    except ConnectionError:
        print(f"[ERROR] Connection lost: {client_address}")

    finally:
        client_socket.close()
        print(f"[DISCONNECTED] {client_address}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

print(f"Server listening on {HOST}:{PORT}")

try:
    while True:
        client_socket, client_address = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_address)
        )
        thread.start()

except KeyboardInterrupt:
    print("\nServer shutting down.")

finally:
    server.close()
