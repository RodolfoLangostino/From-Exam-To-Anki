from anki import create_anki_cards
from pdftotext import pdftotxt


def main():
    # Change the name of the PDF file to the name of your PDF file
    #        "EXAMEN VIRO SIA.pdf
    input_file = "EXAMEN VIRO SIA.pdf"
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

    valid_delimiters = {'.', '-', ')'}
    while True:
        print ("Insert the delimiter between the number or options ")
        delimeter = input("(default: autodetector, recommended: '.', '-', ')'): ")
        if delimeter == "" or delimeter in valid_delimiters:
            break
        print("Invalid input. Please enter a valid delimiter (e.g., '.', '-', ')').")

    input_content = pdftotxt(input_file, skip_pages)
    create_anki_cards(input_content, output_file, delimeter)



if __name__ == "__main__":
    main()


# Example usage:
text = """
1. Pregunta uno
1. Opción uno
2. Opción dos
3. Opción tres
4. Opción cuatro

2- Pregunta dos
1- Opción uno
2- Opción dos
3- Opción tres
4- Opción cuatro

3. Pregunta tres
a. Opción uno
b. Opción dos
c. Opción tres
d. Opción cuatro

4- Pregunta cuatro
a- Opción uno
b- Opción dos
c- Opción tres
d- Opción cuatro
"""