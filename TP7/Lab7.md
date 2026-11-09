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

![Screenshot IP config cmd](images/image4.png)

- **Dirección IP local:** 192.168.0.135
- **Máscara de subred:** 255.255.255.0
- **Dirección de broadcast de la red:** Para calcularla hacemos IP local OR (NOT) máscara de subred. Entonces como la máscara es 255.255.255.0, haciendo NOT queda 0.0.0.255 y haciendo el OR: (192.168.0.135) OR (0.0.0.255) = 192.168.0.255
- **Dirección MAC de broadcast:** FF:FF:FF:FF:FF:FF

### Consigna 2

*Abran Wireshark en la interfaz Wi-Fi y capturen al menos 2 minutos.*

- **Captura:** Adjuntamos dos archivos de capturas de wireshark bajo los nombres "TP7-captura1.pcapng" y "TP7-captura2.pcapng" en la carpeta titulada "Capturas wireshark". A su vez, para mejor visualización en este informe, mostramos capturas de pantalla de algunos paquetes:

![Ejemplo 1 paquete](images/image2.png)

![Ejemplo 2 paquete](images/image3.png)

### Consigna 3

*Analicen la estructura del mensaje. ¿Qué formato tiene? ¿Qué campos contiene y qué creen que representa cada uno? Propongan cómo hay que interpretar los datos.*

- **Formato de la carga útil:**
  El formato de la carga útil es explicitado en la consigna de este trabajo, donde se aclara que se trata de un JSON de forma {"SIZE": "FILAS, COLUMNAS", ???????}.
- **Análisis de los campos:**

  - `SIZE`: Este campo funciona para declarar el tamaño de la matriz, primero el número de filas y luego el número de columnas. Estos parámetros nos serán utiles en el momento de armar la matriz.
  - `PL`: Este campo contiene el payload de unos y ceros que, por más que están en código ASCII por lo cual cada número es en realidad 7 bits, para este caso representan bits que tendremos que decodificar con el archivo "decodificar_mensaje.py".
  - `CHECK`: Este campo también es compuesto de unos y ceros que representan los bits de paridad, primero de las filas (de arriba a abajo) y luego de las columnas (de izquierda a derecha).
- **Interpretación de los datos:** Al captar un paquete debemos armar la matriz de datos para poder utilizar el código "paridad.py" y ver los bits de paridad que devuelve para las filas y columnas. Entonces podremos detectar errores comparando con los bits de paridad otorgados en el campo CHECK.
  Para armar la matriz, primero se debe leer el campo SIZE para poder ordenar los bits de datos del campo PL. Tomamos en cuenta que se nos dice el número de filas N y de columnas M, pero para estas últimas se habla de 7 "bits" en cada una ya que se interpreta como un caracter ASCII. Entonces podemos copiar desde wireshark el campo PL, pegarlo en un archivo de texto y separar en N columnas de 7 bits debeiendo quedar M filas.
  Aquí solo queda realizar la detección y corrección de errores como ya se mencionó antes; utilizamos "paridad.py" y comparamos sus resultados con los datos del campo CHECK. Al finalizar, habiendo cambiado los bits necesarios, pudimos reconstruir el mensaje original y decodificando en ASCII con "decodificar_mensaje.py" sabremos exactamente qué decía.

### Consigna 4

*Verifiquen la integridad del mensaje con el código de la sección 1: recalculen las paridades y compárenlas con las recibidas. Registren qué filas y qué columnas fallan (el síndrome).*

#### Análisis de Payload 1

- **Matriz analizada (SIZE [8, 7]):** El mensaje original de 392 bits se organizó en una matriz bidimensional de 8 filas por 49 columnas (representando 7 caracteres ASCII de 7 bits por cada fila).
- **Paridad de filas:** Al comparar contra los bits de control del campo CHECK, se detectaron discrepancias en las filas 4, 5 y 6 (el índice comienza desde 0).
- **Paridad de columnas** Existen diferencias en las columnas 8, 16 y 22.
- **Síndrome detectado:** El cruce de paridades indica errores simultáneos en las intersecciones de las **filas 4, 5 y 6** con las **columnas 8, 16 y 22**.

