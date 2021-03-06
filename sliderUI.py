# -*- coding: utf-8 -*-
# @Author: Faisal Khan
# @Date:   2017-02-17 16:07:34
# @Last Modified by:   Faisal Khan
# @Last Modified time: 2017-02-20 13:07:15

# -*- coding: utf-8 -*-
# @Author: Faisal Khan
# @Date:   2017-02-16 14:11:13
# @Last Modified by:   Faisal Khan
# @Last Modified time: 2017-02-17 15:33:43

from PyQt4.QtGui import *
from PyQt4.QtCore import *

from pipeline import FuncParam

class SliderUI(QWidget):

    def __init__(self, funcParam):
        super(SliderUI, self).__init__()        

        self.funcParam = funcParam
        self.min = funcParam.default[0]
        self.max = funcParam.default[1]
        self.new_min = self.min
        self.new_max = self.max

        self.textValue = QLineEdit()

        self.initUI()

    def initUI(self):
        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.valueChanged[int].connect(self.sliderValueUpdated)

        if (self.funcParam.isRangeFloat()):
            self.min = 0
            self.max = 100

        self.sld.mouseReleaseEvent = self.mouseReleased

        self.sld.setRange(self.min, self.max)
        self.textValue.setText("%d"%(self.funcParam.default[0]))
        self.textValue.setEnabled(True)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(QLabel("%s"%self.funcParam.shortName()))
        self.hbox.addWidget(self.sld)
        self.hbox.addWidget(self.textValue)

        self.setLayout(self.hbox)


    def sliderValueUpdated(self, value):

        new_value = value

        if (self.new_min != self.min) or (self.new_max != self.max):
            new_value = value/100.0 * (self.new_max - self.new_min) + self.min

        self.textValue.setText("%0.2f"%(new_value))

        self.funcParam.value = new_value

    def mouseReleased(self, event):
        self.emit(SIGNAL("valueChanged()"))

        




