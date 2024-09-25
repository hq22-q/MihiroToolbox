# coding:utf-8
import configparser

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QWidget
from qfluentwidgets import InfoBarIcon, InfoBar, PushButton, setTheme, Theme, FluentIcon, InfoBarPosition, \
    InfoBarManager

from UI.Ui_setting import Ui_setting
from utils.ConfigSetting import ConfigSetting


class SettingInterface(QWidget, Ui_setting):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # 选择主题

        conf = ConfigSetting()
        theme = conf.get( 'theme')

        self.ThemeBox.addItem('跟随系统')
        self.ThemeBox.addItem('浅色')
        self.ThemeBox.addItem('深色')

        self.ThemeBox.setCurrentIndex(int(theme))
        self.ThemeBox.currentIndexChanged.connect(self.ThemeBoxChanged)
        # self.LaunchCheck.setVisible(False)
        # 关闭开屏画面
        splash = conf.get('splash')
        self.LaunchCheck.setChecked(bool(int(splash)))
        self.LaunchCheck.clicked.connect(self.LaunchCheckClicked)

    # 选择主题
    def ThemeBoxChanged(self):
        conf = ConfigSetting()
        conf.set('theme', str(self.ThemeBox.currentIndex()))
        theme  = str(self.ThemeBox.currentIndex())
        # 设置主题
        if theme == '0':
            setTheme(Theme.AUTO)
        elif theme == '1':
            setTheme(Theme.LIGHT)
        elif theme == '2':
            setTheme(Theme.DARK)


    # 关闭开屏画面
    def LaunchCheckClicked(self):
        conf = ConfigSetting()
        conf.set('splash', str(int(self.LaunchCheck.isChecked())))
