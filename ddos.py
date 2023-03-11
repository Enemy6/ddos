import socket
import time

# Define the host and port of the website you want to request
HOST = 'guyanapoliceforce.gy'
PORT = 80

# Define the HTTP request to be sent to the website
request = f"GET / HTTP/1.1\r\nHost: {HOST}\r\n\r\n"
# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the website
client_socket.connect((HOST, PORT))

# Loop through the requests
while True:
    # Send the request to the website
    client_socket.send(request.encode())

    # Receive the response from the website
    response = b""
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response += data

    # Print the response
    print(response.decode())
    print("\n")

    # Wait for 0.01 seconds before sending the next request
    time.sleep(0.01)

# Close the socket
client_socket.close()
