from datetime import datetime

import redis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QFont
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
import json
import re
import requests
from adodbapi import connect
from qfluentwidgets import InfoBar, InfoBarPosition, window

from UI.Ui_attendance import Ui_Form

host = "redis-12134.c252.ap-southeast-1-1.ec2.redns.redis-cloud.com"
port = 12134
password = "7PlhZNhVrIPLpvm0HVotfNKI02BLiqsm"
connect = False

try:
    redis = redis.Redis(host=host, port=port, password=password)
    redis.ping()
    connect = True
except Exception:
    connect = False


class AttendanceInterface(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        comboBox = self.comboBox
        # 添加选项
        items = ['本月', '上月', '本年', '上年', '日期区间']
        comboBox.addItems(items)

        # 当前选项的索引改变信号
        comboBox.currentIndexChanged.connect(lambda index: print(comboBox.currentText()))
        button = self.select
        button.clicked.connect(lambda index: self.selectData())

        # 启用边框并设置圆角
        self.tableView.setBorderVisible(True)
        self.tableView.setBorderRadius(8)

        self.tableView.setWordWrap(False)

    def selectData(self):
        self.showTable(self.get_attendance())
        if connect:
            print("")
            # json_array_from_redis = redis.get('attendanceID')
            # # 解析 JSON 字符串为数组
            # id_list = json.loads(json_array_from_redis)
            # print(id_list)
            # self.showTable(self.get_attendance())
        else:
            InfoBar.error(
                title="出错啦",
                content="查询失败，请检查网络或者关闭VPN!",
                orient=Qt.Vertical,  # 内容太长时可使用垂直布局
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=2000,
                parent=self
            )

    def showTable(self, dates):
        # 定义比较的时间
        start = datetime.strptime("09:00:00", "%H:%M:%S")
        mid = datetime.strptime("12:00:00", "%H:%M:%S")
        end = datetime.strptime("20:30:00", "%H:%M:%S")

        self.tableView.setRowCount(len(dates[0]))
        self.tableView.setColumnCount(3)
        # 设置水平表头并隐藏垂直表头
        self.tableView.setHorizontalHeaderLabels(['日期', '时间', '星期'])
        self.tableView.verticalHeader().hide()
        for i, date in enumerate(dates):
            self.tableView.setColumnWidth(i, 180)
            for j in range(len(date)):
                item = QTableWidgetItem(date[j])
                # 时间
                if i == 1:
                    time = datetime.strptime(date[j], "%H:%M:%S")
                    if start < time < mid:
                        #迟到
                        item.setForeground(QBrush(Qt.red))
                item.setFont(QFont('楷体', 15, QFont.Black))
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.tableView.setItem(j, i, item)

    def get_attendance(self):  # put application's code here
        # 可以通过 request 的 args 属性来获取参数
        where = ''
        # # 写入 redis 中
        # # 通过管道 pipeline 来操作 redis，以减少客户端与 redis-server 的交互次数。
        # list = ["123", "456"]
        # json_array = json.dumps(list)
        # redis.set("attendanceID",json_array)

        # 从 Redis 中获取 JSON 字符串
        # json_array_from_redis = redis.get('attendanceID')
        #
        # # 解析 JSON 字符串为数组
        # id_list = json.loads(json_array_from_redis)

        # print(id_list)
        # if id not in id_list:
        #     print("此工号不可查询!")

        id = "16759"
        dateCode = self.comboBox.currentText()
        if dateCode == '本月':
            # 本月
            where = 'Month(A.Date) = month(getdate()) and Year(A.Date) =year(getdate())'
        elif dateCode == '上月':
            # 上月
            where = 'Month(A.Date) = month(dateadd(m,-1,getdate())) and Year(A.Date) =year(dateadd(m,-1,getdate()))'
        elif dateCode == '本年':
            # 本年
            where = 'Year(A.Date) =year(getdate())'
        elif dateCode == '上年':
            # 上年
            where = 'Year(A.Date) =year(dateAdd(year,-1,getdate()))'
        elif dateCode == '日期区间':
            # 具体范围
            beginDate = "beginDate"
            endDate = "endDate"
            where = "CONVERT(DATETIME,A.Date) >= CONVERT(DATETIME,'" + beginDate + "') and CONVERT(DATETIME,A.Date) <= CONVERT(DATETIME,'" + endDate + "')"
        # 请求
        # c0-id=7166_1712905079013
        str = ["callCount=1",
               "c0-scriptName=ajax_DatabaseAccessor",
               "c0-methodName=executeQuery",
               "c0-param0=string:HRM117",
               "c0-param1=string:select distinct code,CnName,Department,CardCode,Date,Time,ScName from ( SELECT distinct B.code,B.CnName,C.Name as Department,A.CardCode,Convert(nvarchar,A.Date,23) Date,min(time) MinTime,max(time) MaxTime,CodeInfo.ScName  FROM AttendanceCollect as A  LEFT JOIN Employee as B on A.EmployeeId=B.EmployeeId  LEFT JOIN Department as C ON C.DepartmentId=B.DepartmentId  LEFT JOIN Machine AS D ON A.MachineId=D.MachineId  LEFT JOIN AttendanceCollectLog AS F ON A.AttendanceCollectLogId=F.AttendanceCollectLogId  LEFT JOIN Employee AS E ON F.CollectEmployeeId=E.EmployeeId  LEFT JOIN CodeInfo ON CodeInfo.CodeInfoId = A.RepairId  where B.code = '" + id + "' and " + where + " group by B.code,B.CnName,C.Name,A.CardCode,ScName,Convert(nvarchar,A.Date,23)  ) MM  UNPIVOT(Time for Subject in(MinTime,MaxTime) )as up order by Date,Time",
               "c0-param2=null:null", "c0-param3=null:null", "xml=true"]
        data = '\n'.join(str)
        url = "https://efgpcn.digiwin.com/NaNaWeb/dwrDefault/exec/ajax_DatabaseAccessor.executeQuery.dwr"
        headers = {'Accept': '*/*',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                   'Cache-Control': 'no-cache',
                   # 'Content-Length': '1395',
                   'Sec-Ch-Ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
                   'Content-Type': 'text/plain; charset=utf-8',
                   'Host': 'efgpcn.digiwin.com',
                   'Origin': 'https://efgpcn.digiwin.com',
                   'Pragma': 'no-cache',
                   'Proxy-Connection': 'keep-alive',
                   'Referer': 'https://efgpcn.digiwin.com/NaNaWeb/GP/WMS/PerformWorkItem/CallFormHandler?hdnMethod=handleForm',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
                   }

        # response = requests.post(url=url, data=data, headers=headers)
        #
        # text = response.text
        # print(text)
        # # 定义正则表达式
        # date_pattern = r'\d{4}-\d{2}-\d{2}'
        # time_pattern = r'\"(\d{1,2}:\d{2}(?::\d{2})?)\"'
        #
        # # 使用正则表达式提取日期
        # dates = re.findall(date_pattern, text)
        # times = re.findall(time_pattern, text)
        dates = ['2024-09-02', '2024-09-02', '2024-09-03', '2024-09-03', '2024-09-04', '2024-09-04', '2024-09-05',
                 '2024-09-05', '2024-09-06', '2024-09-06', '2024-09-09', '2024-09-09', '2024-09-10', '2024-09-10',
                 '2024-09-11', '2024-09-11', '2024-09-12', '2024-09-12', '2024-09-13', '2024-09-13', '2024-09-18',
                 '2024-09-18', '2024-09-19', '2024-09-19', '2024-09-20', '2024-09-20']
        times = ['09:03:29', '18:09:40', '08:52:57', '18:08:59', '08:51:38', '18:31:32', '08:39:16', '18:08:30',
                 '08:42:17', '18:36:55', '08:52:39', '18:22:58', '08:53:01', '18:21:48', '09:01:15', '18:06:58',
                 '08:58:59', '18:08:05', '08:48:26', '18:18:08', '09:02:11', '18:13:14', '08:51:12', '18:14:49',
                 '08:49:49', '08:53:07']

        # 打印提取的日期
        print("日期", dates)
        print("时间", times)
        data = [[], [], []]
        weeks = []
        for date in dates:
            i = datetime.strptime(date, "%Y-%m-%d").weekday()
            week = ''
            if i == 0:
                week = '星期一'
            elif i == 1:
                week = '星期二'
            elif i == 2:
                week = '星期三'
            elif i == 3:
                week = '星期四'
            elif i == 4:
                week = '星期五'
            elif i == 5:
                week = '星期六'
            elif i == 6:
                week = '星期日'
            weeks.append(week)
        data[0] = dates
        data[1] = times
        data[2] = weeks
        return data
