import sys
from PyQt5.QtWidgets import (QApplication, QWidget, 
  QToolTip, QPushButton)
from PyQt5.QtGui import QFont
 
class Example(QWidget):
 
 def __init__(self):
  super().__init__()
 
  self.initUI()
 
 def initUI(self):
 
  QToolTip.setFont(QFont('楷体', 14))
 
  self.setToolTip('这是一个 <b>QWidget</b> 控件')
 
  btn = QPushButton('按钮', self)
  btn.setToolTip('这是一个 <b>QPushButton</b> 控件')
  btn.resize(btn.sizeHint())
  btn.move(50, 50)
 
  self.setGeometry(300, 300, 300, 220)
  self.setWindowTitle('工具提示')  
  self.show()
 
if __name__ == '__main__':
 
 app = QApplication(sys.argv)
 ex = Example()
 sys.exit(app.exec_())
