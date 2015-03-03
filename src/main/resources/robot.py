import vertx
from core.event_bus import EventBus

web_server_conf = {
    'port': 8080,
    'host': 'localhost',
    'web_root': '../webapp'

    'bridge': True

    'inbound_permitted': [
        {
            'address': 'drive.forward'
        },
        {
            'address': 'drive.backward'
        },
        {
            'address': 'drive.left'
        },
        {
            'address': 'drive.right'
        },
    ]
}

logger = vertx.logger()

vertx.deploy_module('io.vertx~mod-web-server~2.0.0-final', web_server_conf)
