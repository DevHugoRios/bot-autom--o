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
        pyautogui.press("win")
        pyautogui.write("chrome")
        pyautogui.press("enter")

        #achar conta google
        try:
            iconeperfilaleatorio = pyautogui.locateCenterOnScreen("iconeperfilaleatorio.png", confidence=0.8)
            pyautogui.click(iconeperfilaleatorio.x, iconeperfilaleatorio.y)
        except:
            print("icone perfil não encontrado")
        
        time.sleep(4) 

        try:
            iconeperfilgoogle = pyautogui.locateCenterOnScreen("iconeperfilgoogle.png", confidence=0.7)
            pyautogui.click(iconeperfilgoogle.x, iconeperfilgoogle.y)
        except:
            print("icone perfil google não encontrado")
                                      
        #acessar o site do LinkedIn
        time.sleep(6)
        pyautogui.write("www.linkedin.com")
        pyautogui.press("enter")
        time.sleep(2)
        localizaraba = pyautogui.locateCenterOnScreen("linkedinaba.png")
        pyautogui.moveTo(localizaraba, 1)
       
        #acessar a parte de "minha rede"
        entrar1 = "sim"
        
        while entrar1 == "sim":
            try:
                entrarrede = pyautogui.locateCenterOnScreen("minharede.png", confidence= 0.7)
                pyautogui.click(entrarrede.x, entrarrede.y)
                entrar1 = "não"
            except:
                print("icone minha rede não encontrado")
                time.sleep(1)

        #acessar "ver todos"
        entrar2 = "sim"
        while entrar2 == "sim":
            try:
                acessar_vertodos = pyautogui.locateCenterOnScreen("vertodos.png", confidence=0.8)
                pyautogui.click(acessar_vertodos.x,acessar_vertodos.y)
                entrar2 = "não"
            except:
                print("icone ver todos não encontrado ")
                time.sleep(1) 

        conectar = "sim"
        while conectar == "sim":
            try:
                clicarconectar = pyautogui.locateCenterOnScreen("conectarbotao.png", confidence=0.7)
                pyautogui.click(clicarconectar.x, clicarconectar.y)
                conectar = "não"
            except:
                print("icone conectar não encontrado")
                time.sleep(1)

        for i in range(30):
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