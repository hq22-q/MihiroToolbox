# coding:utf-8
import configparser

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from qfluentwidgets import InfoBarIcon, InfoBar, PushButton, setTheme, Theme, FluentIcon, InfoBarPosition, \
    InfoBarManager, ComboBox

from UI.Ui_attendance import Ui_Form




class AttendanceInterface(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        comboBox = self.comboBox
        # 添加选项
        items = ['A', 'B', 'C', 'D']
        comboBox.addItems(items)

        # 当前选项的索引改变信号
        comboBox.currentIndexChanged.connect(lambda index: print(comboBox.currentText()))
        button = self.select
        button.clicked.connect(select)

        table = self.tableView

        # 启用边框并设置圆角
        table.setBorderVisible(True)
        table.setBorderRadius(8)

        table.setWordWrap(False)
        table.setRowCount(3)
        table.setColumnCount(5)

        # 添加表格数据
        songInfos = [
            ['a', 'aiko', '1', '2008', '5:25'],
            ['b', 'RADWIMPS', '2。', '2016', '3:16'],
            ['c', 'aiko', '3', '2016', '6:02'],
        ]
        for i, songInfo in enumerate(songInfos):
            for j in range(5):
                table.setItem(i, j, QTableWidgetItem(songInfo[j]))

        # 设置水平表头并隐藏垂直表头
        table.setHorizontalHeaderLabels(['Title', 'Artist', 'Album', 'Year', 'Duration'])
        table.verticalHeader().hide()


def select():
    print("Select")