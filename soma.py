from tkinter import*

janela = Tk ()
janela.title ("Soma")
janela.geometry('270x250')

label1 = Label (janela, text = "Primeiro número:")
label1.grid (column = 0, row = 0, padx = 15, pady = 15)

label2 = Label (janela, text = "Segundo número:")
label2.grid (column = 0, row = 1, padx = 15, pady = 15)

label3 = Label (janela, text = "Resultado:")
label3.grid (column = 0, row = 3, padx = 15, pady = 15)

label4 = Label (janela, text = "0") #Resutlado
label4.grid (column = 1, row = 3, padx = 15, pady = 15)

entrada1 = Entry(janela, width=10) # Entrada do 1° número
entrada1.grid(column=1, row=0, padx=5, pady=15)
entrada2 = Entry(janela, width=10) # Entrada do 2° número
entrada2.grid(column=1, row=1, padx=5, pady=15)

def somar():
    a = int(entrada1.get())
    b = int(entrada2.get())
    soma = a + b
    label4.configure(text = str(soma))

botao = Button(janela, text="Soma", command = somar)
botao.grid(column = 0, row = 2, padx = 5, pady = 15)

# Iniciar o loop principal da interface
janela.mainloop ()