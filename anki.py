import csv
import re

def count_characters(text):
    points = len(re.findall(r'\.', text))
    hyphens = len(re.findall(r'-', text))
    parenth = len(re.findall(r'\)', text))

    # Comparar las frecuencias de los caracteres
    if points > hyphens and points > parenth:
        return "."
    elif hyphens > points and hyphens > parenth:
        return "-"
    elif parenth > points and parenth > hyphens:
        return ")"
    else:
        return "."

def count_options(text):
    lines = text.split('\n')
    first = [line[0] for line in lines if line]
    first_chars_str = ''.join(first)
    numbers = len(re.findall(r'[1-4]', first_chars_str))
    letters = len(re.findall(r'[a-d]', first_chars_str))
    uppletters = len(re.findall(r'[A-D]', first_chars_str))

    # Comparar las frecuencias de los caracteres
    if numbers > letters and numbers > uppletters:
        return r'^\d+\.'
    elif letters > numbers and letters > uppletters:
        return r'^[a-d]\)'
    elif uppletters > numbers and uppletters > letters:
        return  r'^[A-D]\)'
    else:
        print ("There was an error detecting the options")

def classify_questions_options(text,delimeter):
    lines = text.split('\n')
    questions = []
    options = []
    current_question = ""
    current_options = []
    question_number = 0
    if delimeter == "":
        delimeter = count_characters(text)  # Use the count_characters result to set the delimiter
    rema = count_options(text)
    pattern = r'^\d+[' + re.escape(delimeter) + r']'

    for line in lines:
        line = line.strip()
        if re.match(rema, line):
            num_end = line.find(".")
            num = int(line[:num_end])
            if num > question_number:
                if current_question and len(current_options) == 4:
                    questions.append(current_question)
                    options.append(current_options)
                current_question = line[num_end+1:].strip()
                current_options = []
                question_number = num
            elif 1 <= num <= 4:
                current_options.append(line[num_end+1:].strip())
        elif line == "":
            continue
        else:
            if current_question and not current_options:
                current_question += " " + line
            elif current_options:
                current_options[-1] += " " + line

    if current_question and len(current_options) == 4:
        questions.append(current_question)
        options.append(current_options)

    else:
        print ("There was an error reading the file. ", current_question, current_options)

    if not questions and not options:
        print ("There was not questions either options")
    elif not questions or not options:
        print (f"The last question was {current_question}")

    return questions, options

def create_anki_cards(pdf_content, output_file, delimeter):
    reslist = []
    preguntas, opciones = classify_questions_options(pdf_content, delimeter)
    if len(preguntas) > 4:
        for i in range(len(preguntas)):
            print (f"\n{preguntas[i]}")
            for j, opcion in enumerate(opciones[i], 1):
                print(f" {j}. {opcion}")
            respuesta_correcta = input("\nInsert the number of the answer (1 -4) or 'S' to shut down. ")
            if respuesta_correcta.upper() == "S":
                print("Shutting down...")
                break
            if respuesta_correcta.isdigit() and 1 <= int(respuesta_correcta) <= 4:
                try:
                    respuesta_correcta = int(respuesta_correcta)
                    reslist.append(str(respuesta_correcta))
                except ValueError:
                    print("Respuesta inválida. Ingrese un número entre 1 y 4.\n")

    if len(reslist) > 0:
        with open(output_file, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            for i in range(len(reslist)):
                pregunta = preguntas[i]
                opciones_str = "\n".join([f"{j+1}. {opcion}" for j, opcion in enumerate(opciones[i])])
                contenido = f"{pregunta}\n{opciones_str}"
                writer.writerow([contenido, reslist[i]])
        print(f"The cards of Anki are done on' {output_file}'")
    else:
        print(f"An error has occurred. Reslist: {reslist}")
        print (f"Questions: {preguntas}, Options: {opciones}")