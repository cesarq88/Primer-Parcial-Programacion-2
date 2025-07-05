from abc import ABC, abstractmethod




#esta es la clase abstracta LibraryItem que define la estructura básica de un item de la library
#se defien los traibutos comunes y el metodo abstracto checkout
#las clases Book y Magazine heredan de esta clase y deben implementar el metodo checkout
class LibraryItem (ABC):
    # se inicializan los atributos title y item_id
    # title es el titulo del item y item_id es un identificador unico para cada item
    def __init__(self, title: str, item_id: int):

        #  Estas son validaciones para el title y el item_id
        if not isinstance(title, str):
            raise ValueError("El titulo debe ser una cadena de caractreres")
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("El ID del item debe ser un número entero positivo")
        
        self.title = title
        self.item_id = item_id
     # Este es el metodo abastracto que herredan las clases Book y Magazine, el arroba es solo un adorno
    @abstractmethod
    def checkout(self, user: str )-> str:
        pass
    

#Esta clase reprensenta los libros de la library y hereda : el metodo checkout de la clase LibraryItem
class Book(LibraryItem):
    #el constructor qe recive los title, item_id, author y pages
    # title es el titulo del libro, item_id es un identificador unico para cada libro   
    def __init__(self, title: str,item_id: int  ,author: str, pages: int    ):
        super().__init__(title, item_id)
        #aca  viene las validaciones para los los atrbutos title, item_id, author y pages   
        if not isinstance(title, str) or not title.strip():
            raise ValueError("El titulo debe ser una cadena de caracteres, no tiene que ser vacio ni nulo")
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("El ID del item debe ser un número entero positivo")
        if not isinstance (author, str) or not author.strip():
            raise ValueError("El autor debe ser una cadena de caracteres, no tiene que ser vacio ni nulo")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("El número de páginas debe ser un entero positivo")
        
        
        self.author = author
        self.pages = pages
     #este metodo lo u nico que hace es recivier un usuario y devu elve un strin 
    def checkout(self, user: str) -> str:
         return f"Book: {self.title}, checked out by : {user}"
    #  este metodo devuelve una representacion en string del objeto, por que me tiraba una direccion de memoria
    def __str__(self) -> str:
        return f"Book: {self.title}, Author: {self.author}, Pages: {self.pages}"
# esta clase es de las revistas de la library y hereda : el metodo checkout de la clase LibraryItem
class Magazine(LibraryItem):
    #el constructor qe recive los issue_number, title, item_id
    def __init__(self, issue_number: int, title : str, item_id: int) :
        #aca viene las validaciones para los los atrbutos issue_number, title y item_id 
        
        if not isinstance(issue_number, int) or issue_number <= 0:
            raise ValueError("El número de edición debe ser un entero positivo")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("El titulo debe ser una cadena de caracteres, no tiene que ser vacio ni nulo")
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("El ID del item debe ser un número entero positivo")
        super().__init__(title, item_id)
        
    
        
        self.issue_number = issue_number
       

    def checkout(self, user: str) -> str:
        return f"Magazine: {self.title}, Issue: {self.issue_number}, checked out by: {user}"
    def __str__(self) -> str:
        return f"Magazine: {self.title}, Issue: {self.issue_number}, ID: {self.item_id}"

def checkout_items(items: list[LibraryItem], user: str) -> list[str]:
   #esta funcion la lista de itesm y llama al metordo cheout para cada uno
   #le pasa un usuario y devuelve una lista con los mensajes de cdaa checkout
    return [item.checkout(user) for item in items]

def count_items(items: list[LibraryItem]) -> dict:
  #esta funcio lo hace es recirrrer y contar lobros y revistas estan en la lista de itesm 
  # va sumando uno de cada tipo y deuelve un diccionario con el total de libros y revistas 
    total = {"books": 0, "magazines": 0}
    for item in items:
        if isinstance(item, Book):
            total["books"] = total.get("books", 0) + 1
        elif isinstance(item, Magazine):
            total["magazines"] = total.get("magazines", 0) + 1
    return total

def find_by_title(items: list[LibraryItem], title: str) -> list[LibraryItem]:
    #ACA buscmao todo  los items que tengan el titulo que le pasamos por parametro, y tiene que coincidir con el titulo del item
    #si no hay ninguno devuelve una lista vacia
    return [item for item in items if item.title.lower() == title.lower()]




#Este bloque del if  es solo para  probar el codigo, sus funciones y clases. Y solo corre cuando se ejecuta Clases.py directamente
#si se importa Clases.py desde otro modulo, este bloque no se ejecuta
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


