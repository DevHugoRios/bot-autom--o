import flet as ft
import pyautogui
import time

UTF=8

def main(app):
    app.title = "Bot de automação para LinkedIn e Instagram"
    app.vertical_alignment = ft.MainAxisAlignment.CENTER
    app.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    texto = ft.Text("Olá, Bem vindo ao aplicativo de automação", 
                    font_family='Poppins', 
                    size=40, 
                    weight=ft.FontWeight.W_900,  
                    text_align=ft.TextAlign.CENTER,
                    height=250)   
    
   # def perguntarconexoes(cnxs):
        # app.add(perguntar_conexoes)
       # app.update(app)
        #vezes = ft.TextField(value="0", text_align="right", width=100)

        #def minus_click(e):
           # vezes.value = str(int(vezes.value) - 1)
           # app.update()

       # def plus_click(e):
            #vezes.value = str(int(vezes.value) + 1)
            #app.update()
    
        #ft.Row(
         #   [
           #     ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
           #     vezes,
          #      ft.IconButton(ft.icons.ADD, on_click=plus_click),
          #  ],
          #  alignment=ft.MainAxisAlignment.CENTER,
      #  )
  #  )

    def iniciarconexao(cnx):

        texto2 = ft.Text("Iniciando a automação de conexão...")

        app.add(texto2)
        app.update(app)
        pyautogui.PAUSE = 2

        #acessar o chrome
        pyautogui.click(702,1055)
        pyautogui.write("chrome")
        pyautogui.press("enter")

        #acessar o site do LinkedIn
        time.sleep(10)
        localizaraba = pyautogui.locateCenterOnScreen("linkedinaba.png")
        pyautogui.moveTo(localizaraba, 1)

        #acessar a parte de "minha rede"
        pyautogui.click(979, 119)

        time.sleep(1)

        #acessar "ver todos"
        pyautogui.click(1586, 312)
        pyautogui.click(625, 540)

        time.sleep(1) 

        for i in range(50):
            pyautogui.press("tab", presses=3)
            pyautogui.press("enter") 

    def iniciarseguir(cnx2):          
        pyautogui.PAUSE = 1

        pyautogui.press("win")
        pyautogui.write("chrome")
        pyautogui.press("enter")

        time.sleep(5)

        pyautogui.write("www.instagram.com")
        pyautogui.press("enter")

        time.sleep(2)

        procurar = "sim"

        while procurar == "sim":
            try:
                localizar_para_seguir = pyautogui.locateCenterOnScreen("vertodas.png", confidence=0.7)
                pyautogui.click(localizar_para_seguir.x, localizar_para_seguir.y)
                procurar = "não"
            except:
                print("Não encontrado")
                time.sleep(1)
                

        time.sleep(2)
        procurar2 = "sim"

        while procurar2 == "sim":
            try:
                for i in range(20):
                    seguir = pyautogui.locateCenterOnScreen("seguirinsta.png", confidence=0.8)
                    pyautogui.click(seguir.x, seguir.y)
                    
            except:
                print("Não encontrado")
                pyautogui.scroll(-800)
                time.sleep(1)

    def pararautomacao(p):
        pyautogui.moveTo(0,0)
        pyautogui.hotkey("Ctrl-C")
        textoparar = ft.Text("Parando a automação, tire as mãos do teclado e mouse")
        app.add(textoparar)
        app.update(app)

    botao_iniciarconexao = ft.ElevatedButton("Iniciar automação de conexão",
                                             on_click= iniciarconexao,
                                             height=80, 
                                             color=ft.colors.GREEN_ACCENT)
    
    botao_iniciarseguirinsta = ft.ElevatedButton("Iniciar automação de seguir no instagram",
                                            on_click= iniciarseguir,
                                            height=80, 
                                            color=ft.colors.GREEN_ACCENT)
    
    botao_pararautomacao = ft.ElevatedButton("Parar automação", on_click=pararautomacao, 
                                             height=80, 
                                             color=ft.colors.RED_ACCENT)

    app.add(texto)
    #perguntarconexoes(print)
    app.add(botao_iniciarconexao)
    app.add(botao_iniciarseguirinsta)
    app.add(botao_pararautomacao)

 

ft.app(target=main, port=8000 )