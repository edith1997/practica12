from urllib.request import urlopen
from bs4 import BeautifulSoup

pagina_inicial = "http://sagitario.itmorelia.edu.mx/~rogelio/hola.htm"

url = urlopen(pagina_inicial)
print("\nExtraer los enlaces de la pÃ¡gina Web: " + pagina_inicial + "\n")

bs = BeautifulSoup(url.read(), 'html.parser')
for enlaces in bs.find_all("a"):
    print("href: {}".format(enlaces.get("href")))
print("\nFin de enlaces encontrados\n")