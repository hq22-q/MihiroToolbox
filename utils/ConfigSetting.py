import os
import sys

import PyQt5.QtCore as qc

import utils.FileHandler


class ConfigSetting:
    def __init__(self):
        self.file = utils.FileHandler.getPackagePath('../res/toolbox.ini')
        self.settings = qc.QSettings(self.file, qc.QSettings.IniFormat)
        self.settings.setIniCodec("UTF8")

        # 检查是否有数据进行初始化
        if not os.path.exists(self.file):
            self.init_info()

    def set(self, key, value):
        self.settings.setValue(key, value)

    def get(self, key):
        return self.settings.value(key)



    def init_info(self):
        self.settings.setValue("theme", 1)
        self.settings.setValue("splash", 1)
        self.settings.setValue("id", "")

def getExePath():
    sap = '/'
    if sys.argv[0].find(sap) == -1:
        sap = '\\'
    index = sys.argv[0].rfind(sap)
    path = sys.argv[0][:index] + sap
    return path
