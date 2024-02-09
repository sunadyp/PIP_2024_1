import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P_06_SumNumeros_V2.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)
        self.txt_resultado.setReadOnly(True)
        #self.txt_suma.setReadOnly(False)

    # Área de los Slots
    def sumar(self):
        # el usuario ingresará los números separados por comas
        numeros = self.txt_numeros.text() #entrada ejemplo: 5,6,7,8,9
        lista = numeros.split(",") #convierte la entrada de números en una lista. Ejemplo ['5', '6', '7', '8', '9']
        print(lista)
        lista_en_numeros = [int(i) for i in lista] #conversión de los caracteres a números, por lista de compren
        print(lista_en_numeros)

        suma = sum(lista_en_numeros)

        self.txt_resultado.setText(str(suma))

        #a = self.txt_numeros.text()
        #self.txt_resultado.setText(str(a))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())