#!/usr/bin/env python
# 
# Copyright 2015 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 
import sys
import time
from time import sleep
from collections import deque
from matplotlib import pyplot as plt
import numpy
import gras
from gnuradio import gr
from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import collections
import random
import time
import math
import numpy as np
import threading

class Plot(gr.sync_block):
    """
    docstring for block add_python
    """
    def __init__(self,sampleinterval,timewindow,num_plot):
	a = []
        for i in range(0,num_plot):
	    a.append(numpy.float32)
	size=(600,350)
	self.num_plot = num_plot
	self.ip = 0
	self.ptr1 = 0
	self.win = pg.GraphicsWindow()
	self.plt = self.win.addPlot()
        self.plt.showGrid(x=True, y=True)
        self.plt.setLabel('left', 'amplitude', 'V')
        self.plt.setLabel('bottom', 'time', 's')
	# Data stuff
        self._interval = int(sampleinterval*1000)
        self._bufsize = int(timewindow/sampleinterval)
	if self.num_plot == 1:
	    self.databuffer = collections.deque([0.0]*self._bufsize, self._bufsize)
            self.x = np.linspace(0.0,timewindow,self._bufsize)
            self.y = np.zeros(self._bufsize, dtype=np.float)
            self.curve = self.plt.plot(self.x, self.y, pen=(255,0,0))

	elif self.num_plot == 2:
            self.databuffer = collections.deque([0.0]*self._bufsize, self._bufsize)
            self.x = np.linspace(0.0,timewindow,self._bufsize)
            self.y = np.zeros(self._bufsize, dtype=np.float)
            self.curve = self.plt.plot(self.x, self.y, pen=(255,0,0))
	    self.win.nextRow()
            self.plt1 = self.win.addPlot()
            self.plt1.showGrid(x=True, y=True)
            self.plt1.setLabel('left', 'amplitude', 'V')
            self.plt1.setLabel('bottom', 'time', 's')
	    self.databuffer1 = collections.deque([0.0]*self._bufsize, self._bufsize)
	    self.x1 = np.linspace(0.0,timewindow,self._bufsize)
            self.y1 = np.zeros(self._bufsize, dtype=np.float)
            self.curve1 = self.plt1.plot(self.x1, self.y1, pen=(255,0,0))
	elif self.num_plot == 3:
	    self.databuffer = collections.deque([0.0]*self._bufsize, self._bufsize)
            self.x = np.linspace(0.0,timewindow,self._bufsize)
            self.y = np.zeros(self._bufsize, dtype=np.float)
            self.curve = self.plt.plot(self.x, self.y, pen=(255,0,0))
	    self.win.nextRow()
	    self.databuffer1 = collections.deque([0.0]*self._bufsize, self._bufsize)
            self.x1 = np.linspace(0.0,timewindow,self._bufsize)
            self.y1 = np.zeros(self._bufsize, dtype=np.float)
            self.curve1 = self.plt.plot(self.x1, self.y1, pen=(255,0,0))
	    self.win.nextRow()
	    self.databuffer2 = collections.deque([0.0]*self._bufsize, self._bufsize)
            self.x2 = np.linspace(0.0,timewindow,self._bufsize)
            self.y2 = np.zeros(self._bufsize, dtype=np.float)
            self.curve2 = self.plt.plot(self.x2, self.y2, pen=(255,0,0))
	elif self.num_plot == 4:

	    self.databuffer = collections.deque([0.0]*self._bufsize, self._bufsize)
            self.x = np.linspace(0.0,timewindow,self._bufsize)
            self.y = np.zeros(self._bufsize, dtype=np.float)
            self.curve = self.plt.plot(self.x, self.y, pen=(255,0,0))
	    self.win.nextRow()
            self.databuffer1 = collections.deque([0.0]*self._bufsize, self._bufsize)
            self.x1 = np.linspace(0.0,timewindow,self._bufsize)
            self.y1 = np.zeros(self._bufsize, dtype=np.float)
            self.curve1 = self.plt.plot(self.x1, self.y1, pen=(255,0,0))
	    self.win.nextRow()
            self.databuffer2 = collections.deque([0.0]*self._bufsize, self._bufsize)
            self.x2 = np.linspace(0.0,timewindow,self._bufsize)
            self.y2 = np.zeros(self._bufsize, dtype=np.float)
            self.curve2 = self.plt.plot(self.x2, self.y2, pen=(255,0,0))
	    self.win.nextRow()
	    self.databuffer3 = collections.deque([0.0]*self._bufsize, self._bufsize)
            self.x3 = np.linspace(0.0,timewindow,self._bufsize)
            self.y3 = np.zeros(self._bufsize, dtype=np.float)
            self.curve3 = self.plt.plot(self.x3, self.y3, pen=(255,0,0))


        gr.sync_block.__init__(self,
            name="Plot",
            in_sig=a,
            out_sig=None)

    def getdata(self,ip):
        new = ip
	print "new\n",ip
        return new
    def updateplot1(self):
	self.databuffer.append( self.getdata(self.ip1) )
        self.y[:] = self.databuffer
	self.curve.setData(self.y)	
