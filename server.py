
import socket

# 1. Create TCP Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Choose IP and Port
server.bind(("127.0.0.1", 5000))

# 3. Start listening
server.listen()

print("Server is waiting for connections...")

while True:
    conn, address = server.accept()

    print(f"Connected with: {address}")

    request = conn.recv(4096).decode()
    print(request)

    html = "<h1>Hello from my HTTP Serverr!</h1>"

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(html.encode())}\r\n"
        "Connection: close\r\n"
        "\r\n"
        + html
    )

    conn.sendall(response.encode())
    conn.close()