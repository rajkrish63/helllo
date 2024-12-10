import socket

def get_server_ip():
    """Get the server's local IP address."""
    try:
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.8.8", 80))  # External address to determine local IP
        local_ip = temp_socket.getsockname()[0]
        temp_socket.close()
        return local_ip
    except Exception as e:
        return "Could not determine IP address. Error: {}".format(e)

def start_server(host):
    """Start the server and handle client connections."""
    try:
        # Create and bind the server socket to any available port (port 0)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, 0))  # Using 0 to let the OS pick an available port
        server_port = server_socket.getsockname()[1]  # Get the assigned port
        server_socket.listen(5)  # Allow up to 5 simultaneous connections
        print("Server started on {}:{}.".format(host, server_port))
        print("Waiting for client connection...")

        while True:
            try:
                # Accept new client connections
                client_socket, client_address = server_socket.accept()
                print("Connection established with {}".format(client_address))
                
                # Communicate with the client
                while True:
                    try:
                        message = client_socket.recv(1024).decode()
                        if not message or message.lower() == 'exit':
                            print("Connection closed by client.")
                            break
                        
                        print("Client: {}".format(message))
                        response = input("Server: ")
                        client_socket.send(response.encode())
                    except Exception as e:
                        print("Error during communication: ", e)
                        break
                
                client_socket.close()
                print("Client disconnected.")
            except KeyboardInterrupt:
                print("\nServer interrupted. Shutting down.")
                break
            except Exception as e:
                print("Error accepting connection: ", e)
    
    except Exception as e:
        print("Server error: ", e)
    finally:
        server_socket.close()
        print("Server shut down.")

if __name__ == "__main__":
    host = get_server_ip()  # Automatically gets the server's local IP
    start_server(host)
