# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1212, 684)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frameSuperior = QtWidgets.QFrame(self.centralwidget)
        self.frameSuperior.setMinimumSize(QtCore.QSize(0, 40))
        self.frameSuperior.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frameSuperior.setStyleSheet("background-color: rgb(19, 136, 168);")
        self.frameSuperior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSuperior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSuperior.setObjectName("frameSuperior")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frameSuperior)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_Menu = QtWidgets.QPushButton(self.frameSuperior)
        self.btn_Menu.setMinimumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.btn_Menu.setFont(font)
        self.btn_Menu.setStyleSheet("QPushButton{\n"
"background-color: rgb(19, 136, 168);\n"
"font :87 12pt \"Arial Black\";\n"
"border-radius:0px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"font :87 12pt \"Arial Black\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/menu.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Menu.setIcon(icon)
        self.btn_Menu.setIconSize(QtCore.QSize(32, 32))
        self.btn_Menu.setObjectName("btn_Menu")
        self.horizontalLayout_2.addWidget(self.btn_Menu)
        spacerItem = QtWidgets.QSpacerItem(644, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.btn_Minimizar = QtWidgets.QPushButton(self.frameSuperior)
        self.btn_Minimizar.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"backgroud-color:#ffff00;\n"
"}")
        self.btn_Minimizar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/minus-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Minimizar.setIcon(icon1)
        self.btn_Minimizar.setIconSize(QtCore.QSize(32, 32))
        self.btn_Minimizar.setObjectName("btn_Minimizar")
        self.horizontalLayout_2.addWidget(self.btn_Minimizar)
        self.btn_Restaurar = QtWidgets.QPushButton(self.frameSuperior)
        self.btn_Restaurar.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"backgroud-color:#ffff00;\n"
"}\n"
"")
        self.btn_Restaurar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/minimize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Restaurar.setIcon(icon2)
        self.btn_Restaurar.setIconSize(QtCore.QSize(32, 32))
        self.btn_Restaurar.setObjectName("btn_Restaurar")
        self.horizontalLayout_2.addWidget(self.btn_Restaurar)
        self.btn_Maximizar = QtWidgets.QPushButton(self.frameSuperior)
        self.btn_Maximizar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.btn_Maximizar.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"backgroud-color:#ffff00;\n"
