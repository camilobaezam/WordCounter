# WordCounter

Un contador de palabras simple en Python. Lee un archivo de texto, cuenta la frecuencia de cada palabra (ignorando mayúsculas/minúsculas y signos de puntuación), y muestra las palabras más repetidas.

Perfecto para practicar:  
- Lectura de archivos  
- Uso de diccionarios para conteo  
- `split()`, `lower()`, `replace()`  
- Ordenamiento de resultados

## Requisitos

- Python 3.x  
- No requiere librerías externas (solo módulos estándar: `os`, `string`)

## Instalación

1. Clona o descarga el repositorio:
   ```bash
   git clone https://github.com/camilobaezam/WordCounter.git
2. Entra al directorio: cd WordCounter

## Uso

Ejecuta el programa: python WordCounter.py
El programa te pedirá la ruta del archivo de texto que quieres analizar.

Ejemplo: 
Ingresa la ruta del archivo de texto (o 'salir' para terminar): cuentos.txt

Luego mostrará:

Total de palabras encontradas: 1245
Total de palabras únicas: 312

Las 10 palabras más frecuentes (o todas si hay menos):
--------------------------------------------------
 1. el                  → 98 veces
 2. de                  → 76 veces
 3. y                   → 65 veces
 4. la                  → 52 veces
 5. que                 → 45 veces
...

Puedes elegir cuántas palabras mostrar (presiona Enter para 10 por defecto).

## Ejemplos de archivos para probar

1. texto.txt (simple)
Este es un texto de prueba. Este texto se repite mucho texto.
Texto texto texto. Prueba prueba prueba.
2. cuentos.txt (puedes copiar un cuento corto de internet)
3. libro.txt (puedes pegar el contenido de un libro corto o capítulo)

## Características

- Ignora mayúsculas/minúsculas
- Elimina puntuación básica (.,!?;:"'()[]—)
- Muestra conteo total de palabras y palabras únicas
- Permite elegir cuántas palabras más frecuentes mostrar
- Maneja errores básicos (archivo no existe, vacío)

## Posibles mejoras futuras (ideas para extender el proyecto)

- Contar solo palabras con longitud mínima (ej: > 3 letras)
- Mostrar también las menos frecuentes
- Exportar resultados a archivo CSV
- Interfaz gráfica con tkinter
- Soporte para múltiples idiomas (stopwords)
- Gráficos de frecuencia (con matplotlib)

## Contribuciones
¡Las contribuciones son bienvenidas!
Si quieres agregar alguna funcionalidad (gráficos, exportación, filtros, etc.), abre un issue o pull request.
## Autor 
Camilo Baeza
   