**Evidencia Payload 1:**

Mensaje con errores:

Matriz de paridad:
Detección de errores:
![Detección de errores P1](images/P1DeteccionDeErrores.png)

---

#### Análisis de Payload 2

- **Matriz analizada (SIZE [10, 42]):** El segundo mensaje, de 420 bits, fue estructurado en 10 filas por 42 columnas (6 caracteres ASCII por fila).
- **Paridad de filas (Calculada vs Recibida):** El cálculo local arrojó discrepancias con el control recibido en las filas 0, 4, 5 y 7.
- **Paridad de columnas (Calculada vs Recibida):** Se detectaron discrepancias en las columnas 2, 11, 17 y 24.
- **Síndrome detectado:** El análisis expone un síndrome de error múltiple que afecta las coordenadas donde se cruzan las **filas 0, 4, 5 y 7** y las **columnas 2, 11, 17 y 24**.

**Evidencia Payload 2:**
Mensaje con errores:
Matriz de paridad:
Detección de errores:

---

#### Análisis de Payload 3

- **Matriz analizada (SIZE [4, 28]):** El tercer mensaje consta de 112 bits, divididos en 4 filas por 28 columnas.
- **Paridad de filas:** Todas las filas presentan discrepancias matemáticas respecto al control (filas 0, 1, 2 y 3).
- **Paridad de columnas (Calculada vs Recibida):** Fallan las columnas 6, 10, 14 y 19.
- **Síndrome detectado:** Existe una ambigüedad masiva. El síndrome abarca la totalidad de las filas (**0, 1, 2 y 3**) y las columnas **6, 10, 14 y 19**. Al existir 4 filas y 4 columnas afectadas, la paridad bidimensional genera múltiples combinaciones posibles (24 combinaciones) que comparten el mismo síndrome, demostrando que en fallos múltiples se requiere del contexto semántico (tabla ASCII) para resolver la corrección.

**Evidencia Payload 3:**
Mensaje con errores:
Matriz de paridad:
Detección de errores:

### Consigna 5

*Si hay errores, ubíquenlos y corríjanlos. Para cada bit corregido indiquen fila, columna, valor recibido y valor corregido.*

| **Fila** | **Columna** | **Valor Recibido** | **Valor Corregido** |
| -------------- | ----------------- | ------------------------ | ------------------------- |
| [Ej. 3]        | [Ej. 4]           | [Ej. 1]                  | [Ej. 0]                   |
| [...]          | [...]             | [...]                    | [...]                     |

*(Nota: Si analizaron más de un mensaje distinto, replicar esta tabla por cada mensaje)*

#### Payload 1 (matriz 8 × 49)

| **Fila** | **Columna** | **Valor Recibido** | **Valor Corregido** | **Carácter afectado** |
| -------------- | ----------------- | ------------------------ | ------------------------- | ---------------------------- |
| 4              | 8                 | 1                        | 0                         | `w` → `W`               |
| 5              | 16                | 0                        | 1                         | `$` → `4`               |
| 6              | 22                | 0                        | 1                         | `E` → `e`               |

#### Payload 2 (matriz 10 × 42)

| **Fila** | **Columna** | **Valor Recibido** | **Valor Corregido** | **Carácter afectado** |
| -------------- | ----------------- | ------------------------ | ------------------------- | ---------------------------- |
| 0              | 2                 | 1                        | 0                         | `x` → `h`               |
| 4              | 11                | 1                        | 0                         | `w` → `s`               |
| 5              | 17                | 1                        | 0                         | `}` → `u`               |
| 7              | 24                | 1                        | 0                         | `m` → `e`               |

#### Payload 3 (matriz 4 × 28)

| **Fila** | **Columna** | **Valor Recibido** | **Valor Corregido** | **Carácter afectado** |
| -------------- | ----------------- | ------------------------ | ------------------------- | ---------------------------- |
| 0              | 6                 | 1                        | 0                         | `Q` → `P`               |
| 1              | 10                | 1                        | 0                         | `8` → `0`               |
| 2              | 14                | 1                        | 0                         | `p` → `0`               |
| 3              | 19                | 1                        | 0                         | `g` → `e`               |

