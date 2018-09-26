#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math   #add modul math
import numpy  #add modul numpy
import matplotlib.pyplot as mpp  #add modul matplotlib and rename it to mpp


if __name__=='__main__':    #условие
    arguments = numpy.r_[0:200:0.1]#arguments - множество чисел от 0 до 200 с шагом0.1
    mpp.plot(  #обращение к модулю
        arguments,  #???
        [math.sin(a) * math.sin(a/20.0) for a in arguments]  #для а из arguments
    )  #скобочка)
    mpp.show()  #вывод графика
