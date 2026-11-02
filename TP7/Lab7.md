UNIVERSIDAD NACIONAL DE CÓRDOBA

FACULTAD DE CIENCIAS EXACTAS, FÍSICAS, Y NATURALES

CÁTEDRA DE COMPUTACIÓN

![Escudo UNC](images/image1.png)

**“Trabajo Práctico N°7: Detección y corrección de errores”**

Alumnos:  
Mariano Stroppa (46309318)  
Victor José Arturo Castro (46522607)  
Tiziano Quevedo (44972730)  
Gonzalo del Cotillo (43216694)  
Genaro Agustín Mateos Ferrero (19103190)  
Eliezer Flores (45172399)  
Angélica Moisés (46765089)

Comisión: ICOMP24-3

## Consignas

### Consigna 1

*Averigüen su IP y su máscara (ipconfig / ip addr) y calculen la dirección de broadcast de la red. ¿Cuál es la dirección MAC de broadcast?*

- **Dirección IP local:** [Completar aquí]

- **Máscara de subred:** [Completar aquí]

- **Dirección de broadcast de la red:** [Completar aquí]

- **Dirección MAC de broadcast:** [Completar aquí]

### Consigna 2

*Abran Wireshark en la interfaz Wi-Fi y capturen al menos 2 minutos.*

- **Captura:** [Indicar aquí el nombre del archivo `.pcapng` o captura de pantalla que se adjunta con este informe]

### Consigna 3

*Analicen la estructura del mensaje. ¿Qué formato tiene? ¿Qué campos contiene y qué creen que representa cada uno? Propongan cómo hay que interpretar los datos.*

- **Formato de la carga útil:** [Ej. JSON]

- **Análisis de los campos:**
  
  - `SIZE`: [Explicar su significado, ej. dimensiones de la matriz]
  
  - `PL`: [Explicar su significado, ej. payload o bits de datos]
  
  - `CHECK`: [Explicar su significado, ej. bits de paridad]

- **Interpretación de los datos:** [Explicar cómo agrupar los bits para formar la matriz y decodificarlos]

### Consigna 4

*Verifiquen la integridad del mensaje con el código de la sección 1: recalculen las paridades y compárenlas con las recibidas. Registren qué filas y qué columnas fallan (el síndrome).*

- **Matriz analizada (SIZE [X,Y]):** [Opcional: Pegar la matriz de bits extraída aquí]

- **Paridad de filas (Calculada vs Recibida):** [Detallar si hay diferencias]

- **Paridad de columnas (Calculada vs Recibida):** [Detallar si hay diferencias]

- **Síndrome detectado:** [Indicar qué filas y columnas exactas fallan]

### Consigna 5

*Si hay errores, ubíquenlos y corríjanlos. Para cada bit corregido indiquen fila, columna, valor recibido y valor corregido.*

| **Fila** | **Columna** | **Valor Recibido** | **Valor Corregido** |
| -------- | ----------- | ------------------ | ------------------- |
| [Ej. 3]  | [Ej. 4]     | [Ej. 1]            | [Ej. 0]             |
| [...]    | [...]       | [...]              | [...]               |

*(Nota: Si analizaron más de un mensaje distinto, replicar esta tabla por cada mensaje)*

### Consigna 6

*Construyan un archivo de texto en el formato de mensaje.txt con los datos ya corregidos y decodifíquenlo con decodificar_mensaje.py.*

- **Mensaje final decodificado:**
  
  > [Pegar aquí el texto final obtenido al ejecutar el script]

### Consigna 7 (Opcional)

*paridad.py calcula las paridades, pero no las compara con las recibidas.*

- **Modificación / Automatización:** [Pegar un fragmento de código o explicar brevemente cómo lograron que el script compare automáticamente y encuentre el síndrome]

## Reflexiones e investigación

### Reflexión 1

*¿Qué hubiera pasado si el mensaje tenía errores en dos bits de filas y columnas distintas? ¿Y si se dañaba un bit de los de control?*

- **Error en dos bits de datos:** [Desarrollar respuesta teórica]

- **Daño en un bit de control:** [Desarrollar respuesta teórica]

### Reflexión 2

*Si el mensaje es texto en castellano, muchas veces un error "se adivina" por contexto. ¿Sirve eso para una contraseña, un número de cuenta o una dirección web? ¿Qué aporta el código frente a "leer y adivinar"?*

- **Contexto en datos críticos:** [Desarrollar justificación]

- **Aporte del código (EDAC):** [Desarrollar justificación técnica]

### Reflexión 3

*¿Pudieron confirmar que su corrección es correcta? ¿Cómo?*

- **Método de confirmación:** [Explicar cómo validaron que la corrección fue exitosa más allá de que el texto final tuviera sentido]

### Reflexión 4

*Investigar y describir con el mayor detalle posible cómo funciona la técnica de corrección Hamming (7,4) y por qué es superior a la demostración didáctica que hicimos en este Laboratorio. Luego, aplicar la técnica sobre la carga útil obtenida.*

- **Funcionamiento del Código Hamming (7,4):** [Explicar la teoría de los bits de paridad superpuestos]

- **Superioridad técnica:** [Argumentar por qué es mejor que la paridad bidimensional]

- **Aplicación sobre la carga útil:** [Explicar o mostrar cómo estructurarían el payload del TP utilizando Hamming en lugar del método actual]