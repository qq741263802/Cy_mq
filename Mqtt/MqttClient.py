# -*- coding: utf-8 -*-

import wx
import win32api
import sys, os


class MqttFrame(wx.Frame):
    def __init__(self, parent):
        '''构造函数'''

        wx.Frame.__init__(self, parent, -1, APP_TITLE)
        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.SetSize((520, 220))
        self.Center()


class mainApp(wx.App):


