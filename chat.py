"""
# 1 Frontend ->  o que o usuário vê e interage
# 2 Backend -> lógica por trás do site
# 3 pip install flet -> no terminal - framework para vários veículos, pc, telemovel etc..

# Whatsapp Tabajara, funciona dentro de um mesmo acesso wi-fi, um tipo de WhatsApp numa rede local.

# Título Tabaszap
# Botão iniciar o chat
# Popup
    # Bem vindo ao Tabaszap
    # escreva o seu nome
    # Entrar no chat
# Chat
    # usuario entrou no chat
    # mensagens do usuário
# Campo enviar mensagem
# Botão enviar

# 3 passos:
# 1 importa o flet
# 2 cria função principal
# 3 corre a função(main)
"""
# 
import flet as ft # 1

import datetime
now = datetime.datetime.now()

def main(pagina): # 2, função que recebe a página principal do aplicativo
    titulo = ft.Text('TabasZap')

    nome_usuario = ft.TextField(label='Escreva o seu nome: ')

    chat = ft.Column()

    def enviar_mensagem_tunel(informacoes): # enviando msg passando por um 'túnel', que vai p/ todos!
         chat.controls.append(ft.Text(informacoes))
         pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) # para troca de dados

    def enviar_mensagem(evento):
        texto_campo_mensagem = (f"{now.hour}:{now.minute}:{now.second} - {nome_usuario.value}: {campo_mensagem.value}")
        # colocar nome do usuario
        #chat.controls.append(ft.Text(texto_campo_mensagem))
        pagina.pubsub.send_all(texto_campo_mensagem)
        # limpar o campo mensagem
        campo_mensagem.value = ''
        pagina.update()

    campo_mensagem = ft.TextField(label= 'Escreva sua mensagem aqui', on_submit=enviar_mensagem)

    botao_enviar = ft.ElevatedButton('Enviar', on_click = enviar_mensagem)

    def entrar_chat(evento):
        # fecha o popup
        popup.open = False 
        #tira o botão chat da terminal
        pagina.remove(botao_iniciar) 
        # cria campo de enviar mensagem
        # adicionar o chat
        pagina.add(chat)
        # campo de enviar mensagem
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
        )
        pagina.add(linha_mensagem)
        # botão de enviar mensagem
        texto = f'{nome_usuario.value} entrou no chat :)'
        pagina.pubsub.send_all(texto)
        #chat.controls.append(ft.Text(texto))
        #print(nome_usuario.value)
        pagina.update()# atualiza

    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text('Bem vindo ao Tabaszap'),
        content = nome_usuario,
        actions=[ft.ElevatedButton('Entrar', on_click=entrar_chat)]
        )

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update() # atualiza a página

        #print('Iniciar o chat')

    botao_iniciar = ft.ElevatedButton('Iniciar chat', on_click=iniciar_chat)

    pagina.add(titulo) # o add vai adicionando tudo à página
    pagina.add(botao_iniciar)

#ft.app(main)# view para aplicativo, default # 3 o app começa na função main
ft.app(main, view=ft.WEB_BROWSER) # view para site


