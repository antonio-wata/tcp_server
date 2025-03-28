import socket

HOST = "localhost"
PORT = 5000

# Create a socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((HOST, PORT))
socket_server.listen(1)

print(f"Server listening on {HOST}:{PORT}")

running = True
try:
  while running:
    print("Waiting for a new connection...")
    socket_client, client_address = socket_server.accept()
    print(f"Connection accepted from {client_address}")

    try:
      while True:
        data_message = socket_client.recv(1024).decode().strip()
        if not data_message:
          break  
        
        print(f"Message received: {data_message}")

        if data_message.upper() == "DESCONEXION":
          print("Connection closed by client.")
          running = False
          break  
        else:
          response = data_message.upper().encode()
          socket_client.send(response)
    except Exception as e:
      print(f"Error: {e}")
    finally:
      # Close connection
      socket_client.close()

# Close server
except KeyboardInterrupt:
  print("\nServer shutting down gracefully...")

finally:
  socket_server.close()