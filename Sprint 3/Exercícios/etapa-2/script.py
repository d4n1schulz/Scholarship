import hashlib

def main():
    while True:
        input_usuario = input("Digite uma string para mascarar (ou 'sair' para encerrar): ")
        if input_usuario.lower() == "sair":
            print("Encerrando o programa...")
            break
        hash_object = hashlib.sha1(input_usuario.encode())
        print(f"Hash SHA-1: {hash_object.hexdigest()}")

if __name__ == "__main__":
    main()
