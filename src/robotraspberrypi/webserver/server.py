'''
Created on 18 de out de 2015

@author: Ricardo
'''
import web

urls = (
    '/', 'RobotServer'
)

app = web.application(urls, globals())
render = web.template.render('web-content/')

class RobotServer:
    def GET(self):
        return render.index()