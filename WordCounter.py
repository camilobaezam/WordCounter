import os
import string

def contar_palabras(texto):
    """Convierte el texto a minúsculas y cuenta la frecuencia de cada palabra."""
    # Convertir a minúsculas
    texto = texto.lower()
    
    # Reemplazar signos de puntuación por espacios
    for signo in string.punctuation:
        texto = texto.replace(signo, ' ')
    
    # Dividir en palabras y eliminar espacios múltiples
    palabras = texto.split()
    
    # Contar frecuencia con diccionario
    conteo = {}
    for palabra in palabras:
        if palabra:  # Ignorar cadenas vacías
            conteo[palabra] = conteo.get(palabra, 0) + 1
    
    return conteo

def mostrar_mas_frecuentes(conteo, top_n=10):
    """Muestra las palabras más frecuentes (de mayor a menor)."""
    # Ordenar por frecuencia descendente y luego por palabra alfabéticamente
    palabras_ordenadas = sorted(conteo.items(), key=lambda x: (-x[1], x[0]))
    
    print(f"\nLas {top_n} palabras más frecuentes (o todas si hay menos):")
    print("-" * 50)
    for i, (palabra, frecuencia) in enumerate(palabras_ordenadas[:top_n], 1):
        print(f"{i:2d}. {palabra:20} → {frecuencia} veces")
    print("-" * 50)

def main():
    print("=== WordCounter - Contador de palabras ===\n")
    
    while True:
        archivo = input("Ingresa la ruta del archivo de texto (o 'salir' para terminar): ").strip()
        
        if archivo.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        if not os.path.exists(archivo):
            print("El archivo no existe. Intenta nuevamente.\n")
            continue
        
        try:
            with open(archivo, 'r', encoding='utf-8') as f:
                texto = f.read()
            
            conteo = contar_palabras(texto)
            
            if not conteo:
                print("El archivo está vacío o no contiene palabras válidas.\n")
                continue
            
            # Mostrar total de palabras únicas y total de palabras
            total_palabras = sum(conteo.values())
            print(f"\nTotal de palabras encontradas: {total_palabras}")
            print(f"Total de palabras únicas: {len(conteo)}\n")
            
            # Preguntar cuántas mostrar
            try:
                n = input("¿Cuántas palabras más frecuentes quieres ver? (Enter para 10): ")
                top_n = int(n) if n.strip() else 10
            except ValueError:
                top_n = 10
            
            mostrar_mas_frecuentes(conteo, top_n)
            
        except Exception as e:
            print(f"Error al leer el archivo: {e}\n")

if __name__ == "__main__":
    main()