### Consigna 6

*Construyan un archivo de texto en el formato de mensaje.txt con los datos ya corregidos y decodifíquenlo con decodificar_mensaje.py.*

Para cada payload armamos un archivo con el mismo formato que `mensaje.txt.`Partimos del campo `PL`, lo cortamos en filas según `SIZE` (cada fila tiene M caracteres × 7 bits) e invertimos los bits que corregimos en la Consigna 5. Los archivos están en la carpeta `codigo/`:

| Payload      | Matriz recibida  | Matriz corregida           |
| ------------ | ---------------- | -------------------------- |
| 1 (8 × 49)  | `payload1.txt` | `payload1_corregido.txt` |
| 2 (10 × 42) | `payload2.txt` | `payload2_corregido.txt` |
| 3 (4 × 28)  | `payload3.txt` | `payload3_corregido.txt` |

`decodificar_mensaje.py` decodifica cada línea por separado, así que la salida aparece cortada en una línea por fila de la matriz (`https:/`, `/youtub`). Unimos esas líneas y descartamos los espacios de relleno de la última fila (`0100000` es el espacio en ASCII).

- **Mensaje final decodificado:**

  | Payload | Recibido (con errores)                                   | Corregido                                                |
  | ------- | -------------------------------------------------------- | -------------------------------------------------------- |
  | 1       | `https://youtube.com/shorts/q8wgKzJwPa$?featurE=share` | `https://youtube.com/shorts/q8WgKzJwPa4?feature=share` |
  | 2       | `xttps://youtube.com/shortw/WCi5h}1EqqI?featurm=share` | `https://youtube.com/shorts/WCi5hu1EqqI?feature=share` |
  | 3       | `Qr3mi8!:)1p-dIgZ`                                     | `Pr3mi0!:)10-dIeZ`                                     |


  > Payload 1: https://youtube.com/shorts/q8WgKzJwPa4?feature=share
  >
  > Payload 2: https://youtube.com/shorts/WCi5hu1EqqI?feature=share
  >
  > Payload 3: Pr3mi0!:)10-dIeZ
  >
- En los payloads 1 y 2 el resultado es una URL válida. El payload 3 no tiene contexto semántico (parece una contraseña). Además, fallan cuatro filas y cuatro columnas a la vez. Cuando falla una sola fila y una sola columna, el error está en su cruce; pero con cuatro de cada una sabemos que hay un bit erróneo en cada fila y en cada columna, sin saber qué fila corresponde a qué columna. Hay varias formas de emparejarlas, y con cualquiera de ellas todas las paridades calculadas coinciden con las recibidas. `Pr3mi0!:)10-dIeZ` corresponde a la combinación elegida en la Consigna 5, pero la paridad por sí sola no puede garantizar que sea la correcta: como advierte la consigna, un mensaje que “se lee bien” no es necesariamente correcto.

### Consigna 7 (Opcional)

*paridad.py calcula las paridades, pero no las compara con las recibidas.*

