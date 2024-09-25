# coding:utf-8
import sys
import configparser

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QSplashScreen, QDesktopWidget
from qfluentwidgets import SplitFluentWindow, FluentIcon, NavigationItemPosition, setTheme, Theme

from AttendanceInterface import AttendanceInterface
from SettingInterface import SettingInterface
from utils.ConfigSetting import ConfigSetting


class ToolBox(SplitFluentWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('工具箱')
        self.setWindowIcon(QIcon('img/logo.png'))

        # 设置默认大小
        self.resize(800, 800)

        # 调整窗口在屏幕中央显示
        center_pointer = QDesktopWidget().availableGeometry().center()
        x = center_pointer.x()
        y = center_pointer.y()
        old_x, oldy, width, height = self.frameGeometry().getRect()
        self.move(int(x - width / 2), int(y - height / 2))

        # 添加考勤子界面
        self.AttendanceInterface = AttendanceInterface(self)
        self.addSubInterface(self.AttendanceInterface, FluentIcon.CAFE, '考勤')

        # 添加设置子界面
        self.SettingInterface = SettingInterface(self)
        self.addSubInterface(self.SettingInterface, FluentIcon.SETTING, '设置', NavigationItemPosition.BOTTOM)


if __name__ == '__main__':

    # 读取配置文件
    conf = ConfigSetting()
    theme = conf.get( 'theme')
    showSplash = conf.get('splash')

    # 启用高分屏
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    # 设置主题
    if theme == '0':
        setTheme(Theme.AUTO)
    elif theme == '1':
        setTheme(Theme.LIGHT)
    elif theme == '2':
        setTheme(Theme.DARK)

    app = QApplication(sys.argv)

    splash = QSplashScreen()
    splash.setPixmap(QPixmap(r'img/splash.jpg'))
    if showSplash == '1':
        splash.show()

    ex = ToolBox()
    ex.show()
    splash.finish(ex)  # 主界面加载完成后隐藏
    splash.deleteLater()
    sys.exit(app.exec_())
