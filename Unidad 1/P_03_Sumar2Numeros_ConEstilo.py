import sys
from PyQt5 import uic, QtWidgets

qtCreatorFile = "P_03_Sumar2Numeros_ConEstilo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_sumar.clicked.connect(self.sumar)
        self.txt_suma.setReadOnly(True)
        #self.txt_suma.setReadOnly(False)

    # Área de los Slots
    def sumar(self):
        a = float(self.txt_a.text())
        b = float(self.txt_b.text())

        resultado = a + b

        self.txt_suma.setText(str(resultado))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())