
import socket

# 1. Create TCP Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect to Server
client.connect(("127.0.0.1", 5000))

# 3. Send message
message = "Facebook"
client.sendall(message.encode())

# 4. Receive response
response = client.recv(1024).decode()

print(f"Server says: {response}")

client.close()
