import smtplib
from dotenv import load_dotenv
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QComboBox, QLineEdit, QWidget
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QFont
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart 
from PIL import Image #luego agregar el logo 


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
        self.setStyleSheet("background-color: rgb(234, 212, 149 );")
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
        self.lblEmpresa.setText("PupasSV")

        # ComboBox para elegir pupusa
        self.tdPupusa = QComboBox(self.centralwidget)
        self.tdPupusa.setGeometry(QRect(180, 111, 151, 31))
        self.tdPupusa.setStyleSheet("background-color: rgb(255, 255, 255); font: 14pt 'MS Shell Dlg 2';")
        self.tdPupusa.addItems(["Frijol $0.35", "Queso $0.35", "Revueltas $0.35", "Loroco $0.35", 
                                "Ajo $0.40", "Carne $0.40", "Loca $0.65"])

        # Label para selección de pupusa
        self.lblDequees = QLabel(self.centralwidget)
        self.lblDequees.setGeometry(QRect(40, 110, 131, 31))
        self.lblDequees.setStyleSheet("background-color: rgb(255, 255, 255); font: 75 8pt 'MS Sans Serif';")
        self.lblDequees.setText("De qué es la Pupusa")

        # Campo para la cantidad de pupusas
        self.txtCantidadPupusas = QLineEdit(self.centralwidget)
        self.txtCantidadPupusas.setGeometry(QRect(200, 140, 50, 31))
        self.txtCantidadPupusas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtCantidadPupusas.setPlaceholderText("Cantidad")

        # ComboBox para elegir bebida
        self.tdBebida = QComboBox(self.centralwidget)
        self.tdBebida.setGeometry(QRect(180, 180, 151, 31))
        self.tdBebida.setStyleSheet("background-color: rgb(255, 170, 0); font: 75 12pt 'MS Shell Dlg 2';")
        self.tdBebida.addItems(["Nada $0.00", "Bolsa con agua $0.25", "Jugo $0.50", "Fresco $0.50", "Soda $0.75"])

        # Label para selección de bebida
        self.lblBebida = QLabel(self.centralwidget)
        self.lblBebida.setGeometry(QRect(40, 180, 131, 31))
        self.lblBebida.setStyleSheet("background-color: rgb(255, 255, 255); font: 75 8pt 'MS Sans Serif';")
        self.lblBebida.setText("Bebida")

        # Campo para cantidad de bebida
        self.txtCantidadBebidas = QLineEdit(self.centralwidget)
        self.txtCantidadBebidas.setGeometry(QRect(200, 210, 50, 31))
        self.txtCantidadBebidas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtCantidadBebidas.setPlaceholderText("Cantidad")

        # Label para cantidad de bebida
        self.lblCantidadBebida = QLabel(self.centralwidget)
        self.lblCantidadBebida.setGeometry(QRect(40, 210, 151, 31))
        self.lblCantidadBebida.setStyleSheet("background-color: rgb(255, 255, 255); font: 75 8pt 'MS Sans Serif';")
        self.lblCantidadBebida.setText("Cantidad Bebida")

        # Campo para dirección del cliente
        self.txtDireccionC = QLineEdit(self.centralwidget)
        self.txtDireccionC.setGeometry(QRect(200, 260, 231, 31))
        self.txtDireccionC.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.txtDireccionC.setPlaceholderText("Correo del cliente")
        
        # Label para dirección del cliente
        self.lblDirecCliente = QLabel(self.centralwidget)
        self.lblDirecCliente.setGeometry(QRect(40 ,260 ,151 ,31))
        self.lblDirecCliente.setStyleSheet("background-color: rgb(255 ,255 ,255);")
        self.lblDirecCliente.setAlignment(Qt.AlignCenter)
        self.lblDirecCliente.setText("Dirección de correo cliente")

        # Label para mostrar la cuenta total
        self.cuenta = QLabel(self.centralwidget)
        self.cuenta.setObjectName("cuenta")
        self.cuenta.setGeometry(QRect(200 ,310 ,231 ,31))
        self.cuenta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cuenta.setText("$0.00")
        self.cuenta.setAlignment(Qt.AlignCenter)

        # Label para cuenta
        lblCuentaTexto = QLabel(self.centralwidget)
        lblCuentaTexto.setGeometry(QRect(40 ,310 ,151 ,31))
        lblCuentaTexto.setStyleSheet("background-color: rgb(255 ,255 ,255);")
        lblCuentaTexto.setAlignment(Qt.AlignCenter)
        lblCuentaTexto.setText("Cuenta:")

        # Campo para 'Paga con'
        self.pagaCon = QLineEdit(self.centralwidget)
        self.pagaCon.setGeometry(QRect(200 ,360 ,231 ,31))
        self.pagaCon.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pagaCon.setPlaceholderText("Paga con")

        # Label para 'Paga con'
        lblPagaConTexto = QLabel(self.centralwidget)
        lblPagaConTexto.setGeometry(QRect(40 ,360 ,151 ,31))
        lblPagaConTexto.setStyleSheet("background-color: rgb(255 ,255 ,255);")
        lblPagaConTexto.setAlignment(Qt.AlignCenter)
        lblPagaConTexto.setText("Paga con:")

        # Label para total
        lblTotalTexto = QLabel(self.centralwidget)
        lblTotalTexto.setGeometry(QRect(40 ,410 ,151 ,31))
        lblTotalTexto.setStyleSheet("background-color: rgb(255 ,255 ,255);")
        lblTotalTexto.setAlignment(Qt.AlignCenter)
        lblTotalTexto.setText("Cambio:")

        # Campo para el total (QLabel)
        self.txtTotal = QLabel(self.centralwidget)  
        self.txtTotal.setGeometry(QRect(200 ,410 ,231 ,31))  
        self.txtTotal.setStyleSheet("background-color: rgb(255,170,0);")  
        self.txtTotal.setText("$0.00")  
        self.txtTotal.setAlignment(Qt.AlignCenter)  

        # Botón para enviar el recibo
        self.enviarCorreo = QPushButton(self.centralwidget)
        self.enviarCorreo.setGeometry(QRect(110 ,450 ,161 ,23))
        self.enviarCorreo.setStyleSheet("background-color: rgb(255 ,170 ,0);")
        self.enviarCorreo.clicked.connect(self.enviar_recibo)
        self.enviarCorreo.setText("Enviar Recibo")

        # Mensaje de agradecimiento
        grax = QLabel(self.centralwidget)
        grax.setGeometry(QRect(300 ,520 ,151 ,31))
        grax.setStyleSheet("background-color: rgb(255 ,255 ,255);\n"
                           "font:75 ;8pt 'MS Sans Serif';")
        grax.setAlignment(Qt.AlignCenter)
        grax.setText("Gracias por Preferirnos")

        # Conectar señales a métodos
        self.tdPupusa.currentIndexChanged.connect(self.calcular_total)
        self.tdBebida.currentIndexChanged.connect(self.calcular_total)
        self.pagaCon.textChanged.connect(self.calcular_total)
        self.txtCantidadPupusas.textChanged.connect(self.calcular_total)  # Conectar cantidad de pupusas
        self.txtCantidadBebidas.textChanged.connect(self.calcular_total)  # Conectar cantidad de bebidas

        self.setCentralWidget(self.centralwidget)
        self.setWindowTitle("Pupusería Juan Pérez")

    def calcular_total(self):
        """Calcula el total de la cuenta."""
        # Precios de pupusas y bebidas
        total_pupusa = {
            "Frijol $0.35": 0.35,
            "Queso $0.35": 0.35,
            "Revueltas $0.35": 0.35,
            "Loroco $0.35": 0.35,
            "Ajo $0.40": 0.40,
            "Carne $0.40": 0.40,
            "Loca $0.65": 0.65,
        }

        total_bebida = {
            "Nada $0.00": 0.00,
            "Bolsa con agua $0.25": 0.25,
            "Jugo $0.50": 0.50,
            "Fresco $0.50": 0.50,
            "Soda $0.75": 0.75,
        }

        # Obtener los valores seleccionados
        precio_pupusa = total_pupusa[self.tdPupusa.currentText()]
        precio_bebida = total_bebida[self.tdBebida.currentText()]

        # Obtener la cantidad de pupusas
        try:
            cantidad_pupusas = int(self.txtCantidadPupusas.text()) if self.txtCantidadPupusas.text() else 0
        except ValueError:
            cantidad_pupusas = 0  # En caso de que la entrada no sea un número válido

        # Obtener la cantidad de bebidas
        try:
            cantidad_bebidas = int(self.txtCantidadBebidas.text()) if self.txtCantidadBebidas.text() else 0
        except ValueError:
            cantidad_bebidas = 0  # En caso de que la entrada no sea un número válido

        # Calcular el total de la cuenta
        cuenta_total = (precio_pupusa * cantidad_pupusas) + (precio_bebida * cantidad_bebidas)
        self.cuenta.setText(f"${cuenta_total:.2f}")  # Mostrar en el label de cuenta
        
        # Calcular el vuelto si se ha ingresado un valor en "Paga con"
        if self.pagaCon.text():
            paga_con = float(self.pagaCon.text())
            vuelto = paga_con - cuenta_total
            self.txtTotal.setText(f"${vuelto:.2f}")  # Mostrar el vuelto en el total
        else:
            self.txtTotal.setText("$0.00")  # Si no hay valor en "Paga con", poner $0.00

    def enviar_recibo(self):
        """Envía el recibo por correo electrónico."""
        # Obtener la dirección de correo y el total
        direccion_cliente = self.txtDireccionC.text()
        total = self.cuenta.text()

        # Crear el mensaje
        mensaje = MIMEMultipart()
        mensaje['From'] = remit
        mensaje['To'] = direccion_cliente
        mensaje['Subject'] = "Recibo de compra"

        # Cuerpo del mensaje
        cuerpo = f"Gracias por su compra.\nSu total es: {total}\n¡Vuelva pronto!"
        mensaje.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

        try:
            with smtplib.SMTP(serv, puerto) as server:
                server.starttls()
                server.login(remit, contra)
                server.sendmail(remit, direccion_cliente, mensaje.as_string())
            print("Recibo enviado correctamente.")
        except Exception as e:
            print(f"Ocurrió un error al enviar el recibo: {e}")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = Ui_PupuseriaJuanPerez()
    window.show()
    sys.exit(app.exec_())
