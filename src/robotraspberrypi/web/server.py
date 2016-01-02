'''
Created on 18 de out de 2015

@author: Ricardo
'''
urls = {
    '/(.*)', 'Robot'
}

app = web.application(urls, globals())

class Robot:
    def GET(self):
        return "Robot Raspberry Pi"