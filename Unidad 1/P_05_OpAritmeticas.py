import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P_05_OpAritmeticas.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.operacion)
        self.btn_restar.clicked.connect(self.operacion)
        self.btn_multiplicar.clicked.connect(self.operacion)
        self.btn_dividir.clicked.connect(self.operacion)
        self.txt_resultado.setReadOnly(True)
        #self.txt_suma.setReadOnly(False)

    # Área de los Slots
    def operacion(self):
        try:
            objeto = self.sender()
            nombre = (objeto.objectName())
            print(nombre)

            a = float(self.txt_a.text())
            b = float(self.txt_b.text())

            if nombre == "btn_sumar":
                resultado = a + b
            elif nombre == "btn_restar":
                resultado = a - b
            elif nombre == "btn_multiplicar":
                resultado = a * b
            elif nombre == "btn_dividir":
                resultado = a / b



            self.txt_resultado.setText(str(resultado))
        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())