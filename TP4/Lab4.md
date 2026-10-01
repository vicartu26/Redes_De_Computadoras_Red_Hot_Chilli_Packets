UNIVERSIDAD NACIONAL DE CÓRDOBA

FACULTAD DE CIENCIAS EXACTAS, FÍSICAS, Y NATURALES

CÁTEDRA DE COMPUTACIÓN 

![Escudo UNC](images/image1.png)

**“Trabajo Práctico N°4: Capas de Acceso en Redes Locales, Protocolos y Fundamentos”**

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
a) Investigar cómo se clasifican las redes según su alcance. Mencionar brevemente las características principales de cada una y colocar en cada cuadro de la Figura el acrónimo de red que corresponda.

*PAN (Personal Area Network)* : Tiene un alcance de 10 metros y esta diseñada para los dispositivos de un solo usuario. Ej: Bluetooth, usb

*LAN (Local Area Network)* : Tiene un alcance que va desde algunos metros hasta 1 km, permite compartir recursos a altas velocidades de transferencia y con baja latencia. Ej: Cables Ethernet y wifi domestico

*CAN (Campus Area Network)* : Tiene un alcance desde 1 a 5 km e interconectan varias redes LAN dentro de un area delimitada ,como un campus universitario. Ej: Fibra óptica entre edificios  

*MAN (Metropolitan Area Network)* : Tiene un alcance de hasta 50 km, estas ofrecen cobertura a una area urbana completa interconectando diversas LAN de empresas, instituciones públicas o proveedores de servicios de internet. Ej: Anillos de fibra óptica, redes WiMAX

*WAN (Wide Area Network)* : Su alcance tiene cientos a miles de kilometros (para paises o hasta el planeta entero), Une redes locales dispersas geograficamente a gran escalas, la más grande y conocida es el Internet.Ej :Enlaces satelitales, cables submarinos, fibra óptica transcontinental

2)¿Qué es una vLAN? ¿Cómo se clasifican?

Es el acronimo para "Virtual Local Area Network", como dice el nombre
 es una red local virtual que permite dividir una red real en subredes logicas independientes por configuracion de switches.

Se clasifican principalmente de dos formas
 
 1- Por la asignacion de dispositivos: Estática (por puerto),Dinámica (por dirección MAC o IP)
    2- Por el tipo de trafico: Que pueden ser de datos,voz,administracion y nativa

c) Investigar y resumir el protocolo IEEE 802.1Q. ¿Cómo se relaciona con las VLAN?
El protocolo IEEE 802.1Q es un mecanismo que permite a múltiples redes compartir de forma transparente el mismo medio físico, sin problemas de interferencia entre ellas. Define el protocolo de encapsulamiento para redes Ethernet, es decir, es el estándar que define el etiquetado de las VLAN en tramas de ethernet.

d) En el contexto de los dos ítems anteriores ¿Qué es el Tagging?
Tagging es el nombre que recibe el proceso de etiquetado donde se inserta una etiqueta adicional de 4 bytes dentro de la trama original de ethernet para identificar a que VLAN pertenece el paquete.
De estos 4 bytes, los primeros 2 byets (16 bits) son el identificador de protocolo, los restantes 16 bits se distribuyen de la siguiente manera: 3 bits para la prioridad de la trama, 1 bit indicador de elegilibilidad de descarte en caso de congestion y 12 bits para el identificador de la VLAN, lo que permite soportar hasta 4096 VLAN distintas en una red. 

## Punto 2:

En el presente informe se omiten los comandos correspondientes a los incisos a al f, dado que ya se encuentran detallados en el enunciado del trabajo práctico. Tras configurar los switches con sus respectivos hostname, credenciales de acceso y la asignación de VLANs según la tabla de ruteo, verificamos la conectividad de extremo a extremo entre los hosts mediante el comando "ping".  Se muestra el resultado en las capturas de pantalla:

![Diagrama de Red](images/2.jpeg)

![Ping entre PCs](images/2g.jpeg)

Luego creamos las VLAN especificadas en el punto h) y verificamos su correcto funcionamiento con el comando "show vlan brief". Observamos que la VLAN por defecto es la VLAN 1:

![VLANs](images/2i.png)

A continuación, la interfaz FastEthernet 2/1 (correspondiente a la PC-A) se asignó a la VLAN 10 (Laboratorio). Posteriormente, se procedió a migrar la interfaz de administración: se removió la dirección IP de la interfaz virtual por defecto (VLAN 1) y se configuró en la interfaz virtual de la VLAN 99 (Management). Este procedimiento permite aislar lógicamente la administración del equipo del tráfico de los usuarios. Se visualizan los cambios en la captura:

