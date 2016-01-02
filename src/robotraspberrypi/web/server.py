'''
Created on 18 de out de 2015

@author: Ricardo
'''
import web

urls = {
    '/', 'RobotServer'
}

app = web.application(urls, globals())

class RobotServer:
    def GET(self):
        return "Robot Raspberry Pi"