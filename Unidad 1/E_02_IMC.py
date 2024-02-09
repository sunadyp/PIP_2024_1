import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "E_02_IMC.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_calcular.clicked.connect(self.calcularIMC)

    # Área de los Slots
    def calcularIMC(self):
        peso = float(self.txt_peso.text())
        altura = float(self.txt_altura.text())

        imc = peso / (altura * altura)
        cadena = "Tu IMC es: " + str(imc)

        msj = QtWidgets.QMessageBox()
        msj.setText(cadena)
        msj.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())