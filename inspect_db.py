import pickle
import pprint
import sys


def read_binary(filename: str) -> None:
    try:
        with open(filename, "rb") as file:
            data = pickle.load(file)
            print(f"\n--- Contenido de {filename} ---")
            # pprint indenta los diccionarios automáticamente
            pprint.pprint(data, indent=4)
            print("-" * 30 + "\n")
    except FileNotFoundError:
        print(f"Error: El archivo '{filename}' no existe.")
    except EOFError:
        print(f"El archivo '{filename}' está completamente vacío.")


if __name__ == "__main__":
    # Puedes cambiar el nombre del archivo aquí para inspeccionar otros
    archivo_a_leer = sys.argv[1] if len(sys.argv) > 1 else "users.bin"
    read_binary(archivo_a_leer)
