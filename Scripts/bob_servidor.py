import socket

P = 251
G = 6
PUERTO = 5000

def aplicar_xor(datos_bytes, llave_k):
    """Aplica XOR byte a byte entre el mensaje y la llave K de Diffie-Hellman."""

    print("\n" + "=" * 100)
    print("XOR byte a byte")
    print("=" * 100 + "\n")

    resultado = [byte ^ llave_k for byte in datos_bytes]
    return bytes(resultado)

def main():
    b = int(input("Introduce tu número secreto (b) [2-250]: "))

    print("\n" + "_" * 100)
    print("Clave pública (B)")
    print("=" * 100 + "\n")
    B = pow(G, b, P)
    print(f"[*] Clave pública calculada (B): {B}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("0.0.0.0", PUERTO))
        s.listen(1)
        print(f"\n[*] Esperando conexión de Alice en el puerto {PUERTO}...\n")

        conn, addr = s.accept()
        with conn:
            print(f"[*] Conexión establecida desde {addr[0]}\n")

            print("Recibe clave pública A de Alice y envia B")
            A = int(conn.recv(1024).decode().strip())
            print(f"\n[Red Pública] Recibida clave pública de Alice: A = {A}")
            conn.sendall(f"{B}".encode())
            print(f"[Red Pública] Enviada la clave pública de Bob: B = {B}")

            print("=" * 100)
            print("Clave compartida (K)")
            print("=" * 100 + "\n")

            K = pow(A, b, P)
            print(f"[*] Clave compartida calculada (K): {K}")

            print("Recibe el mensaje cifrado y aplicar XOR con K")
            mensaje_cifrado = conn.recv(4096)
            print(f"\n[Tráfico Cifrado en Red (Hex)]: {mensaje_cifrado.hex(' ').upper()}\n")

            print("=" * 100)
            print("XOR con K")
            print("=" * 100 + "\n")
            mensaje_descifrado = aplicar_xor(mensaje_cifrado, K)

            try:
                texto_plano = mensaje_descifrado.decode('utf-8')
            except UnicodeDecodeError:
                texto_plano = mensaje_descifrado.decode('latin-1')

            print(f"\n[+] Mensaje descifrado en texto plano: {texto_plano}")

if __name__ == "__main__":
    main()
