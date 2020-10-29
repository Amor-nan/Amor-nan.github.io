# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

import sys
import numpy as np
import matplotlib.pyplot as plt


class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = '离散函数'
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100,100,320,200)

        b1 = QPushButton('正弦函数', self)
        b1.move(0,0) 
        b1.clicked.connect(self.sin)
        b2 = QPushButton('冲击函数', self)
        b2.move(100,0) 
        b2.clicked.connect(self.cj)
        b3 = QPushButton('阶跃函数', self)
        b3.move(0,100) 
        b3.clicked.connect(self.jy)
        b4 = QPushButton('实指数函数', self)
        b4.move(100,100) 
        b4.clicked.connect(self.szs)

        self.show()

    @pyqtSlot()
    def sin(self):
        x=np.linspace(0,5,20)
        y1=2*np.sin(np.pi*x)
        plt.grid(True)
        plt.stem(x,y1)
        plt.show()
    def cj(self):
        y2=[1,0,0,0,0,0,0,0,0]
        plt.stem(y2)
        plt.grid(True)
        plt.show()
    def jy(self):
        def dwjy(t):
            r=np.where(t>=0.0,1.0,0.0)
            return r
        n=np.arange(-10,10)
        plt.ylim(0,3)
        plt.grid(True)
        plt.stem(n,dwjy(n))
        plt.show()
    def szs(self):
        x1=np.linspace(0,10,10)
        y4=2*0.7**x1
        plt.stem(x1,y4)
        plt.grid(True)
        plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
sys.exit(app.exec_())