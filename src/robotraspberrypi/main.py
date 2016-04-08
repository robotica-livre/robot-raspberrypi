##
# 
# 
import sys

from robotraspberrypi.webserver.server import app

def webServer():
    app.run()

if __name__ == "__main__":
#     env['web.config.debug'] = True
    if len(sys.argv) > 0:
        for arg in sys.argv:
            if arg == "--web":
                webServer()
            elif arg == "--pid":
                print "Not implemented"
            elif arg == "--verbose":
                print "Not implemented"
    print "Need to implement:"
    print "* Web"
    print "* PID"
    print "* Verbose"