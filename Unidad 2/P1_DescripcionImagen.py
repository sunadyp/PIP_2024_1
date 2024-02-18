import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P1_DescripcionImagen.ui"  # Nombre del archivo aquí.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.datos_personas = {
            1:["Pavel", "Jugar", 20, "O+", ":/variadas/pavel.jpg"],
            2: ["Alfonso", "Mamar pn", 20, "A+", ":/variadas/poncho.jpg"],
            3: ["Adán", "Programar", 20, "O+", ":/variadas/adan.jpg"],
            4: ["Jesús", "Ver series", 20, "A+", ":/variadas/cristobal.jpg"],
        }

        self.btn_atras.clicked.connect(self.atras)

        self.btn_adelante.clicket.connect(self.adelante)

        self.index_control = 0

        self.btn_atras.setEnabled(False)

    # Área de los Slots
    def atras(self):
        if self.index_control > 1:
            self.index_control -= 1
            datos = self.datos_personas[self.index_control]
            print(datos)
            self.btn_adelante.setEnabled(True)
            ##change_img
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))

        if self.index_control == 1:
            self.btn_atras.setEnabled(False)

    def adelante(self):
        if self.index_control < 5:
            self.index_control += 1
            datos = self.datos_personas[self.index_control]
            print(datos)
            self.btn_atras.setEnabled(True)
            self.img_persona.setPixmap(QtGui.QPixmap(datos[-1]))

        if self.index_control == 5:
            self.btn_adelante.setEnabled(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
