import csv 
from Clases import Book, Magazine, LibraryItem

archivo_entrada = 'library.csv'
archivo_salida = 'library_salida.csv'



def load_library_items(path: str) -> list[LibraryItem]: 
    resultados = []
    with open(path, 'r', encoding="utf-8-sig", newline="") as csvfile:
        lector = csv.reader(csvfile) 
        for fila in lector: 
            if not fila: 
                continue
            
            tipo = fila[0].strip().lower()
            try:
                if tipo == 'book':
                    if len(fila) < 5:
                        raise ValueError("Faltan datos para el libro")
                        continue
                    titulo = fila[1].strip()
                    
                    item_id = int(fila[2].strip())
                    autor = fila[3].strip()
                    paginas = int(fila[4].strip())
                    libro = Book(titulo, item_id, autor, paginas)
                    resultados.append(libro)
                
                elif  tipo == 'magazine':
                    if len(fila) < 4:
                        raise ValueError("Faltan datos para la revista")
                        continue
                    numero_edicion = int(fila[1].strip())
                    titulo = fila[2].strip()
                    item_id = int(fila[3].strip())

                    revista = Magazine(numero_edicion, titulo, item_id)
                    resultados.append(revista)
            except ValueError as error:
                print(f"Error al procesar la fila {fila}: {error}")
    return resultados
            
                
items= load_library_items('library.csv')
for item in items:
    print(item.checkout("Persona X"))