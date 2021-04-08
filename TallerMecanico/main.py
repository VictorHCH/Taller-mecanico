import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QToolBar
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtSql import QSqlQuery, QSqlQueryModel, QSqlDatabase, QSqlTableModel


class VentanaPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaPrincipal, self).__init__(parent)
        loadUi('Inicio.ui', self)
        self.btn.clicked.connect(self.VentanaVenta)
        self.lb.setPixmap(QPixmap("Fondo.png"))
        self.lb.setScaledContents(True)

    def VentanaVenta(self):
        self.hide()
        otraventana = VentanaVenta(self)
        otraventana.show()


class VentanaVenta(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaVenta, self).__init__(parent)
        loadUi('Venta.ui', self)

        barra = QToolBar()
        barra.setIconSize(QSize(30, 30))
        self.addToolBar(barra)

        venta = QAction(QIcon("venta.ico"), "Venta", self)
        venta.triggered.connect(self.btnVenta)
        barra.addAction(venta)

        barra.addSeparator()

        cliente = QAction(QIcon("cliente.ico"), "Clientes", self)
        cliente.triggered.connect(self.btnCliente)
        barra.addAction(cliente)

        barra.addSeparator()

        inv = QAction(QIcon("inv.ico"), "Inventario", self)
        inv.triggered.connect(self.btnInv)
        barra.addAction(inv)

        barra.addSeparator()

        reg = QAction(QIcon("registro.ico"), "Registro de ventas", self)
        reg.triggered.connect(self.btnReg)
        barra.addAction(reg)

        #VENTANA NUEVO USUARIO
        self.btn.clicked.connect(self.btnNuevoCliente())

    def btnVenta(self):
        pass

    def btnCliente(self):
        self.hide()
        otraventana = VentanaClientes(self)
        otraventana.show()

    def btnInv(self, s):
        self.hide()
        otraventana = VentanaInventario(self)
        otraventana.show()

    def btnReg(self, s):
        self.hide()
        otraventana = VentanaRegistros(self)
        otraventana.show()

    def btnNuevoCliente(self):
        print("Hola")
        self.hide()
        otraventana = VentanaClienteNuevo(self)
        otraventana.show()


class VentanaClientes(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaClientes, self).__init__(parent)
        loadUi('Clientes.ui', self)

        barra = QToolBar()
        barra.setIconSize(QSize(30, 30))
        self.addToolBar(barra)

        venta = QAction(QIcon("venta.ico"), "Venta", self)
        venta.triggered.connect(self.btnVenta)
        barra.addAction(venta)

        barra.addSeparator()

        cliente = QAction(QIcon("cliente.ico"), "Clientes", self)
        cliente.triggered.connect(self.btnCliente)
        barra.addAction(cliente)

        barra.addSeparator()

        inv = QAction(QIcon("inv.ico"), "Inventario", self)
        inv.triggered.connect(self.btnInv)
        barra.addAction(inv)

        barra.addSeparator()

        reg = QAction(QIcon("registro.ico"), "Registro de ventas", self)
        reg.triggered.connect(self.btnReg)
        barra.addAction(reg)

    def btnVenta(self):
        self.hide()
        otraventana = VentanaVenta(self)
        otraventana.show()

    def btnCliente(self):
        pass

    def btnInv(self, s):
        self.hide()
        otraventana = VentanaInventario(self)
        otraventana.show()

    def btnReg(self, s):
        self.hide()
        otraventana = VentanaRegistros(self)
        otraventana.show()


class VentanaInventario(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaInventario, self).__init__(parent)
        loadUi('Inventario.ui', self)

        barra = QToolBar()
        barra.setIconSize(QSize(30, 30))
        self.addToolBar(barra)

        venta = QAction(QIcon("venta.ico"), "Venta", self)
        venta.triggered.connect(self.btnVenta)
        barra.addAction(venta)

        barra.addSeparator()

        cliente = QAction(QIcon("cliente.ico"), "Clientes", self)
        cliente.triggered.connect(self.btnCliente)
        barra.addAction(cliente)

        barra.addSeparator()

        inv = QAction(QIcon("inv.ico"), "Inventario", self)
        inv.triggered.connect(self.btnInv)
        barra.addAction(inv)

        barra.addSeparator()

        reg = QAction(QIcon("registro.ico"), "Registro de ventas", self)
        reg.triggered.connect(self.btnReg)
        barra.addAction(reg)



    def btnVenta(self):
        self.hide()
        otraventana = VentanaVenta(self)
        otraventana.show()

    def btnCliente(self):
        self.hide()
        otraventana = VentanaClientes(self)
        otraventana.show()

    def btnInv(self, s):
        pass

    def btnReg(self, s):
        self.hide()
        otraventana = VentanaRegistros(self)
        otraventana.show()


class VentanaRegistros(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaRegistros, self).__init__(parent)
        loadUi('RegistroVentas.ui', self)

        barra = QToolBar()
        barra.setIconSize(QSize(30, 30))
        self.addToolBar(barra)

        venta = QAction(QIcon("venta.ico"), "Venta", self)
        venta.triggered.connect(self.btnVenta)
        barra.addAction(venta)

        barra.addSeparator()

        cliente = QAction(QIcon("cliente.ico"), "Clientes", self)
        cliente.triggered.connect(self.btnCliente)
        barra.addAction(cliente)

        barra.addSeparator()

        inv = QAction(QIcon("inv.ico"), "Inventario", self)
        inv.triggered.connect(self.btnInv)
        barra.addAction(inv)

        barra.addSeparator()

        reg = QAction(QIcon("registro.ico"), "Registro de ventas", self)
        reg.triggered.connect(self.btnReg)
        barra.addAction(reg)

    def btnVenta(self):
        self.hide()
        otraventana = VentanaVenta(self)
        otraventana.show()

    def btnCliente(self):
        self.hide()
        otraventana = VentanaClientes(self)
        otraventana.show()

    def btnInv(self, s):
        self.hide()
        otraventana = VentanaInventario(self)
        otraventana.show()

    def btnReg(self, s):
        pass


class VentanaClienteNuevo(QMainWindow):
    def __init__(self, parent=None):
        super(VentanaClienteNuevo, self).__init__(parent)
        loadUi("ClienteNuevo.ui")


app = QApplication(sys.argv)
main = VentanaPrincipal()
main.show()
sys.exit(app.exec_())