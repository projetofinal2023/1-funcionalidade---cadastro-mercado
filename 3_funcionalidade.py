from PyQt5 import uic,QtWidgets
import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_produtos"
)

def editar_dados():
    tela_editar.show()


def excluir_dados():
    linha = segunda_tela.tableWidget.currentRow()
    segunda_tela.tableWidget.removeRow(linha)

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM produtos")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("DELETE FROM produtos WHERE id="+ str(valor_id))

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
        categoria ="Informática"
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

    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")


def chama_segunda_tela():
    segunda_tela.show()


    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM produtos"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    print(dados_lidos)

    segunda_tela.tableWidget.setRowCount(len(dados_lidos))
    segunda_tela.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            segunda_tela.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
segunda_tela=uic.loadUi("listar_dados.ui")
tela_editar=uic.loadUi("menu_editar.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(chama_segunda_tela)
segunda_tela.pushButton.clicked.connect(excluir_dados)
segunda_tela.pushButton_2.clicked.connect(editar_dados)

formulario.show()
app.exec()




