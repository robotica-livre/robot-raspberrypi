import vertx
from core.streams import Pump

web_server_conf = {
    'port': 8080,
    'host': 'localhost',
    'web_root': 'webapp'
}

logger = vertx.logger()

vertx.deploy_module('io.vertx~mod-web-server~2.0.0-final', web_server_conf)