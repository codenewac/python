import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from WeatherWin import Ui_MainWindow
import requests


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 将queryBtn连接到槽函数queryWeather()
        # 将cleraBtn连接到槽函数clearResult()
        self.queryBtn.clicked.connect(self.queryWeather)
        self.clearBtn.clicked.connect(self.clearResult)

    def queryWeather(self):
        print('*queryWeather ')
        cityName = self.WeathercomboBox.currentText()
        cityCode = self.transCityNames(cityName)

        rep = requests.get('http://www.weather.com.cn/data/sk/' + cityCode + '.html')
        rep.encoding = 'utf-8'
        print(rep.json())

        msg1 = '城市：%s' % rep.json()['weatherinfo']["city"] + '\n'
        msg2 = '风向：%s' % rep.json()['weatherinfo']["WD"] + '\n'
        msg3 = '温度：%s' % rep.json()['weatherinfo']["temp"] + '\n'
        msg4 = '风力：%s' % rep.json()['weatherinfo']["WS"] + '\n'
        msg5 = '湿度：%s' % rep.json()['weatherinfo']["SD"] + '\n'
        result = msg1 + msg2 + msg3 + msg4 + msg5
        self.resultText.setText(result)

    def transCityNames(self,cityName):
        cityCode=''
        if cityName=='北京':
            cityCode='101010100'
        elif cityName=='天津':
            cityCode='101030100'
        elif cityName=='上海':
            cityCode='101020100'
        elif cityName=='孝感':
            cityCode='101200401'

        return cityCode

    def clearResult(self):
        print("* clearResult ")
        self.resultText.clear()

if __name__=="__main__":
    app=QApplication([])
    win=MainWindow()
    win.show()
    sys.exit(app.exec_())

