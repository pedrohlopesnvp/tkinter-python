from tkinter import*
import mysql.connector

janela = Tk ()
janela.title ("Controle de veículos - DETRAN")
janela.geometry('800x450')

# Função para criar o BD
def criar_tabela():
    conexao = mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="detran")
    
    cursor = conexao.cursor()
    conexao.commit()
    conexao.close()

# Função para adicionar um novo veiculo
def adicionar_veiculo():

    placa = str(entrada1_placa.get())
    veiculo = str(entrada2_veiculo.get())
    marca = str(entrada3_marca.get())
    cor = str(entrada4_cor.get())
    ano = int(entrada5_ano.get())
    valor = float(entrada6_valor.get())
    opcionais = str(entrada7_opcionais.get())
    proprietario = str(entrada8_proprietario.get())
    fone = str(entrada9_fone.get())

    conexao = mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="detran")
    cursor = conexao.cursor()

    sql = "INSERT INTO veiculos (placa, veiculo, marca, cor, ano, valor, opcionais, proprietario, fone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (placa, veiculo, marca, cor, ano, valor, opcionais, proprietario, fone)
    cursor.execute(sql, val)

    conexao.commit()
    conexao.close()

# Função para listar os veiculos
def listar_veiculos():
    conexao = mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="detran")
    cursor = conexao.cursor()

    sql = "SELECT * FROM veiculos"
    cursor.execute(sql)

    # Recuperar todos os registros
    veiculos = cursor.fetchall()
    for row in veiculos:
        print(row)

    conexao.close()

# Função para atualizar um veiculo
def atualizar_veiculo():

    placa = str(entrada1_placa.get())
    veiculo = str(entrada2_veiculo.get())
    marca = str(entrada3_marca.get())
    cor = str(entrada4_cor.get())
    ano = int(entrada5_ano.get())
    valor = float(entrada6_valor.get())
    opcionais = str(entrada7_opcionais.get())
    proprietario = str(entrada8_proprietario.get())
    fone = str(entrada9_fone.get())

    conexao = mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="detran")
    cursor = conexao.cursor()

    sql = "UPDATE veiculos SET veiculo=%s, marca=%s, cor=%s, ano=%s, valor=%s, opcionais=%s, proprietario=%s, fone=%s  WHERE placa = %s"
    val = (veiculo, marca, cor, ano, valor, opcionais, proprietario, fone, placa)

    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()

# Função para deletar um veiculo
def deletar_veiculo():
    
    placa = str(entrada1_placa.get())

    conexao = mysql.connector.connect(
        port=3307,
        host="localhost",
        user="root",
        password="",
        database="detran")
    cursor = conexao.cursor()

    sql = "DELETE FROM veiculos WHERE placa = %s"
    val = (placa,)

    cursor.execute(sql, val)
    conexao.commit()
    conexao.close()


label1_placa = Label (janela, text = "Digite a placa do veículo:")
label1_placa.grid (column = 0, row = 0, padx = 15, pady = 10, sticky='w')

entrada1_placa = Entry(janela, width=10)
entrada1_placa.grid(column=1, row=0, padx=5, pady = 10, sticky='w')

label2_veiculo = Label (janela, text = "Digite o nome do veículo:")
label2_veiculo.grid (column = 0, row = 1, padx = 15, pady = 10, sticky='w')

entrada2_veiculo = Entry(janela, width=40)
entrada2_veiculo.grid(column=1, row=1, padx=5, pady = 10, sticky='w')

label3_marca = Label (janela, text = "Digite a marca do veículo:")
label3_marca.grid (column = 0, row = 2, padx = 15, pady = 10, sticky='w')

entrada3_marca = Entry(janela, width=25)
entrada3_marca.grid(column=1, row=2, padx=5, pady = 10, sticky='w')

label4_cor = Label (janela, text = "Digite a cor do veículo:")
label4_cor.grid (column = 0, row = 3, padx = 15, pady = 10, sticky='w')

entrada4_cor = Entry(janela, width=25)
entrada4_cor.grid(column=1, row=3, padx=5, pady = 10, sticky='w')

label5_ano = Label (janela, text = "Digite o ano do veículo:")
label5_ano.grid (column = 0, row = 4, padx = 15, pady = 10, sticky='w')

entrada5_ano = Entry(janela, width=10)
entrada5_ano.grid(column=1, row=4, padx=5, pady = 10, sticky='w')

label6_valor = Label (janela, text = "Digite o valor do veículo:")
label6_valor.grid (column = 0, row = 5, padx = 15, pady = 10, sticky='w')

entrada6_valor = Entry(janela, width=15)
entrada6_valor.grid(column=1, row=5, padx=5, pady = 10, sticky='w')

label7_opcionais = Label (janela, text = "Digite uma descrição:")
label7_opcionais.grid (column = 0, row = 6, padx = 15, pady = 10, sticky='w')

entrada7_opcionais = Entry(janela, width=50)
entrada7_opcionais.grid(column=1, row=6, padx=5, pady = 10, sticky='w')

label8_proprietario = Label (janela, text = "Digite o proprietário:")
label8_proprietario.grid (column = 0, row = 7, padx = 15, pady = 10, sticky='w')

entrada8_proprietario = Entry(janela, width=50)
entrada8_proprietario.grid(column=1, row=7, padx=5, pady = 10, sticky='w')

label9_fone = Label (janela, text = "Digite o telefone do proprietário:")
label9_fone.grid (column = 0, row = 8, padx = 10, pady = 10, sticky='w')

entrada9_fone = Entry(janela, width=20)
entrada9_fone.grid(column=1, row=8, padx=5, pady = 10, sticky='w')


botao_adicionar = Button(janela, text="Adicionar", command = adicionar_veiculo, bg="green")
botao_adicionar.grid(column = 1, row = 9, padx = 5, pady = 20, sticky='w')

botao_listar = Button(janela, text="Listar", command = listar_veiculos, bg="blue")
botao_listar.grid(column = 1, row = 9, padx = 75, pady = 20, sticky='w')

botao_atualizar = Button(janela, text="Atualizar", command = atualizar_veiculo, bg="yellow")
botao_atualizar.grid(column = 1, row = 9, padx = 120, pady = 20, sticky='w')

botao_deletar = Button(janela, text="Deletar", command = deletar_veiculo, bg="red")
botao_deletar.grid(column = 1, row = 9, padx = 180, pady = 20, sticky='w')


label10_retorno = Label (janela, text = "Retorno...")
label10_retorno.grid (column = 3, row = 0, padx = 10, pady = 10, sticky='w')

janela.mainloop ()