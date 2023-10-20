from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QGraphicsDropShadowEffect
from PyQt5.QtCore import QFile, QTextStream
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import (QIcon)

import sys

from SqMain import Ui_MainWindow
from SqTamano import Ui_Form
from SqActv import Ui_FormActv
from SqCaracter import Ui_FormCaracter
from SqClima import Ui_FormClima

class ventanaApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowTitle("ID Perros")
        self.titulo.setText("Escoge a tu perro ideal")
        self.tituloCompatibilidad.setText("Proximo amigo")
        self.btnTam.setText("Tamaño")
        self.btnActividad.setText("Actividad Fisica")
        self.btnCaracter.setText("Caracter")
        self.btnClima.setText("Clima")

        self.btnTam.clicked.connect(self.mostrarTam)
        self.btnActividad.clicked.connect(self.mostrarActv)
        self.btnCaracter.clicked.connect(self.mostrarCaracter)
        self.btnClima.clicked.connect(self.mostrarClima)
    
    def mostrarTam(self):
        window.hide()
        tam.show()
    
    def mostrarActv(self):
        window.hide()
        actv.show()
    
    def mostrarCaracter(self):
        window.hide()
        caracter.show()

    def mostrarClima(self):
        window.hide()
        clima.show()

class ventanaTam(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tituloTam.setText("TAMAÑO")
        self.pregTam.setText("¿Prefieres perros pequeños, medianos o grandes?")
        self.boxTam.addItems(["Pequeños", "Medianos", "Grandes"])
        self.aceptar.clicked.connect(self.obtenerInformacion)

    def obtenerInformacion(self):
        print("Degree : {0}".format(self.boxTam.currentText()))
        tam.hide()
        window.show()

class ventanaActv(QMainWindow, Ui_FormActv):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tituloActv.setText("ACTIVIDAD FISICA")

        self.pregunta1.setPlainText("¿Cuánto tiempo puedes dedicar al ejercicio diario del perro?")
        self.respuestas1.addItems(["15 - 30 min", "40 - 60 min", "70 - 120 min"])

        self.pregunta2.setPlainText("¿Te gustaría un perro que sea activo y juguetón o más tranquilo?")
        self.respuestas2.addItems(["tranquilo", "jugueton"])

        self.pregunta3.setText("¿Que tan activo eres?")
        self.respuestas3.addItems(["poco", "normal", "mucho"])
    
        self.aceptar.clicked.connect(self.obtenerInformacion)

    def obtenerInformacion(self):
        print("Degree : {0}".format(self.respuestas1.currentText()))
        print("Degree : {0}".format(self.respuestas2.currentText()))
        print("Degree : {0}".format(self.respuestas3.currentText()))
        actv.hide()
        window.show()

class ventanaCaracter(QMainWindow, Ui_FormCaracter):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tituloCaracteristicas.setText("CARACTERISTICAS")

        self.pregunta1.setPlainText("¿Prefieres perros que sean más independientes o aquellos que son más afectuosos y buscan compañía?")
        self.respuestas1.addItems(["independientes", "afectuosos"])

        self.pregunta2.setPlainText("¿Tienes niños en casa?")
        self.respuestas2.addItems(["no", "si"])

    
        self.aceptar.clicked.connect(self.obtenerInformacion)

    def obtenerInformacion(self):
        print("Degree : {0}".format(self.respuestas1.currentText()))
        print("Degree : {0}".format(self.respuestas2.currentText()))
        caracter.hide()
        window.show()
        
class ventanaClima(QMainWindow, Ui_FormClima):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tituloClima.setText("CLIMA")

        self.pregunta1.setPlainText("¿Vives en un área con un clima cálido, frío o templado?")
        self.respuestas1.addItems(["calido", "templado", "frio"])

        self.pregunta2.setPlainText("¿Estás dispuesto a cuidar el pelaje de un perro que pueda ser sensible a ciertos climas?")
        self.respuestas2.addItems(["no", "si"])

    
        self.aceptar.clicked.connect(self.obtenerInformacion)

    def obtenerInformacion(self):
        print("Degree : {0}".format(self.respuestas1.currentText()))
        print("Degree : {0}".format(self.respuestas2.currentText()))
        clima.hide()
        window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open("./diseño/style.css", "r").read())
    tam = ventanaTam()
    actv = ventanaActv()
    caracter = ventanaCaracter()
    clima = ventanaClima()
    window = ventanaApp()
    window.show()
    sys.exit(app.exec())