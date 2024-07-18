from anki import create_anki_cards
from pdftotext import pdftotxt

def main():
  # Change the name of the PDF file to the name of your PDF file
  input_file = "Example.pdf"
  output_file = 'anki_cards.csv'

  while True:
      skip_pages = input("Insert the number of pages that you want to skip (default: 3): ")
      if skip_pages == "":
        skip_pages = 3
      try:
          skip_pages = int(skip_pages)
          break
      except ValueError:
          print("Invalid input. Please enter a valid number.")

  if skip_pages == "":
      skip_pages = 3

  input_content = pdftotxt(input_file, skip_pages)
  create_anki_cards(input_content, output_file)

if __name__ == "__main__":
  main()
