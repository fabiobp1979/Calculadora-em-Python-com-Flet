import flet as ft
import math
import webbrowser
pi=math.pi

resultado_exibido = False

def main(pagina:ft.Page):
    
    pagina.title="Minha Calculadora"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    caixa_texto = ft.TextField(value='0', width=270,bgcolor='gray300', color='black', text_align=ft.TextAlign.RIGHT,)
   
    def num1(e):
        global resultado_exibido
        if resultado_exibido or (caixa_texto.value == '0' and '2' != '0'):
            
            caixa_texto.value = ""
            resultado_exibido = False
        caixa_texto.value += '1'
        pagina.update()
        
    def num2(e):
        global resultado_exibido
        if resultado_exibido or (caixa_texto.value == '0' and '2' != '0'):
            caixa_texto.value = "" 
            resultado_exibido = False
        caixa_texto.value += '2'
        pagina.update()

    def num3(e):        
        global resultado_exibido
        if resultado_exibido or (caixa_texto.value == '0' and '2' != '0'):
            caixa_texto.value = "" 
            resultado_exibido = False
        caixa_texto.value += '3'
        pagina.update()

    def num4(e):
        global resultado_exibido
        if resultado_exibido or (caixa_texto.value == '0' and '2' != '0'):
            caixa_texto.value = "" 
            resultado_exibido = False
        caixa_texto.value += '4'
        pagina.update()
        
    def num5(e):
        global resultado_exibido
        if resultado_exibido or (caixa_texto.value == '0' and '2' != '0'):
            caixa_texto.value = "" 
            resultado_exibido = False
        caixa_texto.value += '5'
        pagina.update()

    def num6(e):
        global resultado_exibido
        if resultado_exibido or (caixa_texto.value == '0' and '2' != '0'):
            caixa_texto.value = "" 
            resultado_exibido = False   
        caixa_texto.value += '6'
        pagina.update()

    def num7(e):
        global resultado_exibido
        if resultado_exibido or (caixa_texto.value == '0' and '2' != '0'):
            caixa_texto.value = "" 
            resultado_exibido = False         
        caixa_texto.value += '7'
        pagina.update()

    def num8(e):
        global resultado_exibido
        if resultado_exibido or (caixa_texto.value == '0' and '2' != '0'):
            caixa_texto.value = "" 
            resultado_exibido = False        
        caixa_texto.value += '8'
        pagina.update()

    def num9(e):
        global resultado_exibido
        if resultado_exibido or (caixa_texto.value == '0' and '2' != '0'):
            caixa_texto.value = "" 
            resultado_exibido = False       
        caixa_texto.value += '9'
        pagina.update()

    def num0(e):
        global resultado_exibido
        if resultado_exibido or (caixa_texto.value == '0' and '2' != '0'):
            caixa_texto.value = "" 
            resultado_exibido = False
        caixa_texto.value += '0'
        pagina.update()
       
    def vir(e):
        global resultado_exibido
        if ',' not in caixa_texto.value:
            caixa_texto.value += ","
            resultado_exibido = False
        pagina.update()
    
    def pi1(e):
        global resultado_exibido
        if caixa_texto.value == '0' or resultado_exibido:
            caixa_texto.value = "{:.4f}".format(pi)
        else:
            caixa_texto.value += "{:.4f}".format(pi)
            
        resultado_exibido = False
        pagina.update()
    
    def varre(e):
        global resultado_exibido
        resultado_exibido = False  
        caixa_texto.value = '0'
        pagina.update()
    
    def igual_click(e):
        global resultado_exibido
        expression = caixa_texto.value.replace(",", ".")
        try:
            resultado = eval(expression)
            caixa_texto.value = str(resultado).replace(".", ",")
        except Exception as ex:
            caixa_texto.value = "Erro"
        resultado_exibido = True
        pagina.update()
    
    def adicao(e):
        global resultado_exibido
        ultimo_caractere = caixa_texto.value[-1] if caixa_texto.value else ''
        
        # Verifica se o último caractere é um operador
        if ultimo_caractere in ['+', '-', '*', '/']:
            # Se for um operador, substitui pelo novo operador
            caixa_texto.value = caixa_texto.value[:-1] + '+'
        else:
            # Se não for um operador, apenas adiciona o operador de soma
            if caixa_texto.value == '0':
                caixa_texto.value = ""
            caixa_texto.value += '+'
        
        resultado_exibido = False
        pagina.update()
    
    def sub(e):
        global resultado_exibido
        ultimo_caractere = caixa_texto.value[-1] if caixa_texto.value else ''
        
        # Verifica se o último caractere é um operador
        if ultimo_caractere in ['+', '-', '*', '/']:
            # Se for um operador, substitui pelo novo operador
            caixa_texto.value = caixa_texto.value[:-1] + '-'
        else:
            # Se não for um operador, apenas adiciona o operador de subtração
            if caixa_texto.value == '0':
                caixa_texto.value = ""
            caixa_texto.value += '-'
        
        resultado_exibido = False
        pagina.update()
    
    def multiplicacao(e):
        global resultado_exibido
        ultimo_caractere = caixa_texto.value[-1] if caixa_texto.value else ''
        
        # Verifica se o último caractere é um operador
        if ultimo_caractere in ['+', '-', '*', '/']:
            # Se for um operador, substitui pelo novo operador
            caixa_texto.value = caixa_texto.value[:-1] + '*'
        else:
            # Se não for um operador, apenas adiciona o operador de multiplicação
            if caixa_texto.value == '0':
                caixa_texto.value = ""
            caixa_texto.value += '*'
        
        resultado_exibido = False
        pagina.update()
    
    def divisao(e):
        global resultado_exibido
        ultimo_caractere = caixa_texto.value[-1] if caixa_texto.value else ''
        
        # Verifica se o último caractere é um operador
        if ultimo_caractere in ['+', '-', '*', '/']:
            # Se for um operador, substitui pelo novo operador
            caixa_texto.value = caixa_texto.value[:-1] + '/'
        else:
            # Se não for um operador, apenas adiciona o operador de divisão
            if caixa_texto.value == '0':
                caixa_texto.value = ""
            caixa_texto.value += '/'
        
        resultado_exibido = False
        pagina.update()
    
    def backspace_click(e):
        global resultado_exibido
        caixa_texto.value = caixa_texto.value[:-1]
        pagina.update()
    
    #botões
    button1 = ft.ElevatedButton(text="1", width=60, on_click=num1)
    button2 = ft.ElevatedButton(text="2", width=60, on_click=num2)
    button3 = ft.ElevatedButton(text="3", width=60, on_click=num3)
    button4 = ft.ElevatedButton(text="4", width=60, on_click=num4)
    button5 = ft.ElevatedButton(text="5", width=60, on_click=num5)
    button6 = ft.ElevatedButton(text="6", width=60, on_click=num6)
    button7 = ft.ElevatedButton(text="7", width=60, on_click=num7)
    button8 = ft.ElevatedButton(text="8", width=60, on_click=num8)
    button9 = ft.ElevatedButton(text="9", width=60, on_click=num9)
    button0 = ft.ElevatedButton(text="0", width=60, on_click=num0)
    virgula = ft.ElevatedButton(text=",", width=60, on_click=vir)
    picalc= ft.ElevatedButton(text="π", width=60, on_click=pi1)
    
    #operações
    btmais = ft.ElevatedButton(text="+", width=60,bgcolor='blue', color='white',on_click=adicao)
    btmenos = ft.ElevatedButton(text="-", width=60,bgcolor='blue', color='white',on_click=sub)
    btmultiplicacao = ft.ElevatedButton(text="x", width=60,bgcolor='blue', color='white',on_click=multiplicacao)
    btdivisa = ft.ElevatedButton(text="÷", width=60,bgcolor='blue', color='white',on_click=divisao)
    
    backspace = ft.ElevatedButton(text="←", width=60,bgcolor='blue', color='white', on_click=backspace_click)
    porcentagem = ft.ElevatedButton(text="%", width=60,bgcolor='blue', color='white')
    limpar = ft.ElevatedButton(text="C", width=60,bgcolor='blue', color='white',on_click=varre)
    igual = ft.ElevatedButton(text="=", width=60,bgcolor='blue', color='white',on_click=igual_click)
    
    # Cria uma linha com os botões
    rowcaixa = ft.Row([caixa_texto],alignment=ft.MainAxisAlignment.CENTER)
    row0 = ft.Row([limpar, backspace ,porcentagem, btdivisa],alignment=ft.MainAxisAlignment.CENTER)
    row1 = ft.Row([button1, button2,button3, btmultiplicacao],alignment=ft.MainAxisAlignment.CENTER)
    row2 = ft.Row([button4, button5,button6,btmenos],alignment=ft.MainAxisAlignment.CENTER)
    row3 = ft.Row([button7, button8,button9,btmais],alignment=ft.MainAxisAlignment.CENTER)
    row4 = ft.Row([picalc, button0,virgula,igual],alignment=ft.MainAxisAlignment.CENTER)
    
    # Adiciona a linha à página
    pagina.add(rowcaixa)
    pagina.add(row0)
    pagina.add(row1)
    pagina.add(row2)
    pagina.add(row3)
    pagina.add(row4)
  
ft.app(target=main)
