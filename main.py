from anki import create_anki_cards
from pdftotext import pdftotxt


input_file = input("Ingrese el nombre del archivo PDF: ")
output_file = 'anki_cards.csv'
#print (pdftotxt(input_file))
skip_pages = input("Ingrese el número de páginas a omitir: ")
try:  
  skip_pages = int(skip_pages)
except ValueError:
  print("Ingrese un número válido")

input_content = pdftotxt(input_file, skip_pages=3)
create_anki_cards(input_content, output_file)