#	self.ptr1 += 1
#        self.curve.setPos(self.ptr1, 0)
    def updateplot2(self):
        self.databuffer.append( self.getdata(self.ip1) )
	self.databuffer1.append( self.getdata(self.ip2) )
        self.y[:] = self.databuffer
	self.y1[:] = self.databuffer1
        self.curve.setData(self.y)
	self.curve1.setData(self.y1)
	
#	self.ptr1 += 1
#	self.curve.setPos(self.ptr1, 0)

    def updateplot3(self):
        self.databuffer.append( self.getdata(self.ip1) )
        self.databuffer1.append( self.getdata(self.ip2) )
	self.databuffer2.append( self.getdata(self.ip3) )
        self.y[:] = self.databuffer
        self.y1[:] = self.databuffer1
	self.y2[:] = self.databuffer2
        self.curve.setData(self.y)
        self.curve1.setData(self.y1)
	self.curve2.setData(self.y2)
#        self.ptr1 += 1
#        self.curve.setPos(self.ptr1, 0)

    def updateplot4(self):
        self.databuffer.append( self.getdata(self.ip1) )
        self.databuffer1.append( self.getdata(self.ip2) )
        self.databuffer2.append( self.getdata(self.ip3) )
	self.databuffer3.append( self.getdata(self.ip4) )
        self.y[:] = self.databuffer
        self.y1[:] = self.databuffer1
        self.y2[:] = self.databuffer2
	self.y3[:] = self.databuffer3
        self.curve.setData(self.y)
        self.curve1.setData(self.y1)
        self.curve2.setData(self.y2)
	self.curve3.setData(self.y3)
    def work(self, input_items, output_items):
	try:
	    self.ip1 = input_items[0][0]
	except IndexError:
	    pass
	try:
	    self.ip2 = input_items[1][0]
	except IndexError:
	    pass
	try:
	    self.ip3 = input_items[2][0]
	except IndexError:
	    pass
	try:
	    self.ip4 = input_items[3][0]
	except IndexError:
	    pass
	if self.num_plot == 1:
	    self.updateplot1()
	elif self.num_plot == 2:
	    self.updateplot1()
	    self.updateplot2()
#            th1 = threading.Thread(target=self.updateplot2)
#            th1.setDaemon(True)

#	    th2 = threading.Thread(target=self.updateplot2)
#	    th2.setDaemon(True)
#	    th2.start()
#	    th1.start()
	elif self.num_plot == 3:
	    self.updateplot1()
            self.updateplot2()
	    self.updateplot3()
	elif self.num_plot == 4:
	    self.updateplot1()
            self.updateplot2()
	    self.updateplot3()
            self.updateplot4()
	return len(input_items[0])
