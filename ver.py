import socket

# create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12345))  # port fixed
server.listen(1)
print("Server is listening on port 12345...")

# ⿢ client connection
conn, addr = server.accept()
print("Connected with", addr)

try:
    while True:
        # message from client
        msg = conn.recv(1024).decode()
        if not msg:  # jodi client dissconnect kore
            print("Client disconnected.")
            break
        print("Client says:", msg)

        # reply from server
        reply = input("Enter reply to client: ")
        conn.send(reply.encode())

except Exception as e:
    print("Error:", e)

finally:
    conn.close()
    server.close()
    print("Server closed.")