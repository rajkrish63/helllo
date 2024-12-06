import socket

# Function to handle the server
def start_server(host, port):
    # Create the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the specified host and port
    server_socket.bind((host, port))
    server_socket.listen(1)  # The server can handle 1 incoming connection at a time
    print("Server started. Waiting for connections on {}:{}...".format(host, port))  # Replaced f-string with .format()

    # Accept client connection
    client_socket, client_address = server_socket.accept()
    print("Connection established with {}".format(client_address))  # Replaced f-string with .format()

    while True:
        # Receive message from the client
        message = client_socket.recv(1024).decode()
        if message.lower() == 'exit':
            print("Connection closed by client.")
            break
        
        print("Client: {}".format(message))  # Replaced f-string with .format()
        response = input("Server: ")  # Server sends message to client
        client_socket.send(response.encode())  # Send the server's response to the client

    # Close the connection
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    host = '0.0.0.0'  # Accepts connections on all network interfaces (use a specific IP for remote connections)
    port = 12345  # Port to bind to
    start_server(host, port)
