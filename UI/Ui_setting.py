# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(855, 729)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(16, 46, 16, 16)
        self.verticalLayout_4.setSpacing(16)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.VideoTitile = LargeTitleLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VideoTitile.sizePolicy().hasHeightForWidth())
        self.VideoTitile.setSizePolicy(sizePolicy)
        self.VideoTitile.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.VideoTitile.setFont(font)
        self.VideoTitile.setObjectName("VideoTitile")
        self.verticalLayout_4.addWidget(self.VideoTitile)
        self.ScrollArea = ScrollArea(Form)
        self.ScrollArea.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.ScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ScrollArea.setWidgetResizable(True)
        self.ScrollArea.setObjectName("ScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 805, 588))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(700, 530))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(0, -5, 711, 104))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.FileTitle = SubtitleLabel(self.layoutWidget)
        self.FileTitle.setMinimumSize(QtCore.QSize(0, 30))
        self.FileTitle.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.FileTitle.setFont(font)
        self.FileTitle.setObjectName("FileTitle")
        self.verticalLayout.addWidget(self.FileTitle)
        self.SimpleCardWidget = SimpleCardWidget(self.layoutWidget)
        self.SimpleCardWidget.setObjectName("SimpleCardWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.SimpleCardWidget)
        self.horizontalLayout_2.setContentsMargins(25, 16, 16, 16)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LaunchCheck = CheckBox(self.SimpleCardWidget)
        self.LaunchCheck.setChecked(True)
        self.LaunchCheck.setObjectName("LaunchCheck")
        self.horizontalLayout_2.addWidget(self.LaunchCheck, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inputLabel = BodyLabel(self.SimpleCardWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.inputLabel.setFont(font)
        self.inputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.inputLabel.setObjectName("inputLabel")
        self.horizontalLayout.addWidget(self.inputLabel)
        self.ThemeBox = ComboBox(self.SimpleCardWidget)
        self.ThemeBox.setObjectName("ThemeBox")
        self.horizontalLayout.addWidget(self.ThemeBox)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.SimpleCardWidget)
        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.ScrollArea)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.VideoTitile.setText(_translate("Form", "设置"))
        self.FileTitle.setText(_translate("Form", "界面设置"))
        self.LaunchCheck.setText(_translate("Form", "显示启动画面"))
        self.inputLabel.setText(_translate("Form", "程序主题"))
from qfluentwidgets import BodyLabel, CheckBox, ComboBox, LargeTitleLabel, ScrollArea, SimpleCardWidget, SubtitleLabel
