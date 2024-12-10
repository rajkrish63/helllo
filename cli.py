import socket

def start_client(server_host, server_port):
    """Connect to the server and handle communication."""
    try:
        # Create a client socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Connecting to server at {}:{}...".format(server_host, server_port))
        client_socket.connect((server_host, server_port))
        print("Connected to server at {}:{}.".format(server_host, server_port))
        
        while True:
            try:
                # Input message from the user
                message = input("Client: ")
                client_socket.send(message.encode())  # Send the message to the server
                
                if message.lower() == 'exit':
                    print("Connection closed.")
                    break
                
                # Receive response from the server
                response = client_socket.recv(1024).decode()
                print("Server: {}".format(response))
            except Exception as e:
                print("Error during communication: ", e)
                break
        
    except ConnectionRefusedError:
        print("Could not connect to the server. Please check the server address and port.")
    except Exception as e:
        print("An error occurred: ", e)
    finally:
        client_socket.close()
        print("Client socket closed.")

def get_server_details():
    """Get the server IP and port from the user input in a single line."""
    try:
        # Request server details in the form of 'IP:PORT'
        server_input = input("Enter the server IP address and port (e.g., 192.168.1.100:12345): ").strip()
        
        # Split the input into IP and port
        server_host, server_port = server_input.split(':')
        
        # Validate port and convert to integer
        server_port = int(server_port)
        
        return server_host, server_port
    except ValueError:
        print("Invalid input. Please enter the server IP and port in the correct format (e.g., 192.168.1.100:12345).")
        exit(1)

if __name__ == "__main__":
    # Get the server IP and port from the user in one input
    server_host, server_port = get_server_details()

    # Start the client with the obtained details
    start_client(server_host, server_port)
