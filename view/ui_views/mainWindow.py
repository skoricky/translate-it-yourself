# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from os.path import join, abspath


ICONS_PATH = abspath(".\\view\\ui_views\\icons")
SAVE_ICON = "save_ico.png"
EXIT_ICON = "exit_ico.png"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(873, 759)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saveToolButton = QtWidgets.QToolButton(self.centralwidget)
        icon = QtGui.QIcon(join(ICONS_PATH, SAVE_ICON))
        self.saveToolButton.setIcon(icon)
        self.saveToolButton.setIconSize(QtCore.QSize(20, 20))
        self.saveToolButton.setObjectName("saveToolButton")
        self.horizontalLayout_4.addWidget(self.saveToolButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.exitToolButton = QtWidgets.QToolButton(self.centralwidget)
        icon1 = QtGui.QIcon(QtGui.QIcon(join(ICONS_PATH, EXIT_ICON)))
        self.exitToolButton.setIcon(icon1)
        self.exitToolButton.setIconSize(QtCore.QSize(20, 20))
        self.exitToolButton.setObjectName("exitToolButton")
        self.horizontalLayout_4.addWidget(self.exitToolButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 0, 0, 1, 2)
        self.originalPartWidget = QtWidgets.QWidget(self.centralwidget)
        self.originalPartWidget.setObjectName("originalPartWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.originalPartWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.originalListWidget = QtWidgets.QListWidget(self.originalPartWidget)
        self.originalListWidget.setMinimumSize(QtCore.QSize(200, 200))
        self.originalListWidget.setMaximumSize(QtCore.QSize(925, 10000000))
        self.originalListWidget.setWordWrap(True)
        self.originalListWidget.setObjectName("originalListWidget")
        self.gridLayout.addWidget(self.originalListWidget, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.originalPartWidget, 1, 0, 1, 1)
        self.translatedPartStackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.translatedPartStackedWidget.setSizeIncrement(QtCore.QSize(2, 0))
        self.translatedPartStackedWidget.setObjectName("translatedPartStackedWidget")
        self.listPage = QtWidgets.QWidget()
        self.listPage.setMinimumSize(QtCore.QSize(200, 200))
        self.listPage.setObjectName("listPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.listPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.translatedListWidget = QtWidgets.QListWidget(self.listPage)
        self.translatedListWidget.setMinimumSize(QtCore.QSize(200, 200))
        self.translatedListWidget.setMaximumSize(QtCore.QSize(925, 16777215))
        self.translatedListWidget.setWordWrap(True)
        self.translatedListWidget.setObjectName("translatedListWidget")
        self.gridLayout_2.addWidget(self.translatedListWidget, 0, 0, 1, 1)
        self.translatedPartStackedWidget.addWidget(self.listPage)
        self.editorPage = QtWidgets.QWidget()
        self.editorPage.setObjectName("editorPage")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.editorPage)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.saveBlockPushButton = QtWidgets.QPushButton(self.editorPage)
        self.saveBlockPushButton.setObjectName("saveBlockPushButton")
        self.horizontalLayout_3.addWidget(self.saveBlockPushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.translateApiPushButton = QtWidgets.QPushButton(self.editorPage)
        self.translateApiPushButton.setObjectName("translateApiPushButton")
        self.horizontalLayout_2.addWidget(self.translateApiPushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.originalTextEdit = QtWidgets.QTextEdit(self.editorPage)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.originalTextEdit.setFont(font)
        self.originalTextEdit.setReadOnly(True)
        self.originalTextEdit.setObjectName("originalTextEdit")
        self.gridLayout_3.addWidget(self.originalTextEdit, 1, 0, 1, 1)
        self.translatedTextEdit = QtWidgets.QTextEdit(self.editorPage)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.translatedTextEdit.setFont(font)
        self.translatedTextEdit.setObjectName("translatedTextEdit")
        self.gridLayout_3.addWidget(self.translatedTextEdit, 2, 0, 1, 1)
        self.translatedPartStackedWidget.addWidget(self.editorPage)
        self.gridLayout_4.addWidget(self.translatedPartStackedWidget, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.workWithBlockPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.workWithBlockPushButton.setObjectName("workWithBlockPushButton")
        self.horizontalLayout.addWidget(self.workWithBlockPushButton)
        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 873, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.createTrigger = QtWidgets.QAction(MainWindow)
        self.createTrigger.setObjectName("createTrigger")
        self.openTrigger = QtWidgets.QAction(MainWindow)
        self.openTrigger.setObjectName("openTrigger")
        self.saveTrigger = QtWidgets.QAction(MainWindow)
        self.saveTrigger.setObjectName("saveTrigger")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.exitTrigger = QtWidgets.QAction(MainWindow)
        self.exitTrigger.setObjectName("exitTrigger")
        self.exportTxtTrigger = QtWidgets.QAction(MainWindow)
        self.exportTxtTrigger.setObjectName("exportTxtTrigger")
        self.actionPDF = QtWidgets.QAction(MainWindow)
        self.actionPDF.setObjectName("actionPDF")
        self.exportPdfTrigger = QtWidgets.QAction(MainWindow)
        self.exportPdfTrigger.setObjectName("exportPdfTrigger")
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.exportTxtTrigger)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.exportPdfTrigger)
        self.menu.addAction(self.createTrigger)
        self.menu.addSeparator()
        self.menu.addAction(self.openTrigger)
        self.menu.addSeparator()
        self.menu.addAction(self.saveTrigger)
        self.menu.addSeparator()
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.exitTrigger)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.translatedPartStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.saveToolButton.setText(_translate("MainWindow", "..."))
        self.exitToolButton.setText(_translate("MainWindow", "..."))
        self.saveBlockPushButton.setText(_translate("MainWindow", "Сохранить блок"))
        self.translateApiPushButton.setText(_translate("MainWindow", "Перевести"))
        self.workWithBlockPushButton.setText(_translate("MainWindow", "Перевести блок"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.menu_2.setTitle(_translate("MainWindow", "Экспорт"))
        self.createTrigger.setText(_translate("MainWindow", "Новый Проект"))
        self.openTrigger.setText(_translate("MainWindow", "Открыть"))
        self.saveTrigger.setText(_translate("MainWindow", "Сохранить"))
        self.action.setText(_translate("MainWindow", "Выход"))
        self.exitTrigger.setText(_translate("MainWindow", "Выход"))
        self.exportTxtTrigger.setText(_translate("MainWindow", "TXT"))
        self.actionPDF.setText(_translate("MainWindow", "PDF"))
        self.exportPdfTrigger.setText(_translate("MainWindow", "PDF"))
