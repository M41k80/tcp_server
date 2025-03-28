#Ejercicio Técnico: Cliente y Servidor TCP en Python


##Detalles del Ejercicio
###1. Servidor TCP:
 ##El servidor debe iniciar en localhost y escuchar conexiones en el puerto 5000.
 ###Una vez que el cliente se conecte, el servidor debe esperar a recibir un mensaje del cliente.
###Si el servidor recibe el mensaje "DESCONEXION", debe:
■ Cerrar la conexión con ese cliente.
■ Mantenerse disponible para recibir conexiones de nuevos clientes.
○ Para cualquier otro mensaje recibido, el servidor debe responder al cliente
devolviendo el mensaje en mayúsculas.
2. Cliente TCP:
○ El cliente debe conectarse al servidor en localhost y puerto 5000.
○ El cliente debe solicitar al usuario que ingrese un mensaje y luego enviarlo al
servidor.
○ Tras enviar el mensaje, el cliente debe recibir y mostrar la respuesta del
servidor en consola.
○ Si el usuario ingresa "DESCONEXION", el cliente debe:
■ Enviar este mensaje al servidor.
■ Cerrar la conexión y finalizar su ejecución.
3. Requisitos de Pruebas:
○ Incluye dos pruebas manuales:
■ Enviar un mensaje de texto normal y verificar que el servidor
responda con el mensaje en mayúsculas.
■ Enviar el mensaje "DESCONEXION" y verificar que la conexión se
cierre correctamente en ambos lados.
4. Documentación:
○ Incluye un archivo README.md con instrucciones claras para:
■ Ejecutar el servidor y el cliente.
■ Realizar las pruebas manuales.
Ejemplo de Interacción:
Conexión establecida:
Cliente envía: hola servidor
Servidor responde: HOLA CLIENTE
Desconexión:
Cliente envía: DESCONEXION
Servidor cierra la conexión con el cliente.




# Servidor y Cliente TCP - Documentacion

Este proyecto implementa un servidor y cliente TCP  que se comunican a través del puerto 5000 en localhost.

## Requisitos

- Python 3.6 o superior

## Instrucciones de Ejecución

### Para el servidor:

1. Abra una terminal
2. Navegue al directorio del proyecto
3. Ejecute:
    
    ```bash
    python server.py o
    python3 server.py
    ```
    

### Para el cliente:

1. Abra otra terminal
2. Navegue al directorio del proyecto
3. Ejecute:
    
     ```bash
    python client.py o
    python3 client.py
    ```