- **Modificación:** modificamos `paridad.py` (en la carpeta `codigo`) para que, además de calcular las paridades, las compare con los bits de control recibidos en el campo `CHECK` e informe qué filas y qué columnas fallan. Los cambios son dos:

  1. **Nuevo argumento opcional.** Después del nombre del archivo se pueden pasar los bits del campo `CHECK`. Si no se pasan, el script funciona exactamente igual que antes.
  2. **Comparación con las paridades recibidas.** Al final del script, sólo si se pasó `CHECK`, se vuelven a calcular las paridades de filas y columnas, se separa `CHECK` en sus dos partes (primero un bit por fila, de arriba hacia abajo, y luego uno por columna, de izquierda a derecha) y se compara posición por posición. Se imprimen las filas y columnas en las que la paridad calculada no coincide con la recibida (numeradas desde 0):

  Ejemplo con el payload 3. Primero se muestra la matriz igual que en el script original y debajo se agrega el resultado de la comparación:

  ```text
  $ python paridad.py payload3.txt 10001110100011101010001110100000
  1010001111001001100111101101 |0
  1101001011100001000010111010 |1
  0101001011000111100000101101 |1
  1100100100100111001111011010 |1
  ------------------------------
  1110101011001000001010100000

  Filas que fallan:    [0, 1, 2, 3]
  Columnas que fallan: [6, 10, 14, 19]
  ```

  Resultados al ejecutarlo sobre cada matriz:

  | Archivo                    | Filas que fallan | Columnas que fallan |
  | -------------------------- | ---------------- | ------------------- |
  | `payload1.txt`           | [4, 5, 6]        | [8, 16, 22]         |
  | `payload2.txt`           | [0, 4, 5, 7]     | [2, 11, 17, 24]     |
  | `payload3.txt`           | [0, 1, 2, 3]     | [6, 10, 14, 19]     |
  | `payload1_corregido.txt` | []               | []                  |
  | `payload2_corregido.txt` | []               | []                  |
  | `payload3_corregido.txt` | []               | []                  |

  Con las matrices recibidas, el script obtiene las mismas filas y columnas que registramos a mano en la Consigna 4. Con las matrices corregidas de la Consigna 6, las dos listas quedan vacías y todas las paridades calculadas coinciden con las recibidas.

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

Sí, pudimos validar que la corrección fue exitosa de forma objetiva y formal, más allá de que el texto final decodificado fuera legible en español, aplicando las siguientes verificaciones técnicas:

- **Recálculo de la matriz de paridad (Síndrome nulo)**: Reejecutamos el script paridad.py utilizando como entrada la matriz con los bits de datos ya corregidos. Al comparar nuevamente las paridades de filas y columnas calculadas de la nueva matriz contra los vectores de control originales recibidos en el campo CHECK, el resultado arrojó un síndrome nulo (cero discrepancias). Esto demuestra matemáticamente que la matriz corregida satisface al 100% las ecuaciones de paridad del esquema bidimensional.
- **Verificación sintáctica del código ASCII y JSON**: Comprobamos que cada bloque de 7 bits resultante perteneciera al rango de caracteres ASCII imprimibles y respetara la estructura JSON exigida por la consigna ({"SIZE": ...}). En escenarios con síndromes ambiguos (como ocurrió en el Payload 3, donde la falla cruzada de 4 filas y 4 columnas generaba múltiples combinaciones matemáticamente válidas), este criterio permitió descartar de forma inequívoca las soluciones que producían símbolos no imprimibles o combinaciones inválidas en la sintaxis.

### Reflexión 4

*Investigar y describir con el mayor detalle posible cómo funciona la técnica de corrección Hamming (7,4) y por qué es superior a la demostración didáctica que hicimos en este Laboratorio. Luego, aplicar la técnica sobre la carga útil obtenida.*

- **Funcionamiento del Código Hamming (7,4):** [Explicar la teoría de los bits de paridad superpuestos]
El código Hamming (7,4) es un algoritmo de detección y corrección de errores (EDAC) perteneciente a la familia de códigos lineales de bloque. Su nomenclatura indica que toma bloques de 4 bits de datos reales (d_1, d_2, d_3, d_4) y les añade 3 bits de paridad (p_1, p_2, p_3), generando una palabra de código (codeword) de 7 bits en total.
Para garantizar que cada bit de paridad pueda supervisar un grupo único de bits, las posiciones de los bits de paridad se asignan en potencias de 2 (posiciones 2^0, 2^1, 2^2), mientras que los datos se distribuyen en las posiciones restantes:
Posición del bit: 1(2^0)| 2(2^1) | 3 | 4(2^2) | 5 | 6 | 7 |
Tipo de bit:       p_1  | p_2    |d_1|  p_3   | d_2| d_3| d_4 |
Cada bit de paridad cubre a todas las posiciones cuya representación en binario contiene un 1 en su mismo peso de bit:
p_1 (Posición 1 = 001): Supervisa posiciones con un 1 en el bit menos significativo (1, 3, 5, 7).
p_2 (Posición 2 = 010): Supervisa posiciones con un 1 en el bit central (2, 3, 6, 7).
p_3 (Posición 4 = 100): Supervisa posiciones con un 1 en el bit más significativo (4, 5, 6, 7).

