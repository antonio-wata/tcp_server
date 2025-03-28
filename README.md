![Python 3](https://img.shields.io/badge/python-3-blue.svg)

## RUN SERVER
Primero iniciar el servidor, desde terminal colocarse en la carpeta tcp_service y en terminal ejecutar el comando:
`python3 tcp_server.py`

Una vez terminadas las pruebas si desde el servidor ejecuta el comando ctrl+c
hará que el programa termine y muestre el mensaje por parte del servidor:
> Server shutting down gracefully...

Esto también cerra el servicio del cliente.

## RUN CLIENT
Después de iniciar el servidor, para iniciar el cliente, desde terminal colocarse en la carpeta tcp_service y en una segunda terminal ejecutar el comando:
`python3 tcp_client.py`

para terminar la conexión debe pasar la palabra desconexion
En caso de no iniciar primero el servidor, el cliente no podrá ejecutarse mostrando error.

## Pruebas:
Cliente: prueba 1
Server: PRUEBA 1

Cliente: 56789olk,m./
Server: 56789OLK,M./

Cliente: desconexion
Server: Connection closed by client.