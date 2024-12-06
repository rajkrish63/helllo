import socket

# Function to handle the client
def start_client(server_host, server_port):
    # Create the client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((server_host, server_port))
    print("Connected to server at {}:{}".format(server_host, server_port))  # Replaced f-string with .format()

    while True:
        message = input("Client: ")  # Client sends message to server
        client_socket.send(message.encode())  # Send message to the server
        
        if message.lower() == 'exit':
            print("Connection closed.")
            break
        
        # Receive server's response
        response = client_socket.recv(1024).decode()
        print("Server: {}".format(response))  # Replaced f-string with .format()

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    server_host = '10.3.9.30'  # Replace with the server's IP address (e.g., 192.168.x.x)
    server_port = 12345  # The same port number used in the server
    start_client(server_host, server_port)