Al recibir el bloque de 7 bits, el receptor recalcula tres bits de verificación (s_1, s_2, s_3):
La combinación del síndrome vector (s_3 s_2 s_1)_2 en binario da directamente la dirección exacta del bit erróneo en base 10: 
- Si el síndrome es 000: el mensaje no tiene errores.
- Si el síndrome es 110 (6_{10}): el error se encuentra en la posición 6. Basta con invertir ese bit (0 --> 1 o 1 --> 0) para corregirlo automáticamente.

- **Superioridad técnica:** [Argumentar por qué es mejor que la paridad bidimensional]
Aunque la paridad bidimensional (utilizada en la práctica del laboratorio) es conceptualmente intuitiva, Hamming (7,4) presenta ventajas estructurales decisivas:
1- Resolución Inequívoca de Errores (Sin Ambigüedad):
- Paridad Bidimensional: Cuando ocurren fallos en múltiples filas y columnas (como ocurrió en el Payload 3, con 4 filas y 4 columnas afectadas), el método bidimensional genera múltiples combinaciones válidas (24 combinaciones posibles que satisfacen la paridad). Para corregirlo se requirió de la interpretación contextual humana (tabla ASCII).
- Hamming (7,4): Resuelve cualquier error de un bit por bloque de manera algebraicamente determinista. No depende del contexto semántico del mensaje ni de la intervención del operador.

2- Procesamiento en Flujo continuo (Streaming) y menor latencia:
- Paridad Bidimensional: Exige almacenar y estructurar la matriz completa (N X M) antes de poder verificar y calcular las paridades.
- Hamming (7,4): Opera por bloques independientes de 7 bits. La verificación y corrección suceden bit por bit en hardware de forma instantánea conforme llegan los datos, reduciendo significativamente la memoria de búfer requerida.

3- Eficiencia y Overhead predecible:
- Paridad Bidimensional: El costo de redundancia depende de las dimensiones arbitrarias asignadas a la matriz (N filas + M columnas de paridad).
- Hamming (7,4): Mantiene una sobrecarga fija y estandarizada ($4$ bits útiles por cada 7 transmitidos, rendimiento cercano a 57,1%).

4- Extensibilidad a Hamming (8,4) / SEC-DED:
- Añadiendo un octavo bit de paridad global al bloque (Hamming (8,4)), la técnica permite corregir un error simple y detectar dos errores simultáneos (SEC-DED), ofreciendo una robustez ante ruido que la paridad matricial no puede garantizar.

- **Aplicación sobre la carga útil:** [Explicar o mostrar cómo estructurarían el payload del TP utilizando Hamming en lugar del método actual]
Para codificar el payload con Hamming (7,4) en lugar de la estructura matricial del TP, se deben dividir los caracteres del mensaje en nibbles (bloques de 4 bits de datos).
Tomemos el primer carácter del Payload 1 corregido: la letra h.
1. Conversión a ASCII (7 bits): h = 1101000 en binario. Completando a un bloque de 8 bits (byte completo) para dividirlo en 2 nibbles: 0110 1000.
2. Codificación del primer nibble (0110):
Datos: d_1 = 0, d_2 = 1, d_3 = 1, d_4 = 0.
Calculo de paridades:
p1 = 1 ; p2 = 1; p3 = 0;
Palabra Hamming (7,4) generada:
[p1,p2,d1,p3,d2,d3,d4] = [1,1,0,0,1,1,0]

Si durante el envío se corrompe el bit de la posición 6 (d_3 pasa de 1 a 0), se recibe el vector: [1,1,0,0,1,0,0].
En el receptor se calcula el síndrome: 
s_1 = 0; s_2 = 1; s_3= 1;
El síndrome resulta ser (s_3 s_2 s_1)_2 = (110)_2 = 6_10.
El sistema identifica en tiempo real que el fallo proviene exactamente de la posición 6, invierte el bit de 0 a 1 y restaura el dato original 0110 de forma automática.
