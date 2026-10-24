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

* **IPv4 configurada:** [Indicar IP]
* **Máscara de subred:** [Indicar Máscara]
* **Default Gateway:** [Indicar Gateway]
* **Justificación:** *Explicar el por qué se eligieron estas direcciones y analizar si tuvo o no sentido su configuración manual para el alcance de esta actividad local.*

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
  
  
