
# Importando a biblioteca tkinter
from tkinter import *
from tkinter import ttk

# Definindo cores
color1 = "#43464d" # dark grey
color2 = "#e0a941" # orange
color3 = "#f7f7f7" # white
color4 = "#1430ff" # blue


# Criando janela usando tkinter
window = Tk()
window.title("Calculadora")
window.geometry("235x310")
# window.config(bg=color1)

# Criando frame do display para visualizador
frame_display = Frame(window, width=235, height=50, bg=color1)
frame_display.grid(row=0, column=0)

# Criando frame para os botões
frame_body = Frame(window, width=235,height=268,)
frame_body.grid(row=1, column=0)


# iniciação da lógica da calculadora


result = 0.0

# Variável todos os valores

allValues = ''



# Criação das labels

textValue = StringVar()


# Criando função

def setValues(event):

    global allValues
    allValues = allValues + str(event)

    # Passando valor para o display

    textValue.set(allValues)


# Função para limpar o ultimo número ( não aplicada )
def clearLastNum():
    global allValues
    newValues = len(allValues) - 1
    allValues = allValues[0:newValues]
    textValue.set(allValues)

# Função para armazenar a str dos valores
    
    
def calcular():
       
  global allValues
  allValues = allValues.replace('x', '*')
  allValues = allValues.replace('÷', '/')
    
  
  result = eval(allValues)
  textValue.set(str(result))
  allValues = (str(result))
  print(result)
  

# Função para apagar a tela (c)

def clearDisplay():
      global allValues
      allValues = ''
      textValue.set('')


# textvariable (Pode alterar valores variáveis)
app_label = Label(frame_display, textvariable=textValue , width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=color1, fg=color3)
app_label.place(x=0, y=0)



# Criando os botões da calculadora
b1 = Button(frame_body, command = clearDisplay, text="C", width=11, height=2, bg=color3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x= 0, y= 0)

b2 = Button(frame_body, command = lambda: setValues('%') ,text="%", width=5, height=2, bg=color3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x= 118, y= 0)

b3 = Button(frame_body, command = lambda: setValues('÷') ,text="÷", width=5, height=2, bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x= 177, y= 0)

b4 = Button(frame_body, command = lambda: setValues('7') ,text="7", width=5, height=2, bg=color3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x= 0, y= 52)

b5 = Button(frame_body, command = lambda: setValues('8') ,text="8", width=5, height=2, bg=color3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x= 59, y= 52)

b6 = Button(frame_body,command = lambda: setValues('9') , text="9", width=5, height=2, bg=color3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x= 118, y= 52)

b7 = Button(frame_body, command = lambda: setValues('x') ,text="x", width=5, height=2, bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x= 177, y= 52)

b8 = Button(frame_body, command = lambda: setValues('4') ,text="4", width=5, height=2, bg=color3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x= 0, y= 104)

b9 = Button(frame_body,command = lambda: setValues('5') , text="5", width=5, height=2, bg=color3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x= 59, y= 104)

b10 = Button(frame_body, command = lambda: setValues('6') ,text="6", width=5, height=2, bg=color3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b10.place(x= 118, y= 104)

b11 = Button(frame_body,command = lambda: setValues('+') , text="+", width=5, height=2, bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b11.place(x= 177, y= 104)

b12 = Button(frame_body, command = lambda: setValues('1') ,text="1", width=5, height=2, bg=color3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b12.place(x= 0, y= 156)

b13 = Button(frame_body,command = lambda: setValues('2') , text="2", width=5, height=2, bg=color3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b13.place(x= 59, y= 156)

b14 = Button(frame_body,command = lambda: setValues('3') , text="3", width=5, height=2, bg=color3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b14.place(x= 118, y= 156)

b15 = Button(frame_body,command = lambda: setValues('-') , text="-", width=5, height=2, bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x= 177, y= 156)

b16 = Button(frame_body,command = lambda: setValues('0') , text="0", width=11, height=2, bg=color3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b16.place(x= 0, y= 208)

b17 = Button(frame_body,command = lambda: setValues('.') , text=".", width=5, height=2, bg=color3, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b17.place(x= 118, y= 208)

b18 = Button(frame_body,command = calcular , text="=", width=5, height=2, bg=color2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b18.place(x= 177, y= 208)









window.mainloop()