import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

# Carga el modelo de lenguaje y el tokenizador
model_name = "bert-base-uncased"
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Define una función para responder preguntas tipo test
def responder_pregunta(pregunta, contexto):
    # Tokeniza la pregunta y el contexto
    inputs = tokenizer(pregunta, contexto, return_tensors="pt")

    # Realiza la inferencia con el modelo
    outputs = model(**inputs)

    # Devuelve la respuesta
    return tokenizer.decode(torch.argmax(outputs.start_logits) + inputs["input_ids"][0])

# Define una pregunta y un contexto
pregunta = "¿Cuál es la capital de Francia?"
contexto = "Francia es un país ubicado en Europa Occidental. Su capital es París."

# Obtén la respuesta
respuesta = responder_pregunta(pregunta, contexto)

print(f"Respuesta: {respuesta}")