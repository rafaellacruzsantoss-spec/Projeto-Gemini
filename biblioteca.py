!pip install google-genai
# Configura a API Key do Google Gemini e grava em uma variável de ambiente

import os
from google.colab import userdata

os.environ["GOOGLE_API_KEY"] = userdata.get('Gemini')

from google.colab import userdata
userdata.get('Gemini')

# Configura o cliente da SDK do Gemini

import google.generativeai as genai

MODEL_ID = "gemini-2.5-flash"

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

# Pergunta ao Gemini uma informação mais recente que seu conhecimento

from IPython.display import HTML, Markdown

model = genai.GenerativeModel(MODEL_ID)

resposta = model.generate_content(
    contents='Você é um entusiasta do livro Trono de Vidro e quer fazer um resumo sobre o livro',
)
# Exibe a resposta na tela
display(Markdown(f"Resposta:\n {resposta.text}"))
