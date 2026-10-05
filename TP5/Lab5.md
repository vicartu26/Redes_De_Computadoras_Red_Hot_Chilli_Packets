UNIVERSIDAD NACIONAL DE CÓRDOBA

FACULTAD DE CIENCIAS EXACTAS, FÍSICAS, Y NATURALES

CÁTEDRA DE COMPUTACIÓN 

![Escudo UNC](images/image1.png)

**“Trabajo Práctico N°5: Transmisión de Datos”**

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
Investigar brevemente y documentar:

a) Pendiente de completar

b) Pendiente de completar

c) Pendiente de completar

d) Pendiente de completar

![Tabla punto 1](images/tabla1.png)

a) Pendiente de completar

b) Pendiente de completar

c) El payload del ping queda dentro de la parte ICMP (Internet Control Message Protocol) en la sección de "Data". 

![Payload ping request](images/payloadRequest.png)

Tiene 32 bytes que contienen el mensaje que se quería transmitir, en este caso es el abecedario llegando hasta la letra "w" y volviendo a comenzar para llegar hasta la letra "i". Al compararlos, vemos que este contenido es igual en el mensaje de reply. 

![Payload ping reply](images/payloadReply.png)

No contamos con ninguna computadora que tenga Linux, pero al investigar aprendimos que el payload podría tener datos distintos ya que es el sistema operativo quien decide qué datos van en el mensaje de ping.

d) Pendiente de completar

e) En whireshark pudimos ver el tamaño de cada encabezado:

![Frame Bytes](images/FrameBytes.png)

![Ethernet Bytes](images/EthernetBytes.png)

![IP Bytes](images/IPBytes.png)

![ICMP Bytes](images/ICMPBytes.png)

![Data Bytes](images/DataBytes.png)

Entonces el dibujo como "cajas dentro de cajas" queda:

![Cajas en cajas](images/1e.jpeg)

## Punto 2:
Investigar brevemente:

a) Pendiente de completar

b) Pendiente de completar

c) Pendiente de completar

d) En la repetición aparecieron ARP en whireshark, sin embargo vemos que no son de nuestra PC hacia el gateway, sino que el router envió su propio request hacia la computadora ("Who has 192.168.1.102? Tell 192.168.1.1"). 

![Repeticion ping](images/arpNuevas.png)

La falta del request de nuestra computadora al gateway se debe a que quedó guardado en la caché ARP por el ping anterior:

![Caché de ARP](images/arpCache.png)

Entonces la ventaja del caché es que evita enviar un broadcast para comunicarnos con un destino ya conocido. Es bajo la misma lógica que surge el problema: al quedar una entrada vieja, incluso si hay cambios, no se va a hacer un broadcast sino que será utiizada la misma entrada. Los paquetes se enviarán a una dirección incorrecta hasta que la entrada vieja sea actualizada. 

e) Pendiente de completar

f) Pendiente de completar

![Tabla punto 2](images/tabla2.png)

a) Pendiente de completar

b) Pendiente de completar

c) Pendiente de completar

d) Pendiente de completar

## Punto 3:
Investigar brevemente:

a) Pendiente de completar

b) Pendiente de completar

c) Pendiente de completar



a) Pendiente de completar

b) Pendiente de completar

c) Pendiente de completar

d) Pendiente de completar

e) Pendiente de completar

f) Pendiente de completar

## Punto 4:

a) -

b) -

c) Pendiente de completar

d) Pendiente de completar