![SW1 Management IP y puerto f2/1 en Lab](images/2l.png)

Repetimos los mismos cambios en el switch 2:

![SW2 Management IP y puerto f2/1 en Lab](images/2m.png)

Al finalizar estas configuraciones, verificamos que no hay conectividad entre las PCs ni entre los Switches, debido a la separación entre VLANs. Aunque la PC-A y la PC-B pertenecenn a la VLAN 10 (Laboratorio), se encuentran en switches distintos cuyo enlace de interconexión opera, por defecto, en la VLAN 1. Para que los paquetes alcancen su destino, es indispensable configurar este enlace en modo troncal (trunk), lo que permitirá etiquetar y transportar el tráfico de múltiples VLANs a través de la misma conexión física.

![Fallo de ping entre PCs](images/2nPC.png)

![Fallo de ping entre switch](images/2nSW.png)

## Punto 3:

El objetivo es separar el tráfico de red de los pasajeros y de la tripulación utilizando VLANs (Redes Virtuales). Esto divide la infraestructura compartida en redes lógicas independientes, permitiendo aplicar distintas reglas de acceso según requiera la aerolínea.

La topología incluye:

- Un servidor local para el sistema de entretenimiento.

- Un switch de acceso que conecta los dispositivos finales a su VLAN correspondiente.

- Un router principal (Gateway) que dirige el tráfico interno y aplica las políticas de seguridad.

- Un router externo que provee la salida a Internet.

<img title="" src="images/DiagramaLogico.png" alt="Diagrama lógico de la red" width="403" data-align="center">

#### Pruebas

- Validación Clase Turista (VLAN 10)

El dispositivo final de la clase Turista es capaz de hacer ping y resolver las peticiones HTTP hacia el servidor de entretenimiento. 

<img title="" src="images/p1.png" alt="PruebaClaseTurista1" width="463" data-align="center">

<img title="" src="images/p2.png" alt="PruebaClaseTurista2" width="520" data-align="center">

Sin embargo, al intentar enviar una solicitud de ping hacia un servidor externo (8.8.8.8) no hay éxito.

<img src="images/p3.png" title="" alt="PruebaClaseTurista3" data-align="center">

#### Análisis de la falta de conectividad a Internet en Clase Turista (VLAN 10):
El fallo en el envío de paquetes ICMP hacia direcciones públicas de Internet desde los dispositivos de la Clase Turista responde a dos restricciones configuradas intencionalmente en el router principal 1. Bloqueo por Lista de Control de Acceso: En la subinterfaz FastEthernet0/0.10 correspondiente a Turista, se encuentra aplicada una ACL extendida en sentido saliente (out) que deniega explícitamente el tráfico IP proveniente de la red privada 10.10.10.0/24 hacia cualquier otro destino exterior .   
2. Ausencia de traducción de direcciones (NAT/PAT): La función NAT con sobrecarga en la interfaz de salida hacia el ISP está habilitada únicamente para el rango de la Clase Business (access-list 20 permit 10.10.20.0 0.0.0.255). Al no pertenecer al grupo de NAT, las direcciones IP de la VLAN 10 no pueden traducirse a una IP pública para viajar a través de Internet. 

- Validación Clase Business (VLAN 20)

Desde la PC Business se accede correctamente al servidor de entretenimiento (`http://10.10.99.10`).

![PruebaBusiness1](images/p4.png)

El ping a 8.8.8.8 es exitoso: el router Aircraft aplica NAT con sobrecarga y traduce las direcciones de la VLAN 20 a la IP pública `200.0.0.1`.

![PruebaBusiness2](images/p5.png)

- Validación Admin(VLAN 99)

La PC Admin tiene conectividad con Turista, Business, el servidor e Internet (acceso total).

![PruebaAdmin](images/p6.png)


#### Conclusión

En este trabajo se realizo la red de un avión donde todos comparten los mismos equipos, pero no todos pueden acceder a las mismas funciones. Usamos VLANs para separar a los pasajeros en tres grupos: Turista, Business y Admin, como si cada grupo tuviera su propia red.

Después controlamos qué puede hacer cada uno. Turista solo puede entrar al servidor de entretenimiento, porque una ACL (una lista de reglas) le bloquea el acceso a Internet. Business puede usar el servidor e Internet, y Admin puede acceder a todo. Para que Business y Admin salgan a Internet usamos NAT, que hace que todos los dispositivos salgan con una única dirección pública.

En sintesis las pruebas salieron como se esperaba: cada grupo puede acceder a lo que le corresponde y nada más.
