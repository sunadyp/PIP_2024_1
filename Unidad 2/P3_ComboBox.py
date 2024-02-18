import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P3_ComboBox.ui"  # Nombre del archivo aquí.
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
            4: ["Jesús", "Ver series", 20, "A+", ":/variadas/cristobal.jpg"]
        }

        self.combo_personas.addItem("Selecciona...", 0)
        self.combo_personas.addItem("Pavel", 1)
        self.combo_personas.addItem("Alfonso", 2)
        self.combo_personas.addItem("Adán", 3)
        self.combo_personas.addItem("Jesús", 4)
        self.combo_personas.currentIndexChanged.connect(self.cambia)


    # Área de los Slots
    def cambia(self):
        print("Text: " + self.combo_personas.currentText())
        print("Index: " + str(self.combo_personas.currentIndex()))
        print("Data: " + str(self.combo_personas.currentData()))

        dataClave = self.combo_personas.currentText()
        imagen = self.datos_personas[dataClave][-1]
        self.img_persona.setPixmap(QtGui.QPixmap(imagen))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
