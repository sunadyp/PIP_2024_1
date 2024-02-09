import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P_04_OpAritmeticas_ConEstilo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)
        self.btn_restar.clicked.connect(self.restar)
        self.btn_multiplicar.clicked.connect(self.multiplicar)
        self.btn_dividir.clicked.connect(self.dividir)
        self.txt_resultado.setReadOnly(True)
        #self.txt_suma.setReadOnly(False)

    # Área de los Slots
    def sumar(self):
        a = float(self.txt_a.text())
        b = float(self.txt_b.text())

        resultadoSumar = a + b

        self.txt_resultado.setText(str(resultadoSumar))

    def restar(self):
        a = float(self.txt_a.text())
        b = float(self.txt_b.text())

        resultadoRestar = a - b

        self.txt_resultado.setText(str(resultadoRestar))

    def multiplicar(self):
        a = float(self.txt_a.text())
        b = float(self.txt_b.text())

        resultadoMultplicar = a * b

        self.txt_resultado.setText(str(resultadoMultplicar))

    def dividir(self):
        a = float(self.txt_a.text())
        b = float(self.txt_b.text())

        resultadoDividir = a / b

        self.txt_resultado.setText(str(resultadoDividir))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())