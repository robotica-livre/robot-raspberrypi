import vertx
from core.event_bus import EventBus
from robot import SimpleDrive

web_server_conf = {
    'port': 1234,
    'host': 'localhost',
    'web_root': '../webapp',

    'bridge': True,

    'inbound_permitted': [
        {
            'vertx.forward': 'drive.forward'
        },
        {
            'vertx.backward': 'drive.backward'
        },
        {
            'drive.left': 'drive.left'
        },
        {
            'drive.right': 'drive.right'
        },
    ]
}

robot = SimpleDrive()

EventBus.send('vertx.forward', None, robot.forward)
EventBus.send('vertx.backward', None, robot.backward)
EventBus.send('vertx.left', None, robot.left)
EventBus.send('vertx.right', None, robot.right)



logger = vertx.logger()

vertx.deploy_module('io.vertx~mod-web-server~2.0.0-final', web_server_conf)
