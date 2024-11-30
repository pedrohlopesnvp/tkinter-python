from tkinter import*

janela = Tk ()
janela.title ("IMC")
janela.geometry("300x270")

def calcular_imc():
    peso = float(entrada1_peso.get())
    altura = float(entrada2_altura.get())
    imc = peso / (altura * altura)
    label4.configure(text = "{:.2f}".format(imc))
    definir_situacao(imc)

def definir_situacao(imc):
    if(imc < 17):
        label5.configure(text = "Muito abaixo do peso")
    elif(imc >= 17 and imc <= 18.49):
        label5.configure(text = "Abaixo do peso")
    elif(imc >= 18.5 and imc <= 24.99):
        label5.configure(text = "Peso normal")
    elif(imc >= 25 and imc <= 29.99):
        label5.configure(text = "Acima do peso")
    elif(imc >= 30 and imc <= 34.99):
        label5.configure(text = "Obesidade I")
    elif(imc >= 35 and imc <= 39.99):
        label5.configure(text = "Obesidade II (severa)")
    elif(imc >= 40):
        label5.configure(text = "Obesidade III (mórbida)")

label1 = Label (janela, text = "Digite seu Peso:")
label1.grid (column = 0, row = 0, padx = 15, pady = 15)

entrada1_peso = Entry(janela, width=10)
entrada1_peso.grid(column=1, row=0, padx=5, pady=15)

label2 = Label (janela, text = "Digite sua Altura:")
label2.grid (column = 0, row = 1, padx = 15, pady = 15)

entrada2_altura = Entry(janela, width=10)
entrada2_altura.grid(column=1, row=1, padx=5, pady=15)

botao = Button(janela, text="Calcular IMC", command = calcular_imc)
botao.grid(column = 0, row = 2, padx = 5, pady = 15)

label3 = Label (janela, text = "Seu IMC:")
label3.grid (column = 0, row = 3, padx = 15, pady = 15)

label4 = Label (janela, text = "0")
label4.grid (column = 1, row = 3, padx = 15, pady = 15)

label5 = Label (janela, text = "Situação")
label5.grid (column = 0, row = 4, padx = 15, pady = 15)

# Iniciar o loop principal da interface
janela.mainloop ()
