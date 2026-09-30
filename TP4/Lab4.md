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

- Validación Clase Business (VLAN 20)

Desde la PC Business se accede correctamente al servidor de entretenimiento (`http://10.10.99.10`).

![PruebaBusiness1](images/p4.png)

El ping a 8.8.8.8 es exitoso: el router Aircraft aplica NAT con sobrecarga (PAT) y traduce las direcciones de la VLAN 20 a la IP pública `200.0.0.1`.

![PruebaBusiness2](images/p5.png)

- Validación Admin(VLAN 99)

La PC Admin tiene conectividad con Turista, Business, el servidor e Internet (acceso total).

![PruebaAdmin](images/p6.png)

#### Conclusión

#### Conclusión

En este trabajo se realizo la red de un avión donde todos comparten los mismos equipos, pero no todos pueden acceder a las mismas funciones. Usamos VLANs para separar a los pasajeros en tres grupos: Turista, Business y Admin, como si cada grupo tuviera su propia red.

Después controlamos qué puede hacer cada uno. Turista solo puede entrar al servidor de entretenimiento, porque una ACL (una lista de reglas) le bloquea el acceso a Internet. Business puede usar el servidor e Internet, y Admin puede acceder a todo. Para que Business y Admin salgan a Internet usamos NAT, que hace que todos los dispositivos salgan con una única dirección pública.

En sintesis las pruebas salieron como se esperaba: cada grupo puede acceder a lo que le corresponde y nada más.