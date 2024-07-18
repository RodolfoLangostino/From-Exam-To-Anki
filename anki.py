import csv
import os
import re

def classify_questions_options(text):
    lines = text.split('\n')
    questions = []
    options = []
    current_question = ""
    current_options = []
    question_number = 0

    for line in lines:
        line = line.strip()
        if re.match(r'^\d+\.', line):
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
    return questions, options

def create_anki_cards(pdf_content, output_file):
    reslist = []
    preguntas, opciones = classify_questions_options(pdf_content)
    if len(preguntas) > 4:
        for i in range(len(preguntas)):
            print (f"\n{preguntas[i]}")
            for j, opcion in enumerate(opciones[i], 1):
                print(f" {j}. {opcion}")
            respuesta_correcta = input("\nInsert the number of the answer (1 -4) or 'S' to save and shut down.")
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
        print(f"Las tarjetas de Anki se han generado en '{output_file}'")
    else:
        print("An error has occurred: The response list is empty")