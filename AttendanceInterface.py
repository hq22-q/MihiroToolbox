# coding:utf-8
import configparser

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QWidget
from qfluentwidgets import InfoBarIcon, InfoBar, PushButton, setTheme, Theme, FluentIcon, InfoBarPosition, \
    InfoBarManager, ComboBox

from UI.UI_attendance import Ui_Form


class AttendanceInterface(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # 选择主题

        conf = configparser.ConfigParser()
        conf.read('config.ini')
        theme = conf.get('DEFAULT', 'theme')

        comboBox = ComboBox()

        # 添加选项
        items = ['shoko', '西宫硝子', '宝多六花', '小鸟游六花']
        self.pushButton.addItems(items)

        # 当前选项的索引改变信号
        self.pushButton.currentIndexChanged.connect(lambda index: print(comboBox.currentText()))

