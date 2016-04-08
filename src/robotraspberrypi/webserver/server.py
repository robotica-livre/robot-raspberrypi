'''
Created on 18 de out de 2015

@author: Ricardo
'''
import web
import os

urls = (
    '/command/(.*)', 'RobotServer'
)   

app = web.application(urls, globals())

render = web.template.render('web-content', base=os.getcwd())

class RobotServer:
    GET = app.autodelegate('GET_')
    
    def GET_forward(self):
        return 'forward'
    
    def GET_backward(self):
        return 'backward'
    
    def GET_left(self):
        return 'left'
    
    def GET_right(self):
        return 'right'
    
    def POST(self):
#         return render.index()
        return 'test'
