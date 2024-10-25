print(" ")
print("Alvaro Campechano 3W")
print(" ")
# programa_lectura_archivo.py

def leer_archivo(ruta_archivo):
    """
    Esta función abre un archivo en la ruta especificada y lee su contenido.
    
    Args:
        ruta_archivo (str): La ruta completa del archivo a leer.
        
    Returns:
        None
    """
    try:
        # Abrir el archivo en modo lectura
        f = open(ruta_archivo, "r")
        # Leer y mostrar el contenido del archivo
        print(f.read())
    except FileNotFoundError:
        print(f"El archivo {ruta_archivo} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
    finally:
        # Asegurarse de cerrar el archivo
        f.close()

if __name__ == "__main__":
    # Especifica la ruta del archivo que deseas leer
    ruta = "D:\\myfiles\\welcome.txt"  # Cambia esta ruta según sea necesario
    leer_archivo(ruta)
