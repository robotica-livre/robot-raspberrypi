'''
Created on 7 de abr de 2016

@author: Ricardo
'''
from robotraspberrypi.webserver.server import app
import unittest

class Test(unittest.TestCase):

    def testForwardCommand(self):
        if app.request('/command/forward').data == 'forward':
            pass
        
    def testBackwardCommand(self):
        if app.request('/command/backward').data == 'backward':
            pass
    
    def testLeftCommand(self):
        if app.request('/command/left').data == 'left':
            pass
        
    def testRightCommand(self):
        if app.request('/command/right').data == 'right':
            pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()