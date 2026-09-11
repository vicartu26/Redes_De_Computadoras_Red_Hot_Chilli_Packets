UNIVERSIDAD NACIONAL DE CÓRDOBA

FACULTAD DE CIENCIAS EXACTAS, FÍSICAS, Y NATURALES

CÁTEDRA DE COMPUTACIÓN 

![Escudo UNC](images/image1.png)

**“**Trabajo Práctico N°2: Conceptos fundamentales de capa física y capa de enlace de datos”

Alumnos:  
Genaro Agustín Mateos Ferrero (19103190)  
Angélica Moisés (46765089)  
Victor José Arturo Castro (46522607)  
Eliezer Flores (45172399)  
Tiziano Quevedo (44972730)  
Gonzalo del Cotillo (43216694)  
Mariano Stroppa (46309318)

Comisión: ICOMP24-3 

## Punto 1:

Vamos a empezar observando cómo se organiza la información dentro de una red local:

a) ¿Qué función cumple la capa de enlace dentro del modelo OSI? ¿Qué tipo de comunicación resuelve?

_Pendiente de completar._

b) ¿Qué es una dirección MAC? ¿En qué se diferencia de una dirección IP?

_Pendiente de completar._

c) ¿Qué es una trama Ethernet? Identificar sus principales campos y explicar brevemente para qué sirve cada uno.

_Pendiente de completar._

d) ¿Qué información permite determinar qué protocolo de capa superior está transportando una trama Ethernet?

_Pendiente de completar._

## Punto 2:

Usando Wireshark, capturar tráfico generado por su propia computadora mientras acceden a una página web o ejecutan alguna aplicación que utilice la red (en general no hace falta hacer nada realmente, el tráfico normal de la computadora ya genera UNA BOCHA de paquetes a internet).

a) Seleccionar una trama Ethernet e identificar las direcciones MAC de origen y destino. ¿A qué dispositivos creen que corresponden?   
![Trama Ethernet - MAC origen y destino](images/2-a.png)

* MAC origen: `70:4d:7b:8b:06:71` → ASUSTek Computer (la laptop desde la que se capturó el tráfico).   
* MAC destino: `08:f6:06:95:a5:94` → ZTE Corporation (el router de la red local), este es el salto desde donde salimos para internet. 

b) Dentro de la misma trama, identificar el paquete IP. ¿Cuáles son las direcciones IP de origen y destino? (no importa si son versión 4 o versión 6\)   
![Paquete IP dentro de la trama](images/2-b.png)  
Dentro de esta trama podemos observar que el paquete es IPv4 (Type: 0x0800 en la capa Ethernet, y se confirma en la cabecera IP con "Versión: 4") 

* IP origen: `192.168.1.102` (dirección privada, la PC local).   
* IP destino: `104.29.142.146` (dirección pública, servidor en Internet). 

c) Comparar las direcciones MAC y las direcciones IP encontradas. ¿Representan lo mismo?

No representan lo mismo, la dirección IP representa ubicaciones de red, mientras que MAC  lo hace respecto a la dirección física del hardware. Dicho de otro modo, la dirección IP identifica la conexión del dispositivo en la red, y la MAC el dispositivo en sí. Además se puede observar que los primeros 6 dígitos de ésta última representan al fabricante del dispositivo (OUI, Organizational Unique Identifier), por esto vemos ASUSTekCOMPU en source y zte_95 en destination.


d) Observar el campo EtherType. ¿Qué protocolo está encapsulado dentro de la trama analizada?
![Protocolo dentro de la trama](images/2-d.png) 
Observamos que el protocolo encapsulado en la trama analizada es el llamado “protocolo de datagrama de usuario” (User Datagram Protocol), que pertenece dentro de la familia TCP/IP y, en este caso, utiliza Internet Protocol versión 4.

## Punto 3:

Vamos ahora a subir una capa y observar el transporte de información mediante TCP.

a) ¿Qué problema(s) resuelve TCP que no resuelve directamente Ethernet ni IP?

_Pendiente de completar._

b) Investigar los campos más importantes de la metadata en un frame TCP. ¿Para qué sirve cada uno?

_Pendiente de completar._

c) Explicar el Three y Four way handshake en TCP.

El Three way handshake o diálogo en tres pasos, como su nombre indica, consiste básicamente de tres partes. En la primera el emisor o cliente inicia el proceso de comunicación enviando un segmento TCP con la flag de SYN activada y un número de secuencia inicial  i. Luego el receptor o servidor confirma el número de secuencia recibido enviando un AN=i+1 y envía su propio número de secuencia inicial j.(SYN + ACK). Finalmente, el cliente confirma el número de secuencia del servidor enviando AN=j+1 y se establece la conexión.
El Four way handshake funciona de forma similar:
Paso 1: el usuario emite una orden de cierre (Close) y se envía  un segmento con el bit de FIN activado (FIN i).
Paso 2: el receptor recibe el FIN y devuelve una confirmación ACK con AN= i+1.
Paso 3: cuando el receptor termina de enviar todos sus datos pendientes y su usuario ejecuta la orden de cierre, envía su propio segmento FIN  j.
Paso 4: el emisor inicial confirma el FIN enviando un ACK AN = j+1 , luego debe esperar un intervalo de tiempo igual a dos veces el máximo tiempo de vida esperado un segmento antes de cerrar definitivamente la conexión.


d) Iniciar la conexión enviando un paquete, capturar el handshake y el paquete de datos. Analizar el paquete de datos, sus distintas partes y encontrar la carga útil del paquete usando WireShark.

_Pendiente de completar._

e) Finalizar la conexión y capturar el Four-way handshake.

_Pendiente de completar._

f) ¿Qué conclusión podemos sacar de que sea tan fácil ver un paquete que viaja a través de la red?

_Pendiente de completar._

## Punto 4:
Siguiendo los pasos para iniciar la conexión pudimos verificar las respuestas del servidor con los comandos correspondientes.
![Interacción con el servidor - Packet Sender](images/PacketSender.png)
![Interacción con el servidor - Wireshark](images/Wireshark.png)
Después de conseguir el paquete específico para nuestro grupo, pudimos completar el siguiente link utilizando los comandos de los demás grupos: https://www.youtube.com/watch?v=dQw4w9WgXcQ
