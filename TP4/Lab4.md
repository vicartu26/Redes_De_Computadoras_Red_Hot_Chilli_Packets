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

Decidimos omitir en el presente informe los comandos de los puntos a) al f) ya que son mostrados en la misma consigna del trabajo. Al finalizar de realizar las configuraciones correspondientes a los switch, con sus respectivos nombres y contraseñas además de sus VLAN de la tabla de ruteo; testeamos la comunicación entre las computadoras realizando pings. Se muestra el resultado en las capturas de pantalla:

![Diagrama de Red](images/2.jpeg)

![Ping entre PCs](images/2g.jpeg)

Luego creamos las VLAN especificadas en el punto h) y verificamos su correcto funcionamiento con el comando "show vlan brief". Observamos que la VLAN por defecto es la VLAN 1:

![VLANs](images/2i.png)

Los siguientes pasos constaron en asignar el puerto de la PC A (Fa2/1) a la VLAN 10 "Laboratorio" y cambiar la dirección de IP de la VLAN 1 a la 99 "Management" para que las configuraciones del switch se deban hacer desde allí y quede separado del tráfico de usuarios. Se visualizan ambos cambios en la captura:

![SW1 Management IP y puerto f2/1 en Lab](images/2l.png)

Repetimos los mismos cambios en el switch 2:

![SW2 Management IP y puerto f2/1 en Lab](images/2m.png)

Al finalizar estas configuraciones, verificamos que no hay conectividad entre las PCs ni entre los Switch, debido a la separación entre VLANs. Esto es así por más que la PC A y B estén en "Laboratirio", ya que se trata de distintos switches que están conectados por un solo puerto de acceso que sigue utilizando la VLAN 1 por defecto. Para habilitar la comunicación entre computadoras deberíamos tener un enlace troncal entre los switches para soportar el tráfico de múltiples VLAN.

![Fallo de ping entre PCs](images/2nPC.png)

![Fallo de ping entre switch](images/2nSW.png)

## Punto 3:

