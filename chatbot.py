from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
# Crear una nueva instancia de ChatBot
chatbot = ChatBot("Jarvis")

# Crear una nueva instancia de ChatterBotCorpusTrainer y pasarle el chatbot como argumento
trainer = ChatterBotCorpusTrainer(chatbot)

# Entrenar al chatbot con el corpus de datos en español
trainer.train("chatterbot.corpus.spanish")

@app.route('/get_response', methods=['POST'])

def get_response(user_input):
    # Obtener una respuesta del chatbot
    return chatbot.get_response(user_input)

while True:
    user_input = input("Usuario: ")
    if user_input.lower() == "salir":
        break
    response = get_response(user_input)
    print("Jarvis: ", response)

if __name__ == '__main__':
    app.run(port=5000)