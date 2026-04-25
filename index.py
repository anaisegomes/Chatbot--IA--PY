import os

from dotenv import load_dotenv
from google import genai

# ignore

load_dotenv()

cliente = genai.Client()

api_key = os.getenv("GEMINI_APY_KEY")

print("ChatBot iniciando....(Digite 'sair' para encerrar) ===")

while True:
    pergunta = ("Digite algo: ")

    if pergunta.lower() == 'sair':
        print("Bot: Até a próxima!")
        break
    try:
            
        resposta = cliente.models.generate_content(
            model = "gemini-2.5-flash",
            contents=pergunta
            )

        print(resposta.text)
    except Exception as e:
        print(f"Erro ao conectcar a API{e}")
