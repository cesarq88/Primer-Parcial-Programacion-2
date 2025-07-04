import os
import csv
from unittest import TestCase
from Clases import Book, Magazine, LibraryItem


def test_load_libreria_from_csv(self):
    # Crear un CSV temporal
    fname = 'temp_library.csv'
    lines = [
        ['book','Artificial','1','Santigo Bilinkis','145'],
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
    libreria = load_libreria_from_csv(fname)

    # 1) Compruebo el número total de libreria
    self.assertEqual(len(libreria), 3)

    # 2) Extraigo círculos y rectángulos
    libros     = [s for s in libreria if isinstance(s, Book)]
    revistas   = [s for s in libreria if isinstance(s, Magazine)]

   
    self.assertEqual(len(libros), 1)
    self.assertEqual(libros[0].title, "Artificial")
    self.assertEqual(libros[0].author, "Santiago Bilinkis")
    self.assertEqual(libros[0].pages, 145)

   # 3) Compruebo que las revistas tienen el número de edición correcto
    dims = [(r.issue_number, r.title, r.item_id) for r in revistas]
    # Debe contener (2,3) y (3,4), en cualquier orden
    self.assertCountEqual(dims, [(2.0,"Telenisima", 244)])

    os.remove(fname)