import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P2_SeleccionEquipo.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        ##self.text_equipo.setPlainText("Hola \n mundo")
        self.cb_persona1.toggled.connect(self.sel_persona1)
        self.cb_persona2.toggled.connect(self.sel_persona2)
        self.cb_persona3.toggled.connect(self.sel_persona3)
        self.cb_persona4.toggled.connect(self.sel_persona4)

        self.persona1 = ""
        self.persona2 = ""
        self.persona3 = ""
        self.persona4 = ""

    # Área de los Slots

    def sel_persona1(self):
        if self.cb_persona1.isChecked():
            print("Persona 1 True")
            self.persona1 = "Persona 1\n"
        else:
            print("Persona 1 False")
            self.persona1 = ""
        self.txt_equipo.setPlainText(self.persona1 + self.persona2 + self.persona3 + self.persona4)
    def sel_persona2(self):
        if self.cb_persona2.isChecked():
            print("Persona 2 True")
            self.persona2 = "Persona 2\n"
        else:
            print("Persona 2 False")
            self.persona2 = ""
        self.txt_equipo.setPlainText(self.persona1 + self.persona2 + self.persona3 + self.persona4)

    def sel_persona3(self):
        pass

    def sel_persona4(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
