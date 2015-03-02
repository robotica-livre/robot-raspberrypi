import vertx

web_server_conf = {
    'port': 8080,
    'host': 'localhost'    
}

vertx.deploy_verticle('io.vertx~mod-web-server~2.0.0-final', web_server_conf)
