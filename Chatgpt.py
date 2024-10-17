import openai

chaveapi = "sua chave api"

openai.api_key = chaveapi


def enviar_mensagens(mensagem, lista_mensagens=[]):
    lista_mensagens.append({"role": "user", "content": mensagem})
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=lista_mensagens
    )
    return resposta["choices"][0]["message"]


lista_mensagens = []
while True:
    txt = input("Escreva aqui sua mensagem: ")
    if txt == "sair":
        break
    else:
        resposta = enviar_mensagens(txt, lista_mensagens)
        lista_mensagens.append(resposta)
        print("ChatGPT:", resposta["content"])
