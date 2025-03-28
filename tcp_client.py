import socket

HOST = "localhost"
PORT = 5000

# Create a socket
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((HOST, PORT))

try:
  while True:
    message = input("Write a message: ").strip()
    if not message:
      continue

    socket_client.send(message.encode("utf-8"))

    if message.upper() == "DESCONEXION":
      print("Disconnecting from the server...")
      break  

    response = socket_client.recv(1024).decode().strip()
    print(f"Server response: {response}")

except Exception as e:
  print(f"Error: {e}")

finally:
  print("Closing connection...")
  socket_client.close()