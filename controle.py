from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_produtos"
)


def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    categoria = ""


    if formulario.radioButton.isChecked() :
        print("Categoria Alimenticios foi selecionado")
        categoria ="Alimenticios" 
    elif formulario.radioButton_2.isChecked() :
        print("Categoria Utensilios foi selecionado")
        categoria ="Utensilios"
    elif formulario.radioButton_4.isChecked() :
        print("Categoria informática foi selecionado")
        categoria ="informática"
    elif formulario.radioButton_5.isChecked() :
        print("Categoria Eletrodomesticos foi selecionado")
        categoria ="Eletrodomesticos"
    elif formulario.radioButton_6.isChecked() :
        print("Categoria Limpeza foi selecionado")
        categoria ="Limpeza"
    else :
        print("Categoria Verduras foi selecionado")
        categoria ="Verduras"


    print("Código do Produto",linha1)
    print("Descrição",linha2)
    print("Preço",linha3)
    
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO produtos (codigo_do_produto,descricao,preco,categoria) VALUES (%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),categoria)
    cursor.execute(comando_SQL,dados)
    banco.commit()





app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
