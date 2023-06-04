import socket


def check_internet_connection():
    servers = [
        ("www.google.com", 80),
        ("www.bing.com/", 80),
    ]  # List of servers to attempt connection

    for server in servers:
        try:
            # Set a timeout of 300 ms
            socket.setdefaulttimeout(0.3)

            # Try connecting to the server
            sock = socket.create_connection(server)
            sock.close()  # Close the connection
            return True
        except OSError as e:
            print(f"Error connecting to {server}: {str(e)}")

    return False


# Example usage
if __name__ == "__main__":
    if check_internet_connection():
        print("Internet connection is available.")
    else:
        print("No internet connection.")
