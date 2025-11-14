import socket

#create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

try:
    while True:
        #client theke server a msg pathano
        msg = input("Enter message to server: ")
        if msg.lower() == "exit":
            break
        client_socket.send(msg.encode())

        # server theke reply neya
        reply = client_socket.recv(1024).decode()
        print("Server replied:", reply)

except Exception as e:
    print("Error:", e)

finally:
    client_socket.close()
    print("Client closed.")