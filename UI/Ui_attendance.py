# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_attendance.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(738, 815)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(16, 46, 16, 16)
        self.verticalLayout_4.setSpacing(16)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 101))
        self.widget.setObjectName("widget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 241, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.select = PushButton(self.gridLayoutWidget)
        self.select.setObjectName("select")
        self.gridLayout.addWidget(self.select, 1, 1, 1, 1)
        self.comboBox = ComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.id = LineEdit(self.gridLayoutWidget)
        self.id.setObjectName("id")
        self.gridLayout.addWidget(self.id, 0, 0, 1, 1)
        self.formLayoutWidget = QtWidgets.QWidget(self.widget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(380, 10, 301, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.startTime = TimePicker(self.formLayoutWidget)
        self.startTime.setText("")
        self.startTime.setObjectName("startTime")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.startTime)
        self.label = PixmapLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = PixmapLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(False)
        self.label.setFont(font)
        self.label_2.setFont(font)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.endTime = TimePicker(self.formLayoutWidget)
        self.endTime.setText("")
        self.endTime.setObjectName("endTime")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.endTime)
        self.verticalLayout_4.addWidget(self.widget)
        self.ScrollArea = ScrollArea(Form)
        self.ScrollArea.setMaximumSize(QtCore.QSize(16777215, 618))
        self.ScrollArea.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.ScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ScrollArea.setWidgetResizable(True)
        self.ScrollArea.setObjectName("ScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 700, 601))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(700, 530))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableView = TableWidget(self.scrollAreaWidgetContents)
        self.tableView.setGeometry(QtCore.QRect(10, 0, 571, 601))
        self.tableView.setObjectName("tableView")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(610, 0, 71, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.late = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.late.setObjectName("late")
        self.verticalLayout.addWidget(self.late)
        self.workOver = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.workOver.setObjectName("workOver")
        self.verticalLayout.addWidget(self.workOver)
        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.ScrollArea)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.select.setText(_translate("Form", "查询"))
        self.comboBox.setText(_translate("Form", "日期范围"))
        self.label.setText(_translate("Form", "上班时间:"))
        self.label_2.setText(_translate("Form", "下班时间:"))
        self.late.setText(_translate("Form", "迟到"))
        self.workOver.setText(_translate("Form", "加班"))
from qfluentwidgets import ComboBox, LineEdit, PixmapLabel, PushButton, ScrollArea, TableWidget, TimePicker
