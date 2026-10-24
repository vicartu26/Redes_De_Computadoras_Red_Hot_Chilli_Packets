UNIVERSIDAD NACIONAL DE CÓRDOBA

FACULTAD DE CIENCIAS EXACTAS, FÍSICAS, Y NATURALES

CÁTEDRA DE COMPUTACIÓN

![Escudo UNC](C:/Users/Genar/Desktop/Redes_De_Computadoras_Red_Hot_Chilli_Packets/TP5/images/image1.png)

**“Trabajo Práctico N°6: Capa Física y de Red”**

Alumnos:  

Eliezer Flores (45172399)

Genaro Agustín Mateos Ferrero (19103190)    
Victor José Arturo Castro (46522607)  
Tiziano Quevedo (44972730)  
Gonzalo del Cotillo (43216694)  
Mariano Stroppa (46309318)

Angélica Moisés (46765089)

Comisión: ICOMP24-3 

## Parte 1: Taller de armado y verificación de cables Cat5/Cat5e

### 1.1 Pasos para crimpar un cable bajo la norma T568A/B

*Detallar aquí el procedimiento paso a paso que se investigó para realizar el crimpado del cable de red de forma directa (no cruzado).*

### 1.2 Inspección visual y constructiva

* **Aspectos positivos:** [Mencionar qué quedó bien armado, ej: recubrimiento dentro del conector, cables llegando al fondo, etc.]
* **Aspectos negativos/A mejorar:** [Mencionar detalles constructivos, si los hubiera]
* **Justificación fotográfica:** [Insertar aquí las fotos tomadas al conector/cable para respaldar el análisis]

### 1.3 Verificación eléctrica

*Documentar aquí el resultado de la prueba realizada con el tester para cables ethernet.*

* **Evidencia fotográfica:** [Insertar foto del tester indicando continuidad correcta de los pines]

---

## Parte 2: Equipamiento físico y generación de tráfico

### 2.1 Levantar y testear una LAN

#### Justificación de Direccionamiento IP (Punto 1.d)

* **IPv4 configurada:** 192.168.1.10 y 192.168.1.11

Se optó las direcciones IP correspondientes al espacio de direccionamiento privado establecido por el estándar RFC 1918. Estas direcciones pertenecen a un bloque comúnmente utilizado para redes de área local (LAN) por lo que garantiza que no existan conflictos con direcciones IP públicas.

* **Máscara de subred:** 255.255.255.0

La configuración de esta máscara indica que los primeros tres octetos corresponden a la porción de red y el último octeto a la porción de host. Al aplicar esta misma máscara en ambas computadoras, las dos direcciones IP quedan lógicamente ubicadas dentro de la misma subred. Esto es fundamental porque le indica a la pila TCP/IP de cada computadora que el equipo de destino se encuentra en el mismo segmento de red local. Como resultado, las computadoras pueden comunicarse directamente en la capa de enlace de datos (Capa 2) resolviendo sus direcciones MAC mediante el protocolo ARP a través del switch, sin requerir un enrutador el cual no se disponía en el laboratorio.

* **Default Gateway:** Ninguna

Se decidió no configurar ninguna puerta de enlace predeterminada ya que solo se utiliza cuando un host necesita enviar paquetes a una dirección IP que se encuentra fuera de su propia subred. Dado que el alcance de esta actividad consistía en comunicar únicamente a dos equipos conectados físicamente al mismo switch en una LAN aislada, todo el tráfico generado tenía un destino estrictamente local. En pocas palabras, configurar un gateway hubiera sido redundante e innecesario para los fines de este laboratorio.



#### Captura de Tráfico UDP (Punto 4)

* **Captura en Wireshark:** [Insertar captura de pantalla de los paquetes recibidos con Ncat]
* **Análisis de la captura:** *Documentar los detalles observados (direcciones IP de origen y destino, puertos utilizados, longitud, etc.).*

#### Cuestionario sobre UDP (Punto 5)

* **a) ¿Se observa algún procedimiento de establecimiento de conexión antes de enviar los datos?**

* **b) ¿Existe algún mecanismo de confirmación de recepción equivalente a los ACK de TCP?**

* **c) ¿Qué ocurre si se envían mensajes mientras el receptor UDP no está ejecutándose?**

* **d) ¿UDP garantiza que los mensajes lleguen en el mismo orden en que fueron enviados?**

* **e) ¿Qué aplicaciones reales utilizan UDP y por qué?**

---

## Parte 3: Desarrollar un pequeño servidor

### 3.1 Análisis de tráfico web (Punto 4)

* **Captura en Wireshark (Descarga HTTP/curl):** [Insertar imagen de la captura del tráfico generado al bajar el archivo del servidor Python]
* **Tipo de tráfico observado:** *[Explicar qué protocolo de la capa de transporte (TCP) se está utilizando para esta transmisión, identificando el Three-Way Handshake, ACKs, etc., y comparándolo con el comportamiento visto anteriormente en UDP].*
