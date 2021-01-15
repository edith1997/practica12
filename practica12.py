from urllib.request import urlopen  # Importamos "urlopen" para abrir una pÃ¡gina Web
from bs4 import BeautifulSoup       # Importamos "BeautifulSoup" para hacer WebScraping

# Definir e imprimir pÃ¡gina a leer
pagina_inicial = "http://sagitario.itmorelia.edu.mx/~rogelio/hola.htm"
print("\nDireccion: " + pagina_inicial)

# Cargar pagina en memoria
url = urlopen(pagina_inicial)

# Parsear la pagina usando HTML
bs = BeautifulSoup(url.read(), 'html.parser')

# Extraer e imprimir el titulo de la pagina
print("\nTitulo: " + bs.title.text + "\n")

# Extraer e imprimir la descripion de la pagina
for descripcion in bs.find_all('meta',attrs={'name':'description'}):
    print("Descripcion: {}".format(descripcion.get("content"))+"\n")

# Extraer e imprimir las keywords
for keywords in bs.find_all('meta',attrs={'name':'keywords'}):
    print("Keywords: {}".format(keywords.get("content"))+"\n")

# Extraer los enlaces de la pagina
print("\nEnlaces encontrados\n")
for enlaces in bs.find_all("a"):
    print("href: {}".format(enlaces.get("href")))
