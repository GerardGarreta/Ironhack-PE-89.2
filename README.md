# Ironhack PE 89.2

PARTE 1 Selección de técnicas criptográficas

Ejercicio 1. Selección de la técnica adecuada

A continuación se relacionan las necesidades de seguridad con la técnica criptográfica más idónea y su justificación breve:

| Necesidad de seguridad | Técnica seleccionada | Justificación |
| :--- | :--- | :--- |
| **Proteger un gran volumen de información cuando emisor y receptor ya comparten una clave secreta** | Cifrado simétrico (ej. AES) | Los algoritmos simétricos son mucho más rápidos y eficientes que los asimétricos al procesar grandes volúmenes de datos, utilizando la misma clave tanto para cifrar como para descifrar. |
| **Proteger un secreto destinado a un receptor sin haber acordado previamente una clave compartida** | Cifrado asimétrico (ej. RSA) | Utiliza un par de claves (pública y privada). El emisor cifra el mensaje con la clave pública del receptor, y solo este último podrá descifrarlo usando su clave privada sin necesidad de intercambio previo. |
| **Detectar si un archivo ha sido modificado** | Función hash (ej. SHA-256) | Genera una huella digital única (resumen) de tamaño fijo para el archivo. Cualquier alteración mínima en el contenido producirá un hash completamente distinto, evidenciando la modificación. |
| **Comprobar la identidad de un servidor web** | Certificado digital (ej. X.509) | Vincula la identidad del servidor con su clave pública mediante la firma de una Autoridad de Certificación (CA) de confianza, permitiendo al cliente verificar quién está al otro lado. |
| **Acordar una clave compartida a través de una red insegura** | Intercambio de claves Diffie-Hellman | Es un protocolo criptográfico que permite a dos partes establecer una clave secreta común sobre un canal público e inseguro sin transmitir la clave directamente. |
| **Demostrar que un documento ha sido firmado por una determinada entidad y detectar modificaciones posteriores** | Firma digital | Combina una función hash y el cifrado asimétrico con la clave privada del firmante. Aporta autenticidad, no repudio y garantiza la integridad (detección de cambios). |

______________________________________________________________________________________________________________________________________________________________________________________________________________________________

Ejercicio 2. Selección de una configuración segura

¿Qué configuración seleccionarías para proteger una comunicación actual? Justifica la respuesta.

 - Seleccionaría la Configuración B, ya que es la única que cumple con los estándares actuales de seguridad recomendados:
 - Certificado RSA de 2048 bits: Ofrece un nivel de seguridad robusto frente al tamaño obsoleto de 1024 bits.
 - SHA-256: Es una función hash criptográfica segura, muy superior a SHA-1 o MD5, que ya presentan vulnerabilidades conocidas frente a ataques de colisión.
 - TLS 1.3: Es la versión más reciente, rápida y segura del protocolo TLS, eliminando algoritmos obsoletos y reduciendo la latencia y la superficie de ataque en comparación con TLS 1.0.

¿Por qué rechazarías las otras dos configuraciones? Identifica al menos un problema de seguridad en cada una.

Configuración A (rechazada por):

 - Uso de TLS 1.0: Es un protocolo antiguo (deprecado oficialmente) vulnerable a diversos ataques como BEAST o POODLE.
 - Uso de SHA-1: Está considerado criptográficamente débil y vulnerable a ataques de colisión (creación de dos ficheros distintos con el mismo hash).
 - RSA de 1024 bits: Hoy en día se considera una longitud de clave insuficiente y vulnerable ante la capacidad de cómputo actual.

Configuración C (rechazada por):

 - HTTP sin TLS: Los datos viajan en texto plano (en claro), lo que permite ataques de escucha pasiva (sniffing) y de intermediario (Man-in-the-Middle).
 - Uso de MD5: Es una función hash totalmente rota y vulnerable a colisiones rápidas.
 - Clave secreta en el mensaje: Enviar la clave junto al mensaje elimina por completo la confidencialidad, ya que cualquiera que interceptes el mensaje obtendrá la clave para descifrarlo.

Explica la diferencia entre cifrar un mensaje y calcular su hash.

 - Cifrado: Es un proceso reversible. Su objetivo principal es garantizar la confidencialidad transformando un mensaje legible (texto claro) en ilegible (texto cifrado) mediante una clave, de modo que el receptor autorizado pueda revertir el proceso y leerlo.

 - Función Hash: Es un proceso unidireccional (irreversible). Su objetivo principal es garantizar la integridad, generando una cadena de caracteres de longitud fija (resumen o huella) a partir de un archivo o mensaje, siendo imposible reconstruir el mensaje original a partir de su hash.

¿Qué propiedades de seguridad puede aportar un certificado digital dentro de una comunicación TLS?
Un certificado digital en el contexto de TLS aporta principalmente:

 - Autenticación: Permite al cliente (y opcionalmente al servidor) verificar la identidad real de la entidad con la que se está comunicando, evitando ataques de suplantación (phishing o Man-in-the-Middle).
 - Claves seguras: Contiene la clave pública de la entidad, necesaria para llevar a cabo el intercambio o acuerdo de claves que darán paso a una sesión cifrada segura y simétrica.

______________________________________________________________________________________________________________________________________________________________________________________________________________________________


PARTE-2 Intercambio de claves mediante Diffie–Hellman y cifrado XOR

Ejercicio 1. Preparación del entorno

- Generación de script para la creación del entorno: "Crear.sh"
  
  -    Crea la estructura de directorios
  -    Crea el docker-compose.yml
  -    Levanta el entorno con el docker compose
  -    Comprueba que los contenedores estén en ejecución

- Archivos del ejercicio:

  - [Crear.sh](./Scripts/Crear.sh)
  - [docker-compose.yml](./docker-compose.yml)
     
______________________________________________________________________________________________________________________________________________________________________________________________________________________________

Ejercicio 2. Servidor Bob

- Generación del Python: "bob_servidor.py"

- Aechivo del ejercicio:

  - [bob_servidor.py](./Scripts/bob_servidor.py)

______________________________________________________________________________________________________________________________________________________________________________________________________________________________

Ejercicio 3. Cliente Alice

- Generación del Python: "alice_cliente.py"

- Aechivo del ejercicio:

  - [alice_cliente.py](./Scripts/alice_cliente.py)

______________________________________________________________________________________________________________________________________________________________________________________________________________________________

Ejercicio 4. Comprobación

| Elemento | Valor |
| :--- | :--- |
| Clave privada de Alice | 3 |
| Clave pública de Alice | 216 (6^3 \bmod 251) |
| Clave privada de Bob | 4 |
| Clave pública de Bob | 41 | (6^4 \bmod 251) |
| Clave compartida calculada por Alice | 147 (41^3 \bmod 251) |
| Clave compartida calculada por Bob | 147 (216^4 \bmod 251) |
| Mensaje original | Hola Bob! |
| Mensaje cifrado en hexadecimal | DB F4 EF F6 B3 D9 F4 F1 B2 |
| Mensaje recuperado por Bob | Hola Bob! |

Evidencias:

- [bob_servidor.png](./Evidencias/bob_servidor.png)
- [alice_cliente.png](./Evidencias/alice_cliente.png)


