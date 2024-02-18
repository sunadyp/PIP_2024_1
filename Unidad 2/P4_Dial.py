import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P4_Dial.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_personas = {
            1: ["Pavel", "Jugar", 20, "O+", ":/variadas/pavel.jpg"],
            2: ["Alfonso", "Mamar pn", 20, "A+", ":/variadas/poncho.jpg"],
            3: ["Adán", "Programar", 20, "O+", ":/variadas/adan.jpg"],
            4: ["Jesús", "Ver series", 20, "A+", ":/variadas/cristobal.jpg"],
        }

        self.dial_personas.setMinimum(0)
        self.dial_personas.setMinimum(5)
        self.dial_personas.setMinimum(1)
        self.dial_personas.setMinimum(1)
        self.combo_personas.currentIndexChanged.connect(self.cambia)

    # Área de los Slots
    def cambia(self):
        dataClave = self.dial_personas.value
        imagen = self.datos_personas[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
