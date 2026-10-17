
import socket

HOST = "127.0.0.1"
PORT = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to the server!")
print("Type 'exit' to disconnect.")

try:
    while True:
        message = input("You: ")

        if message.lower() == "exit":
            break

        client.sendall(message.encode())

        reply = client.recv(1024).decode()
        print(reply)

finally:
    client.close()
    print("Disconnected from server.")
