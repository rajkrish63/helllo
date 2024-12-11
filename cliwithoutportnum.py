import socket

def start_client(server_host, server_port=40205, client_name="Client"):  # Default port set to 40205
    """Connect to the server and handle communication."""
    try:
        # Create a client socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Connecting to server at {server_host}:{server_port}...")
        client_socket.connect((server_host, server_port))
        print(f"Connected to server at {server_host}:{server_port}.")
        
        # Receive the server's name
        server_name = client_socket.recv(1024).decode()
        print(f"thier name: {server_name}")  # Print the server's name
        
        # Send the client's name to the server
        client_socket.send(client_name.encode())
        
        while True:
            try:
                # Input message from the user
                message = input(f"{client_name}: ")
                client_socket.send(message.encode())  # Send the message to the server
                
                if message.lower() == 'exit':
                    print("Connection closed.")
                    break
                
                # Receive response from the server
                response = client_socket.recv(1024).decode()
                print(f"{server_name}: {response}")  # Now displaying server's name properly
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

def get_server_ip():
    """Get the server IP from the user input."""
    try:
        # Request server IP address only (no port input required)
        server_host = input("Enter the server IP address: ").strip()
        return server_host
    except ValueError:
        print("Invalid input. Please enter the correct server IP address.")
        exit(1)

if __name__ == "__main__":
    # Get the server IP address from the user (no port input)
    server_host = get_server_ip()

    # Get the client's name
    client_name = input("Enter your name  :) ")

    # Start the client with the obtained details and default port 40205
    start_client(server_host, client_name=client_name)