"}\n"
"")
        self.btn_Maximizar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/maximize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Maximizar.setIcon(icon3)
        self.btn_Maximizar.setIconSize(QtCore.QSize(32, 32))
        self.btn_Maximizar.setObjectName("btn_Maximizar")
        self.horizontalLayout_2.addWidget(self.btn_Maximizar)
        self.btn_Cerrar = QtWidgets.QPushButton(self.frameSuperior)
        self.btn_Cerrar.setMaximumSize(QtCore.QSize(16777215, 35))
        self.btn_Cerrar.setStyleSheet("QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border:5px solid #aa00ff;\n"
"backgroud-color:#ffff00;\n"
"}\n"
"")
        self.btn_Cerrar.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/x-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Cerrar.setIcon(icon4)
        self.btn_Cerrar.setIconSize(QtCore.QSize(32, 32))
        self.btn_Cerrar.setObjectName("btn_Cerrar")
        self.horizontalLayout_2.addWidget(self.btn_Cerrar)
        self.gridLayout_2.addWidget(self.frameSuperior, 0, 0, 1, 1)
        self.frameInferior = QtWidgets.QFrame(self.centralwidget)
        self.frameInferior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameInferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameInferior.setObjectName("frameInferior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameInferior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frameLateral = QtWidgets.QFrame(self.frameInferior)
        self.frameLateral.setMinimumSize(QtCore.QSize(0, 0))
        self.frameLateral.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frameLateral.setStyleSheet("QFrame{\n"
"background-color: rgb(19, 136, 168);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(19, 136, 168);\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"\n"
"font:75 12pt \"Arial Narrow\";\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius:20px;\n"
"border-bottom-left-radius:20px;\n"
"\n"
"font:75 12pt \"Arial Narrow\";\n"
"}\n"
"\n"
"")
        self.frameLateral.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameLateral.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameLateral.setObjectName("frameLateral")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameLateral)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_Inicio = QtWidgets.QPushButton(self.frameLateral)
        self.btn_Inicio.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_Inicio.setMaximumSize(QtCore.QSize(16777215, 40))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Inicio.setIcon(icon5)
        self.btn_Inicio.setIconSize(QtCore.QSize(32, 32))
        self.btn_Inicio.setObjectName("btn_Inicio")
        self.verticalLayout_3.addWidget(self.btn_Inicio)
        self.btn_Pacientes = QtWidgets.QPushButton(self.frameLateral)
        self.btn_Pacientes.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_Pacientes.setMaximumSize(QtCore.QSize(16777215, 40))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Pacientes.setIcon(icon6)
        self.btn_Pacientes.setIconSize(QtCore.QSize(32, 32))
        self.btn_Pacientes.setObjectName("btn_Pacientes")
        self.verticalLayout_3.addWidget(self.btn_Pacientes)
        self.btn_Terapias = QtWidgets.QPushButton(self.frameLateral)
        self.btn_Terapias.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_Terapias.setMaximumSize(QtCore.QSize(16777215, 40))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/heart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Terapias.setIcon(icon7)
        self.btn_Terapias.setIconSize(QtCore.QSize(32, 32))
        self.btn_Terapias.setObjectName("btn_Terapias")
        self.verticalLayout_3.addWidget(self.btn_Terapias)
        spacerItem1 = QtWidgets.QSpacerItem(20, 425, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.frameLateral)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout.addWidget(self.frameLateral)
        self.frameContenedor = QtWidgets.QFrame(self.frameInferior)
        self.frameContenedor.setStyleSheet("\n"
"QWidget{\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frameContenedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameContenedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameContenedor.setObjectName("frameContenedor")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frameContenedor)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frameContenedor)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_0 = QtWidgets.QWidget()
        self.page_0.setObjectName("page_0")
        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.stackedWidget.addWidget(self.page_1)
        self.page_Pacientes_no_usable = QtWidgets.QWidget()
        self.page_Pacientes_no_usable.setObjectName("page_Pacientes_no_usable")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_Pacientes_no_usable)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(20, 188, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.btn_CrearPaciente = QtWidgets.QPushButton(self.page_Pacientes_no_usable)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_CrearPaciente.setFont(font)
        self.btn_CrearPaciente.setStyleSheet("background-color: rgb(221, 117, 255);")
        self.btn_CrearPaciente.setObjectName("btn_CrearPaciente")
        self.verticalLayout_4.addWidget(self.btn_CrearPaciente)
        self.btn_CrearPaciente_4 = QtWidgets.QPushButton(self.page_Pacientes_no_usable)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_CrearPaciente_4.setFont(font)
        self.btn_CrearPaciente_4.setStyleSheet("\n"
"background-color: rgb(98, 198, 80);")
        self.btn_CrearPaciente_4.setObjectName("btn_CrearPaciente_4")
        self.verticalLayout_4.addWidget(self.btn_CrearPaciente_4)
        self.btn_CrearPaciente_2 = QtWidgets.QPushButton(self.page_Pacientes_no_usable)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_CrearPaciente_2.setFont(font)
        self.btn_CrearPaciente_2.setStyleSheet("background-color: rgb(221, 117, 255);")
        self.btn_CrearPaciente_2.setObjectName("btn_CrearPaciente_2")
        self.verticalLayout_4.addWidget(self.btn_CrearPaciente_2)
        self.btn_CrearPaciente_3 = QtWidgets.QPushButton(self.page_Pacientes_no_usable)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_CrearPaciente_3.setFont(font)
        self.btn_CrearPaciente_3.setStyleSheet("background-color: rgb(221, 117, 255);")
        self.btn_CrearPaciente_3.setObjectName("btn_CrearPaciente_3")
        self.verticalLayout_4.addWidget(self.btn_CrearPaciente_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 187, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.stackedWidget.addWidget(self.page_Pacientes_no_usable)
        self.page_Inicio = QtWidgets.QWidget()
        self.page_Inicio.setAutoFillBackground(False)
        self.page_Inicio.setStyleSheet("")
        self.page_Inicio.setObjectName("page_Inicio")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_Inicio)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.page_Inicio)
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("owo.png"))
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.stackedWidget.addWidget(self.page_Inicio)
        self.page_Pacientes = QtWidgets.QWidget()
        self.page_Pacientes.setStyleSheet("")
        self.page_Pacientes.setObjectName("page_Pacientes")
        self.gridLayout = QtWidgets.QGridLayout(self.page_Pacientes)
        self.gridLayout.setObjectName("gridLayout")
        self.gb_RegistroUsuario = QtWidgets.QGroupBox(self.page_Pacientes)
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setItalic(True)
        self.gb_RegistroUsuario.setFont(font)
        self.gb_RegistroUsuario.setStyleSheet("background-color: rgb(70, 157, 214);")
        self.gb_RegistroUsuario.setObjectName("gb_RegistroUsuario")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gb_RegistroUsuario)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.lb_Contacto = QtWidgets.QLabel(self.gb_RegistroUsuario)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_Contacto.setFont(font)
        self.lb_Contacto.setObjectName("lb_Contacto")
        self.gridLayout_6.addWidget(self.lb_Contacto, 5, 0, 1, 1)
        self.txt_Apellido_Materno = QtWidgets.QLineEdit(self.gb_RegistroUsuario)
        self.txt_Apellido_Materno.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_Apellido_Materno.setObjectName("txt_Apellido_Materno")
        self.gridLayout_6.addWidget(self.txt_Apellido_Materno, 2, 3, 1, 3)
        self.lb_LastNameMother = QtWidgets.QLabel(self.gb_RegistroUsuario)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_LastNameMother.setFont(font)
        self.lb_LastNameMother.setObjectName("lb_LastNameMother")
        self.gridLayout_6.addWidget(self.lb_LastNameMother, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(80, 23, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem4, 3, 3, 1, 1)
        self.txt_Tutor = QtWidgets.QLineEdit(self.gb_RegistroUsuario)
        self.txt_Tutor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_Tutor.setObjectName("txt_Tutor")
        self.gridLayout_6.addWidget(self.txt_Tutor, 4, 3, 1, 3)
        self.lb_Tutor = QtWidgets.QLabel(self.gb_RegistroUsuario)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_Tutor.setFont(font)
        self.lb_Tutor.setObjectName("lb_Tutor")
        self.gridLayout_6.addWidget(self.lb_Tutor, 4, 0, 1, 1)
        self.lb_Edad = QtWidgets.QLabel(self.gb_RegistroUsuario)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_Edad.setFont(font)
        self.lb_Edad.setObjectName("lb_Edad")
        self.gridLayout_6.addWidget(self.lb_Edad, 3, 0, 1, 1)
        self.txt_Telefono = QtWidgets.QLineEdit(self.gb_RegistroUsuario)
        self.txt_Telefono.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_Telefono.setObjectName("txt_Telefono")
        self.gridLayout_6.addWidget(self.txt_Telefono, 5, 3, 1, 3)
        self.lb_Grade_Of_TEA = QtWidgets.QLabel(self.gb_RegistroUsuario)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_Grade_Of_TEA.setFont(font)
        self.lb_Grade_Of_TEA.setObjectName("lb_Grade_Of_TEA")
        self.gridLayout_6.addWidget(self.lb_Grade_Of_TEA, 3, 4, 1, 1)
        self.txt_Apellido_Paterno = QtWidgets.QLineEdit(self.gb_RegistroUsuario)
        self.txt_Apellido_Paterno.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_Apellido_Paterno.setObjectName("txt_Apellido_Paterno")
        self.gridLayout_6.addWidget(self.txt_Apellido_Paterno, 1, 4, 1, 2)
        self.lb_LastNameFater = QtWidgets.QLabel(self.gb_RegistroUsuario)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_LastNameFater.setFont(font)
        self.lb_LastNameFater.setObjectName("lb_LastNameFater")
        self.gridLayout_6.addWidget(self.lb_LastNameFater, 1, 0, 1, 1)
        self.lb_Name = QtWidgets.QLabel(self.gb_RegistroUsuario)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lb_Name.setFont(font)
        self.lb_Name.setObjectName("lb_Name")
        self.gridLayout_6.addWidget(self.lb_Name, 0, 0, 1, 1)
        self.txt_Nombre = QtWidgets.QLineEdit(self.gb_RegistroUsuario)
        self.txt_Nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txt_Nombre.setObjectName("txt_Nombre")
        self.gridLayout_6.addWidget(self.txt_Nombre, 0, 3, 1, 3)
        self.cb_Grado_TEA = QtWidgets.QComboBox(self.gb_RegistroUsuario)
        self.cb_Grado_TEA.setMaximumSize(QtCore.QSize(121, 21))
        self.cb_Grado_TEA.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_Grado_TEA.setObjectName("cb_Grado_TEA")
        self.gridLayout_6.addWidget(self.cb_Grado_TEA, 3, 5, 1, 1)
        self.cb_Edad = QtWidgets.QComboBox(self.gb_RegistroUsuario)
        self.cb_Edad.setMaximumSize(QtCore.QSize(121, 21))
        self.cb_Edad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_Edad.setObjectName("cb_Edad")
        self.gridLayout_6.addWidget(self.cb_Edad, 3, 2, 1, 1)
        self.btn_SaveDataOfUser = QtWidgets.QPushButton(self.gb_RegistroUsuario)
        self.btn_SaveDataOfUser.setMinimumSize(QtCore.QSize(131, 81))
        self.btn_SaveDataOfUser.setMaximumSize(QtCore.QSize(131, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_SaveDataOfUser.setFont(font)
        self.btn_SaveDataOfUser.setStyleSheet("background-color:rgb(255, 163, 35)")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_SaveDataOfUser.setIcon(icon8)
        self.btn_SaveDataOfUser.setObjectName("btn_SaveDataOfUser")
        self.gridLayout_6.addWidget(self.btn_SaveDataOfUser, 6, 4, 1, 1)
        self.gridLayout.addWidget(self.gb_RegistroUsuario, 0, 0, 1, 1)
        self.gb_SeleccionTerapias = QtWidgets.QGroupBox(self.page_Pacientes)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setItalic(True)
        self.gb_SeleccionTerapias.setFont(font)
        self.gb_SeleccionTerapias.setStyleSheet("background-color: rgb(55, 177, 116);")
        self.gb_SeleccionTerapias.setObjectName("gb_SeleccionTerapias")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gb_SeleccionTerapias)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lb_Ejercicio_3 = QtWidgets.QLabel(self.gb_SeleccionTerapias)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_Ejercicio_3.setFont(font)
        self.lb_Ejercicio_3.setObjectName("lb_Ejercicio_3")
        self.gridLayout_7.addWidget(self.lb_Ejercicio_3, 7, 0, 1, 1)
        self.btn_SaveDataOfTerhapy = QtWidgets.QPushButton(self.gb_SeleccionTerapias)
        self.btn_SaveDataOfTerhapy.setMinimumSize(QtCore.QSize(131, 81))
        self.btn_SaveDataOfTerhapy.setMaximumSize(QtCore.QSize(131, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_SaveDataOfTerhapy.setFont(font)
        self.btn_SaveDataOfTerhapy.setStyleSheet("background-color:rgb(255, 163, 35)")
        self.btn_SaveDataOfTerhapy.setIcon(icon8)
        self.btn_SaveDataOfTerhapy.setObjectName("btn_SaveDataOfTerhapy")
        self.gridLayout_7.addWidget(self.btn_SaveDataOfTerhapy, 10, 0, 1, 1)
        self.lb_Ejercicio_2 = QtWidgets.QLabel(self.gb_SeleccionTerapias)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_Ejercicio_2.setFont(font)
        self.lb_Ejercicio_2.setObjectName("lb_Ejercicio_2")
        self.gridLayout_7.addWidget(self.lb_Ejercicio_2, 5, 0, 1, 1)
        self.cb_Ejercicio_1 = QtWidgets.QComboBox(self.gb_SeleccionTerapias)
        self.cb_Ejercicio_1.setMinimumSize(QtCore.QSize(421, 18))
        self.cb_Ejercicio_1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_Ejercicio_1.setObjectName("cb_Ejercicio_1")
        self.gridLayout_7.addWidget(self.cb_Ejercicio_1, 4, 0, 1, 1)
        self.cb_Ejercicio_3 = QtWidgets.QComboBox(self.gb_SeleccionTerapias)
        self.cb_Ejercicio_3.setMinimumSize(QtCore.QSize(421, 20))
        self.cb_Ejercicio_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_Ejercicio_3.setObjectName("cb_Ejercicio_3")
        self.gridLayout_7.addWidget(self.cb_Ejercicio_3, 8, 0, 1, 1)
        self.lb_Ejercicio_1 = QtWidgets.QLabel(self.gb_SeleccionTerapias)
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_Ejercicio_1.setFont(font)
        self.lb_Ejercicio_1.setObjectName("lb_Ejercicio_1")
        self.gridLayout_7.addWidget(self.lb_Ejercicio_1, 3, 0, 1, 1)
        self.cb_Ejercicio_2 = QtWidgets.QComboBox(self.gb_SeleccionTerapias)
        self.cb_Ejercicio_2.setMinimumSize(QtCore.QSize(421, 20))
        self.cb_Ejercicio_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_Ejercicio_2.setObjectName("cb_Ejercicio_2")
        self.gridLayout_7.addWidget(self.cb_Ejercicio_2, 6, 0, 1, 1)
        self.l_PacienteInSelection = QtWidgets.QLabel(self.gb_SeleccionTerapias)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.l_PacienteInSelection.setFont(font)
        self.l_PacienteInSelection.setObjectName("l_PacienteInSelection")
        self.gridLayout_7.addWidget(self.l_PacienteInSelection, 0, 0, 1, 1)
        self.lb_contador = QtWidgets.QLabel(self.gb_SeleccionTerapias)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lb_contador.setFont(font)
        self.lb_contador.setObjectName("lb_contador")
        self.gridLayout_7.addWidget(self.lb_contador, 2, 0, 1, 1)
        self.cb_SeleccionPaciente = QtWidgets.QComboBox(self.gb_SeleccionTerapias)
        self.cb_SeleccionPaciente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cb_SeleccionPaciente.setObjectName("cb_SeleccionPaciente")
        self.gridLayout_7.addWidget(self.cb_SeleccionPaciente, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem5, 9, 0, 1, 1)
        self.gridLayout.addWidget(self.gb_SeleccionTerapias, 0, 2, 1, 1)
        self.stackedWidget.addWidget(self.page_Pacientes)
        self.page_Interfaz_de_Terapia = QtWidgets.QWidget()
        self.page_Interfaz_de_Terapia.setObjectName("page_Interfaz_de_Terapia")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_Interfaz_de_Terapia)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.page_Interfaz_de_Terapia)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gb_ConectionWithHead = QtWidgets.QGroupBox(self.groupBox)
        self.gb_ConectionWithHead.setMaximumSize(QtCore.QSize(16777215, 138))
        self.gb_ConectionWithHead.setObjectName("gb_ConectionWithHead")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gb_ConectionWithHead)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.cb_Puertos = QtWidgets.QComboBox(self.gb_ConectionWithHead)
        self.cb_Puertos.setObjectName("cb_Puertos")
        self.gridLayout_3.addWidget(self.cb_Puertos, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gb_ConectionWithHead)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gb_ConectionWithHead)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)
        self.cb_Baudios = QtWidgets.QComboBox(self.gb_ConectionWithHead)
        self.cb_Baudios.setObjectName("cb_Baudios")
        self.gridLayout_3.addWidget(self.cb_Baudios, 2, 2, 1, 1)
        self.btn_Conectar = QtWidgets.QPushButton(self.gb_ConectionWithHead)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/hexagon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_Conectar.setIcon(icon9)
        self.btn_Conectar.setObjectName("btn_Conectar")
        self.gridLayout_3.addWidget(self.btn_Conectar, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.gb_ConectionWithHead)
        self.gb_Vision = QtWidgets.QGroupBox(self.groupBox)
        self.gb_Vision.setObjectName("gb_Vision")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.gb_Vision)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lb_VideoSkeleto = QtWidgets.QLabel(self.gb_Vision)
        self.lb_VideoSkeleto.setStyleSheet("background-color: rgb(176, 195, 255);")
        self.lb_VideoSkeleto.setText("")
        self.lb_VideoSkeleto.setScaledContents(True)
        self.lb_VideoSkeleto.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lb_VideoSkeleto.setObjectName("lb_VideoSkeleto")
        self.horizontalLayout_4.addWidget(self.lb_VideoSkeleto)
        self.lb_Video = QtWidgets.QLabel(self.gb_Vision)
        self.lb_Video.setEnabled(True)
        self.lb_Video.setStyleSheet("background-color: rgb(255, 195, 255);")
        self.lb_Video.setText("")
        self.lb_Video.setScaledContents(True)
        self.lb_Video.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lb_Video.setObjectName("lb_Video")
        self.horizontalLayout_4.addWidget(self.lb_Video)
        self.verticalLayout.addWidget(self.gb_Vision)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 138))
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.rb_both = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_both.setObjectName("rb_both")
        self.gridLayout_4.addWidget(self.rb_both, 1, 2, 1, 1)
        self.btn_Encender = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_Encender.setFont(font)
        self.btn_Encender.setStyleSheet("background-color: rgb(56, 206, 22);")
        self.btn_Encender.setObjectName("btn_Encender")
        self.gridLayout_4.addWidget(self.btn_Encender, 0, 0, 1, 1)
        self.rb_Emociones = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_Emociones.setObjectName("rb_Emociones")
        self.gridLayout_4.addWidget(self.rb_Emociones, 1, 0, 1, 1)
        self.rb_Skeleto = QtWidgets.QRadioButton(self.groupBox_2)
        self.rb_Skeleto.setObjectName("rb_Skeleto")
        self.gridLayout_4.addWidget(self.rb_Skeleto, 1, 1, 1, 1)
        self.btn_Apagar = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_Apagar.setFont(font)
        self.btn_Apagar.setStyleSheet("background-color: rgb(220, 74, 38);")
        self.btn_Apagar.setObjectName("btn_Apagar")
        self.gridLayout_4.addWidget(self.btn_Apagar, 0, 2, 1, 1)
        self.lb_StateVideo = QtWidgets.QLabel(self.groupBox_2)
        self.lb_StateVideo.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_StateVideo.setObjectName("lb_StateVideo")
        self.gridLayout_4.addWidget(self.lb_StateVideo, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.horizontalLayout_3.addWidget(self.groupBox)
        self.gb_Workout = QtWidgets.QGroupBox(self.page_Interfaz_de_Terapia)
        self.gb_Workout.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.gb_Workout.setFont(font)
        self.gb_Workout.setTitle("")
        self.gb_Workout.setObjectName("gb_Workout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.gb_Workout)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lb_games = QtWidgets.QLabel(self.gb_Workout)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(18)
        self.lb_games.setFont(font)
        self.lb_games.setObjectName("lb_games")
        self.verticalLayout_5.addWidget(self.lb_games)
        self.groupBox_3 = QtWidgets.QGroupBox(self.gb_Workout)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lb_Voice = QtWidgets.QLabel(self.groupBox_3)
        self.lb_Voice.setEnabled(True)
        self.lb_Voice.setStyleSheet("")
        self.lb_Voice.setText("")
        self.lb_Voice.setPixmap(QtGui.QPixmap("states/slee.png"))
        self.lb_Voice.setObjectName("lb_Voice")
        self.gridLayout_5.addWidget(self.lb_Voice, 0, 0, 1, 2)
        self.btn_PlayWorkout = QtWidgets.QPushButton(self.groupBox_3)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_PlayWorkout.setIcon(icon10)
        self.btn_PlayWorkout.setIconSize(QtCore.QSize(16, 16))
        self.btn_PlayWorkout.setObjectName("btn_PlayWorkout")
        self.gridLayout_5.addWidget(self.btn_PlayWorkout, 1, 0, 1, 1)
        self.btn_StopWorkout = QtWidgets.QPushButton(self.groupBox_3)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/stop-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_StopWorkout.setIcon(icon11)
        self.btn_StopWorkout.setObjectName("btn_StopWorkout")
        self.gridLayout_5.addWidget(self.btn_StopWorkout, 1, 1, 1, 1)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.gb_Workout)
        self.groupBox_4.setMinimumSize(QtCore.QSize(380, 358))
        self.groupBox_4.setMaximumSize(QtCore.QSize(380, 358))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setStyleSheet("background-color: rgb(226, 199, 90);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.horizontalLayout_3.addWidget(self.gb_Workout)
        self.stackedWidget.addWidget(self.page_Interfaz_de_Terapia)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.frameContenedor)
        self.gridLayout_2.addWidget(self.frameInferior, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_Menu.setText(_translate("MainWindow", "  MENU"))
        self.btn_Inicio.setText(_translate("MainWindow", "  Inicio"))
        self.btn_Pacientes.setText(_translate("MainWindow", "  Pacientes"))
        self.btn_Terapias.setText(_translate("MainWindow", "  Terapias"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">S.T.A.R </p><p align=\"center\">S.A de C.V</p></body></html>"))
        self.btn_CrearPaciente.setText(_translate("MainWindow", "Crear Paciente"))
        self.btn_CrearPaciente_4.setText(_translate("MainWindow", "Seleccionar Paciente"))
        self.btn_CrearPaciente_2.setText(_translate("MainWindow", "Modificar Paciente"))
        self.btn_CrearPaciente_3.setText(_translate("MainWindow", "Eliminar Paciente"))
        self.gb_RegistroUsuario.setTitle(_translate("MainWindow", "Registro de Usuarios"))
        self.lb_Contacto.setText(_translate("MainWindow", "Contacto:"))
        self.lb_LastNameMother.setText(_translate("MainWindow", "Apellido Materno:"))
        self.lb_Tutor.setText(_translate("MainWindow", "Tutor Responsable:"))
        self.lb_Edad.setText(_translate("MainWindow", "Edad:"))
        self.lb_Grade_Of_TEA.setText(_translate("MainWindow", "<html><head/><body><p>Grado de TEA:</p></body></html>"))
        self.lb_LastNameFater.setText(_translate("MainWindow", "Apellido Paterno:"))
        self.lb_Name.setText(_translate("MainWindow", "Nombre:"))
        self.btn_SaveDataOfUser.setText(_translate("MainWindow", "Guardar Datos"))
        self.gb_SeleccionTerapias.setTitle(_translate("MainWindow", "Selección de Terapias"))
        self.lb_Ejercicio_3.setText(_translate("MainWindow", "Ejercicio #3:"))
        self.btn_SaveDataOfTerhapy.setText(_translate("MainWindow", "Guardar \n"
"Terapias"))
        self.lb_Ejercicio_2.setText(_translate("MainWindow", "Ejercicio #2:"))
        self.lb_Ejercicio_1.setText(_translate("MainWindow", "Ejercicio #1:"))
        self.l_PacienteInSelection.setText(_translate("MainWindow", "Paciente:"))
        self.lb_contador.setText(_translate("MainWindow", "Elige tres ejercicios que mejor se adapten a tu terapia"))
        self.gb_ConectionWithHead.setTitle(_translate("MainWindow", "CONNECTION WITH STAR"))
        self.label_2.setText(_translate("MainWindow", "Puerto"))
        self.label_3.setText(_translate("MainWindow", "Baudios"))
        self.btn_Conectar.setText(_translate("MainWindow", "Conectar"))
        self.gb_Vision.setTitle(_translate("MainWindow", "Vision"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Controles de Video"))
        self.rb_both.setText(_translate("MainWindow", "Video Normal"))
        self.btn_Encender.setText(_translate("MainWindow", "Turn On"))
        self.rb_Emociones.setText(_translate("MainWindow", "Activar Reconocimientos\n"
"de Emociones"))
        self.rb_Skeleto.setText(_translate("MainWindow", "Activar Esqueleto"))
        self.btn_Apagar.setText(_translate("MainWindow", "Turn Off"))
        self.lb_StateVideo.setText(_translate("MainWindow", "State of Video"))
        self.lb_games.setText(_translate("MainWindow", "¡¡¡MUY BIEN LO LOGRASTE!!!"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Voice"))
        self.btn_PlayWorkout.setText(_translate("MainWindow", "Play"))
        self.btn_StopWorkout.setText(_translate("MainWindow", "Stop"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Emocion Detectada"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
