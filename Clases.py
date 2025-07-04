from abc import ABC, abstractmethod

class LibraryItem (ABC):
    def __init__(self, title: str, item_id: int):
        if not isinstance(title, str):
            raise ValueError("El titulo debe ser una cadena de caractreres")
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("El ID del item debe ser un número entero positivo")
        
        self.title = title
        self.item_id = item_id

    @abstractmethod
    def checkout(self, user: str )-> str:
        pass



class Book(LibraryItem):
    def __init__(self, title: str,item_id: int  ,author: str, pages: int    ):
        super().__init__(title, item_id)   
        if not isinstance(title, str) or not title.strip():
            raise ValueError("El titulo debe ser una cadena de caracteres, no tiene que ser vacio ni nulo")
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("El ID del item debe ser un número entero positivo")
        if not isinstance (author, str) or not author.strip():
            raise ValueError("El autor debe ser una cadena de caracteres, no tiene que ser vacio ni nulo")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("El número de páginas debe ser un entero positivo")
        
        self.title = title
        self.author = author
        self.pages = pages

    def checkout(self, user: str) -> str:
         return f"Book: {self.title}, checked out by : {user}"
    def __str__(self) -> str:
        return f"Book: {self.title}, Author: {self.author}, Pages: {self.pages}"

class Magazine(LibraryItem):
    def __init__(self, issue_number: int, title : str, item_id: int) :
        if not isinstance(issue_number, int) or issue_number <= 0:
            raise ValueError("El número de edición debe ser un entero positivo")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("El titulo debe ser una cadena de caracteres, no tiene que ser vacio ni nulo")
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("El ID del item debe ser un número entero positivo")
        super().__init__(title, item_id)
        
    
        
        self.issue_number = issue_number
        self.title = title
        self.item_id = item_id

    def checkout(self, user: str) -> str:
        return f"Magazine: {self.title}, Issue: {self.issue_number}, checked out by: {user}"
    def __str__(self) -> str:
        return f"Magazine: {self.title}, Issue: {self.issue_number}, ID: {self.item_id}"

def checkout_items(items: list[LibraryItem], user: str) -> list[str]:
    """
    Realiza el checkout de una lista de items de la library.
    
    :param items: Lista de objetos LibraryItem a ser procesados.
    :param user: Nombre del usuario que realiza el checkout.
    :return: Lista de mensajes de checkout para cada item.
    """
    return [item.checkout(user) for item in items]

def count_items(items: list[LibraryItem]) -> dict:
    """
    Este cuenta la cantidad de libros y revistas en una lista de items de la library.
    
    :param items: Lista de objetos LibraryItem a ser procesados.
    :return: Diccionario con la cantidad de libros y revistas.
    """
    total = {"books": 0, "magazines": 0}
    for item in items:
        if isinstance(item, Book):
            total["books"] = total.get("books", 0) + 1
        elif isinstance(item, Magazine):
            total["magazines"] = total.get("magazines", 0) + 1
    return total

def find_by_title(items: list[LibraryItem], title: str) -> list[LibraryItem]:
    """
    Busca items por título en una lista de items de la library.
    
    :param items: Lista de objetos LibraryItem a ser procesados.
    :param title: Título a buscar.
    :return: Lista de items que coinciden con el título.
    """
    return [item for item in items if item.title.lower() == title.lower()]





if __name__ == "__main__":
    #hacemos una prueba del metodo checkout_items
    libros = [Book("Artificial", 1, "Santiago Bilinkis", 284)]
    revistas = [Magazine(2033, "Nature", 2)]
    items = libros + revistas
    user = "jon doe"
    mensajes = checkout_items(items, user)
    for mensaje in mensajes:
        print(mensaje)

    print (count_items(items))

libros_encontrados = find_by_title(items, "Artificial")
for item in libros_encontrados:
    print(item)


revistas_encontradas = find_by_title(items, "Nature")
for item in revistas_encontradas:
    print(item)


