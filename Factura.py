import smtplib
from dotenv import load_dotenv
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QComboBox, QLineEdit, QStatusBar, QWidget
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
import sys
# Cargar variables de entorno
load_dotenv()


remit = os.getenv('CORREO')
serv = os.getenv('SERV')
puerto = int(os.getenv('PUERTO'))
contra = os.getenv('CONTRA')

class Ui_PupuseriaJuanPerez(QMainWindow):
    def __init__(self):
        super(Ui_PupuseriaJuanPerez, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("PupuseriaJuanPerez")
        self.resize(466, 610)
        self.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Label para el nombre de la empresa
        self.lblEmpresa = QLabel(self.centralwidget)
        self.lblEmpresa.setObjectName("lblEmpresa")
        self.lblEmpresa.setGeometry(QRect(0, 0, 471, 81))
        font = QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(16)
        self.lblEmpresa.setFont(font)
        self.lblEmpresa.setStyleSheet("background-color: rgb(255, 170, 0); font: 63 16pt 'Yu Gothic UI Semibold';")
        self.lblEmpresa.setAlignment(Qt.AlignCenter)
        self.lblEmpresa.setText("Pupuseria Juan Perez")

        # ComboBox para elegir pupusa
        self.tdPupusa = QComboBox(self.centralwidget)
        self.tdPupusa.setGeometry(QRect(180, 111, 151, 31))
        self.tdPupusa.setStyleSheet("background-color: rgb(255, 255, 255); font: 14pt 'MS Shell Dlg 2';")
        self.tdPupusa.addItems(["Frijol $0.35", "Queso $0.35", "Revueltas $0.35", "Loroco $0.35", 
                                "Ajo $0.40", "Carne $0.40", "Loca $0.65"])

        # ComboBox para elegir bebida
        self.TdBebida = QComboBox(self.centralwidget)
        self.TdBebida.setGeometry(QRect(180, 180, 151, 31))
        self.TdBebida.setStyleSheet("background-color: rgb(170, 255, 127); font: 75 12pt 'MS Shell Dlg 2';")
        self.TdBebida.addItems(["Nada $0.00", "Bolsa con agua $0.25", "Jugo $0.50", "Fresco $0.50", "Soda $0.75"])

        # Campo para dirección del cliente
        self.txtDireccionC = QLineEdit(self.centralwidget)
        self.txtDireccionC.setGeometry(QRect(200, 260, 231, 31))
        self.txtDireccionC.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.txtDireccionC.setPlaceholderText("Correo del cliente")

        # Campo para la cuenta
        self.cuenta = QLineEdit(self.centralwidget)
        self.cuenta.setGeometry(QRect(200, 310, 231, 31))
        self.cuenta.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.cuenta.setPlaceholderText("Cuenta")

        # Campo para 'Paga con'
        self.pagaCon = QLineEdit(self.centralwidget)
        self.pagaCon.setGeometry(QRect(200, 360, 231, 31))
        self.pagaCon.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.pagaCon.setPlaceholderText("Paga con")

        # Campo para el total
        self.txtTotal = QLineEdit(self.centralwidget)
        self.txtTotal.setGeometry(QRect(200, 410, 231, 31))
        self.txtTotal.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.txtTotal.setPlaceholderText("Total")

        # Botón para enviar el recibo
        self.EnviarCorreo = QPushButton(self.centralwidget)
        self.EnviarCorreo.setGeometry(QRect(110, 450, 161, 23))
        self.EnviarCorreo.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.EnviarCorreo.setText("Enviar Recibo")
        self.EnviarCorreo.clicked.connect(self.enviar_recibo)

        # Mensaje de agradecimiento
        self.Grax = QLabel(self.centralwidget)
        self.Grax.setGeometry(QRect(300, 520, 151, 31))
        self.Grax.setStyleSheet("background-color: rgb(255, 255, 255); font: 75 8pt 'MS Sans Serif';")
        self.Grax.setAlignment(Qt.AlignCenter)
        self.Grax.setText("Gracias por Preferirnos")

        # Status bar
        self.setStatusBar(QStatusBar(self))

        self.setCentralWidget(self.centralwidget)

    def enviar_recibo(self):
        correo_cliente = self.txtDireccionC.text()
        total = self.txtTotal.text()
        cuenta = self.cuenta.text()
        paga_con = self.pagaCon.text()

        mensaje = f"""Subject: Recibo de compra - Pupusería Juan Perez
        
        Estimado cliente,

        Gracias por su compra. Aquí está el resumen de su pedido:
        - Total a pagar: {total}
        - Cuenta: {cuenta}
        - Paga con: {paga_con}

        ¡Gracias por preferirnos!
        """

        try:
            conex = smtplib.SMTP(serv, puerto)
            conex.starttls()
            conex.login(remit, contra)
            conex.sendmail(remit, correo_cliente, mensaje)
            print("El recibo ha sido enviado correctamente al cliente")
        except smtplib.SMTPException as e:
            print(f"Error al mandar el mensaje: {e}")
        finally:
            conex.quit()

if __name__ == "__main__":
    app = QApplication([])
    ventana = Ui_PupuseriaJuanPerez()
    ventana.show()
    app.exec_()
