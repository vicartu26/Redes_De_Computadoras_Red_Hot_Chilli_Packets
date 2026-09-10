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

_Pendiente de completar._

d) Observar el campo EtherType. ¿Qué protocolo está encapsulado dentro de la trama analizada?

_Pendiente de completar._

## Punto 3:

Vamos ahora a subir una capa y observar el transporte de información mediante TCP.

a) ¿Qué problema(s) resuelve TCP que no resuelve directamente Ethernet ni IP?

_Pendiente de completar._

b) Investigar los campos más importantes de la metadata en un frame TCP. ¿Para qué sirve cada uno?

_Pendiente de completar._

c) Explicar el Three y Four way handshake en TCP.

_Pendiente de completar._

d) Iniciar la conexión enviando un paquete, capturar el handshake y el paquete de datos. Analizar el paquete de datos, sus distintas partes y encontrar la carga útil del paquete usando WireShark.

_Pendiente de completar._

e) Finalizar la conexión y capturar el Four-way handshake.

_Pendiente de completar._

f) ¿Qué conclusión podemos sacar de que sea tan fácil ver un paquete que viaja a través de la red?

_Pendiente de completar._

## Punto 4:

_Pendiente de completar._
