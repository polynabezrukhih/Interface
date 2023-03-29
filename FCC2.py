# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FCC.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1400, 1050)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interface_project/img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(10)
        MainWindow.setToolTipDuration(0)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(2, 0, 1391, 961))
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_reactor = QtWidgets.QWidget()
        self.tab_reactor.setObjectName("tab_reactor")
        self.label = QtWidgets.QLabel(self.tab_reactor)
        self.label.setGeometry(QtCore.QRect(880, 90, 370, 720))
        self.label.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Interface_project/img/схема-1.jpg"))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_reactor, "")
        self.tab_rectic = QtWidgets.QWidget()
        self.tab_rectic.setObjectName("tab_rectic")
        self.label_2 = QtWidgets.QLabel(self.tab_rectic)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 331, 661))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Interface_project/img/ректификация.jpg"))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_rectic, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1400, 21))
        self.menubar.setObjectName("menubar")
        self.bar_input = QtWidgets.QMenu(self.menubar)
        self.bar_input.setObjectName("bar_input")
        self.bar_input_2 = QtWidgets.QMenu(self.bar_input)
        self.bar_input_2.setObjectName("bar_input_2")
        self.bar_rezhim = QtWidgets.QMenu(self.bar_input_2)
        self.bar_rezhim.setObjectName("bar_rezhim")
        self.bar_catal = QtWidgets.QMenu(self.bar_input_2)
        self.bar_catal.setObjectName("bar_catal")
        self.bar_reactor = QtWidgets.QMenu(self.bar_input_2)
        self.bar_reactor.setObjectName("bar_reactor")
        self.bar_feed = QtWidgets.QMenu(self.bar_input_2)
        self.bar_feed.setObjectName("bar_feed")
        self.bar_file = QtWidgets.QMenu(self.menubar)
        self.bar_file.setObjectName("bar_file")
        self.bar_calc = QtWidgets.QMenu(self.menubar)
        self.bar_calc.setObjectName("bar_calc")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Excel = QtWidgets.QAction(MainWindow)
        self.action_Excel.setObjectName("action_Excel")
        self.action_extra = QtWidgets.QAction(MainWindow)
        self.action_extra.setObjectName("action_extra")
        self.action_clean = QtWidgets.QAction(MainWindow)
        self.action_clean.setObjectName("action_clean")
        self.action_create_rezh = QtWidgets.QAction(MainWindow)
        self.action_create_rezh.setObjectName("action_create_rezh")
        self.action_edit_rezh = QtWidgets.QAction(MainWindow)
        self.action_edit_rezh.setObjectName("action_edit_rezh")
        self.action_open_rezh = QtWidgets.QAction(MainWindow)
        self.action_open_rezh.setObjectName("action_open_rezh")
        self.action_create_catal = QtWidgets.QAction(MainWindow)
        self.action_create_catal.setObjectName("action_create_catal")
        self.action_edit_catal = QtWidgets.QAction(MainWindow)
        self.action_edit_catal.setObjectName("action_edit_catal")
        self.action_open_catal = QtWidgets.QAction(MainWindow)
        self.action_open_catal.setObjectName("action_open_catal")
        self.action_create_reactor = QtWidgets.QAction(MainWindow)
        self.action_create_reactor.setObjectName("action_create_reactor")
        self.action_edit_reactor = QtWidgets.QAction(MainWindow)
        self.action_edit_reactor.setObjectName("action_edit_reactor")
        self.action_save_reactor = QtWidgets.QAction(MainWindow)
        self.action_save_reactor.setObjectName("action_save_reactor")
        self.action_save_feed = QtWidgets.QAction(MainWindow)
        self.action_save_feed.setObjectName("action_save_feed")
        self.action_edit_feed = QtWidgets.QAction(MainWindow)
        self.action_edit_feed.setObjectName("action_edit_feed")
        self.action_save_adit = QtWidgets.QAction(MainWindow)
        self.action_save_adit.setObjectName("action_save_adit")
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName("action_save")
        self.action_delete = QtWidgets.QAction(MainWindow)
        self.action_delete.setObjectName("action_delete")
        self.action_save_as = QtWidgets.QAction(MainWindow)
        self.action_save_as.setObjectName("action_save_as")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.action_find_reactor = QtWidgets.QAction(MainWindow)
        self.action_find_reactor.setObjectName("action_find_reactor")
        self.bar_rezhim.addAction(self.action_create_rezh)
        self.bar_rezhim.addAction(self.action_edit_rezh)
        self.bar_rezhim.addAction(self.action_open_rezh)
        self.bar_catal.addAction(self.action_create_catal)
        self.bar_catal.addAction(self.action_edit_catal)
        self.bar_catal.addAction(self.action_open_catal)
        self.bar_reactor.addAction(self.action_create_reactor)
        self.bar_reactor.addAction(self.action_edit_reactor)
        self.bar_reactor.addAction(self.action_save_reactor)
        self.bar_reactor.addAction(self.action_find_reactor)
        self.bar_feed.addAction(self.action_save_feed)
        self.bar_feed.addAction(self.action_edit_feed)
        self.bar_feed.addAction(self.action_save_adit)
        self.bar_input_2.addAction(self.bar_rezhim.menuAction())
        self.bar_input_2.addAction(self.bar_catal.menuAction())
        self.bar_input_2.addAction(self.bar_reactor.menuAction())
        self.bar_input_2.addAction(self.bar_feed.menuAction())
        self.bar_input.addAction(self.bar_input_2.menuAction())
        self.bar_input.addAction(self.action_Excel)
        self.bar_input.addAction(self.action_extra)
        self.bar_input.addAction(self.action_clean)
        self.bar_file.addAction(self.action_save)
        self.bar_file.addAction(self.action_save_as)
        self.bar_file.addAction(self.action_delete)
        self.bar_file.addSeparator()
        self.bar_file.addAction(self.action_exit)
        self.menubar.addAction(self.bar_file.menuAction())
        self.menubar.addAction(self.bar_input.menuAction())
        self.menubar.addAction(self.bar_calc.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Каталитический крекинг"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_reactor), _translate("MainWindow", "Реактор"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_rectic), _translate("MainWindow", "Ректификация"))
        self.bar_input.setTitle(_translate("MainWindow", "Ввод данных"))
        self.bar_input_2.setTitle(_translate("MainWindow", "Ввод данных"))
        self.bar_rezhim.setTitle(_translate("MainWindow", "Режим"))
        self.bar_catal.setTitle(_translate("MainWindow", "Катализатор"))
        self.bar_reactor.setTitle(_translate("MainWindow", "Реактор"))
        self.bar_feed.setTitle(_translate("MainWindow", "Сырье"))
        self.bar_file.setTitle(_translate("MainWindow", "Файл"))
        self.bar_calc.setTitle(_translate("MainWindow", "Расчет"))
        self.action_Excel.setText(_translate("MainWindow", "Чтение данных с Excel"))
        self.action_extra.setText(_translate("MainWindow", "Дополнительно"))
        self.action_clean.setText(_translate("MainWindow", "Очистить"))
        self.action_create_rezh.setText(_translate("MainWindow", "Создать"))
        self.action_edit_rezh.setText(_translate("MainWindow", "Редактировать"))
        self.action_open_rezh.setText(_translate("MainWindow", "Открыть"))
        self.action_create_catal.setText(_translate("MainWindow", "Создать"))
        self.action_edit_catal.setText(_translate("MainWindow", "Редактировать"))
        self.action_open_catal.setText(_translate("MainWindow", "Открыть"))
        self.action_create_reactor.setText(_translate("MainWindow", "Создать"))
        self.action_edit_reactor.setText(_translate("MainWindow", "Редактировать"))
        self.action_save_reactor.setText(_translate("MainWindow", "Сохранить"))
        self.action_save_feed.setText(_translate("MainWindow", "Создать"))
        self.action_edit_feed.setText(_translate("MainWindow", "Редактировать"))
        self.action_save_adit.setText(_translate("MainWindow", "Сохранить"))
        self.action_save.setText(_translate("MainWindow", "Сохранить"))
        self.action_delete.setText(_translate("MainWindow", "Удалить"))
        self.action_save_as.setText(_translate("MainWindow", "Сохранить как..."))
        self.action_exit.setText(_translate("MainWindow", "Выйти"))
        self.action_find_reactor.setText(_translate("MainWindow", "Выбрать"))

        def push_btm(btm):
            if btm == action_create_rezh or action_create_rezh or action_open_rezh:
                rezh.show()
            ifelse btm ==

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
