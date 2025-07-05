import unittest 
import csv
import os 
from Clases import Book, Magazine, LibraryItem
from CSV_library import load_library_items

class TestBook(unittest.TestCase):

    
    
    #este metodo testea la inicializacion de la clase Book
    def test_book_initialization(self):
        libro = Book("Artificial", 1, "Santiago Bilinkis", 284)

        self.assertEqual(libro.title, "Artificial")
        self.assertEqual(libro.item_id, 1)
        self.assertEqual(libro.author, "Santiago Bilinkis")
        self.assertEqual(libro.pages, 284) 

    #aca pru ebo que si tira  error si  el titulo no es string
    def test_book_init_invalido_title(self):
        with self.assertRaises(ValueError):
            Book(123, 1, "Santiago Bilinkis", 284)
    #este metodo prueba si tira error si el item_id es negativo
    def test_book_init_invalido_item_id(self):
        with self.assertRaises(ValueError):
            Book("Artificial", -1, "Santiago Bilinkis", 284)
    #este metodo es para probar si tira error si el autor esta vacio
    def test_book_init_invalido_author(self):
        with self.assertRaises(ValueError):
            Book("Artificial", 1, "", 284)

    def test_book_init_invalido_pages(self):
        with self.assertRaises(ValueError):
            Book("Artificial", 1, "Santiago Bilinkis", -10)

    def test_book_checkout(self):
        libro = Book("Artificial", 1, "Santiago Bilinkis", 284)
        impresion_por_pantalla = libro.checkout("Juan")
        self.assertEqual(impresion_por_pantalla, "Book: Artificial, checked out by : Juan")
####################################################################################
     #aca empezamos con las pruebas de la clase Magazine
     #exactament lo mismo que  la clase book, pero con los tributos de la clase magazine
    def test_Magazine_init(self):
        revista = Magazine(2033, "Nature", 2)

        self.assertEqual(revista.issue_number, 2033)
        self.assertEqual(revista.title, "Nature")
        self.assertEqual(revista.item_id, 2)

    def test_magazine_init_invalido_issue_number(self):
        with self.assertRaises(ValueError):
            Magazine(-1, "Nature", 2)
    def test_magazine_init_invalido_title(self):
        with self.assertRaises(ValueError):
            Magazine(2033, 123, 2) 
    def test_magazine_init_invalido_item_id(self):
        with self.assertRaises(ValueError):
            Magazine(2033, "Nature", -1)

    def test_magazine_checkout(self):
        revista = Magazine(2033, "Nature", 2)
        impresion_por_pantalla = revista.checkout("Maria")
        self.assertEqual(impresion_por_pantalla, "Magazine: Nature, Issue: 2033, checked out by: Maria")

    

    # Este es progrtam que nos paso por el aula , y se lo modifico para que funcione con las clases Book y Magazine
    def test_load_libreria_from_csv(self):
    # Crear un CSV temporal
        fname = 'temp_library.csv'
        lines = [
            ['book','Artificial','1','Santiago Bilinkis','145'],
            ['magazine','2','Telenisima','244'],
            ['book','-1'],         # inválido
            ['magazine','4'],       # inválido: falta parámetro
            ['book', '5'],         # inválido
            [],                       # vacía
            ['magazine','4','Formula 1','1']  # válido
        ]
        with open(fname, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(lines)

        libreria = load_library_items(fname)

        # 1) Compruebo el número total de libreria
        self.assertEqual(len(libreria), 3)

        # 2) Extraigo libros y revistas
        # Utilizo isinstance para filtrar los objetos de tipo Book y Magazine
        libros     = [s for s in libreria if isinstance(s, Book)]
        revistas   = [s for s in libreria if isinstance(s, Magazine)]

    
        self.assertEqual(len(libros), 1)
        self.assertEqual(libros[0].title, "Artificial")
        self.assertEqual(libros[0].author, "Santiago Bilinkis")
        self.assertEqual(libros[0].pages, 145)

   #     3) Compruebo que las revistas tienen el número de edición correcto
        dims = [(r.issue_number, r.title, r.item_id) for r in revistas]
        # Debe contener (2,"Telenisima", 244) y (4,"Formula 1", 1), en cualquier orden
        self.assertCountEqual(dims, [(2,"Telenisima", 244), (4,"Formula 1", 1)])

        os.remove(fname)
 # este bloque if es para correr las pruebas unitarias cuando se ejecuta este archivo directamente
# si se importa este archivo desde otro modulo, este bloque no se ejecuta       
if __name__ == '__main__':
    unittest.main()        