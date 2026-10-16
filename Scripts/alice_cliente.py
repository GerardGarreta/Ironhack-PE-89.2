import socket

P = 251
G = 6
IP_BOB = "172.28.0.10"
PUERTO = 5000


def aplicar_xor(datos_bytes, llave_k):
    """Aplica XOR byte a byte entre el texto claro y la llave K."""

    print("=" * 100)
    print("XOR byte a byte")
    print("=" * 100 + "\n")

    resultado = [byte ^ llave_k for byte in datos_bytes]
    return bytes(resultado)


def main():

    print("\n" + "=" * 100)
    print("Clave privada (a)")
    print("Clave pública (A)")
    print("=" * 100 + "\n")
    a = int(input("Introduce tu número secreto (a) [2-250]: \n"))
    A = pow(G, a, P)
    print(f"[*] Clave pública calculada (A): {A}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"\n[*] Conectando con el contenedor de Bob ({IP_BOB}:{PUERTO})...\n")
        s.connect((IP_BOB, PUERTO))

        print("Envía clave pública A y recibe clave pública B\n")
        s.sendall(f"{A}".encode())
        B = int(s.recv(1024).decode().strip())
        print(f"[Red Pública] Enviada clave pública A = {A} | Recibida clave pública B = {B}")

        print("\n" + "=" * 100)
        print("Clave compartida (K)")
        print(" - Pide mensaje para cifrarlo con XOR usando K")
        print("=" * 100 + "\n")
        K = pow(B, a, P)
        print(f"[*] Clave compartida calculada (K): {K}")

        mensaje = input("\nIntroduce el mensaje de texto a enviar: ")
        bytes_mensaje = mensaje.encode('utf-8')

        bytes_cifrados = aplicar_xor(bytes_mensaje, K)

        print("\nEnviando mensaje a Bob...")
        print(f"\n[Enviando por la red en Hex]: {bytes_cifrados.hex(' ').upper()}")
        s.sendall(bytes_cifrados)
        print("\n[+] ¡Mensaje cifrado enviado con éxito!")


if __name__ == "__main__":
    main()
