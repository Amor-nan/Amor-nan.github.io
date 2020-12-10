from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
        QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout)

import sys

class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 2

    def __init__(self):
        super(Dialog, self).__init__()

        b1=QPushButton("导入音频")
        b2=QPushButton("分析比较")

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(b1)
        mainLayout.addWidget(b2)

        self.setLayout(mainLayout)
        self.setWindowTitle("根据音频拨号音识别出当前所拨号码")
        self.setGeometry(100,100,320,200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())