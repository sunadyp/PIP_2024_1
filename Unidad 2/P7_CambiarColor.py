import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P7_CambiarColor.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.valor_r.setMinimum(0)
        self.valor_r.setMaximum(255)
        self.valor_r.setSingleStep(1)
        self.valor_r.setValue(0)
        self.valor_r.valueChanged.connect(self.cambiaR)

        self.R = 0
        self.G = 0
        self.B = 0

        self.valor_g.setMinimum(0)
        self.valor_g.setMaximum(255)
        self.valor_g.setSingleStep(1)
        self.valor_g.setValue(0)
        self.valor_g.valueChanged.connect(self.cambiaG)

        self.R = 0
        self.G = 0
        self.B = 0

        self.valor_b.setMinimum(0)
        self.valor_b.setMaximum(255)
        self.valor_b.setSingleStep(1)
        self.valor_b.setValue(0)
        self.valor_b.valueChanged.connect(self.cambiaB)

        self.R = 0
        self.G = 0
        self.B = 0

    # Área de los Slots
    def cambiaR(self):
        self.R = self.valor_r.value()
    def cambiaG(self):
        self.G = self.valor_g.value()

    def cambiaB(self):
        self.B = self.valor_b.value()
        estilo = ("background-color: rgb("+ str(self.R") + "," + ")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
