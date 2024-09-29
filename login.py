import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
                            
from PyQt5 import uic, QtWidgets
from Factura import Ui_PupuseriaJuanPerez


class ventanaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui",self)
        self.boton = self.findChild(QtWidgets.QPushButton, "BtnIngresar")
        self.contratxt = self.findChild(QtWidgets.QLineEdit, "lineEditContra")
        self.usuariotxt = self.findChild(QtWidgets.QLineEdit, "lineEditUsuario")
        self.boton.clicked.connect(self.pasarContra)
    #esta funcion verifica que la contra que se ingresa es la valida 
    def pasarContra(self):
      contra = self.contratxt.text()
      usuario = self.usuariotxt.text()

      if self.verificaCredenciales(usuario, contra):
                QMessageBox.information(self, 'Éxito', 'Contraseña correcta')
                self.abrirVentanaFact()
      else:
                QMessageBox.warning(self, 'Error', 'Contraseña incorrecta')
    
    def abrirVentanaFact(self):
        self.ventana_factura = Ui_PupuseriaJuanPerez()
        self.ventana_factura.show()
        self.close()
        

    def verificaCredenciales(self, usuario, contra):
        return usuario == "juan" and contra == "pupas"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ventanaLogin()
    window.show()
    sys.exit(app.exec_())