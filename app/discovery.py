import  consul, os, socket
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
    
def register(name=None, port=5000, service_tags=None, consul_url=None):
    ip = get_ip_address()
    consul_port = None
    if not consul_url:
        consul_host=os.getenv("CONSUL_IP")
    else:
        consul_host = consul_url.split[':'][0]
        consul_port = int(consul_url.split[':'][1])
    if not name:
        service_name=os.getenv("SERVICE_NAME")
    if not service_tags:
        service_tags=os.getenv("SERVICE_TAGS")
        if service_tags:
            if ',' in service_tags:
                service_tags=service_tags.split(',')
    if not consul_port:
        consul_port=int(os.getenv("CONSUL_PORT"))
    c = consul.Consul(host=consul_host, port=consul_port)
    s = c.agent.service
    s.register(name, service_id=socket.gethostname(), address=ip, port=port, http=f"http://{ip}:{port}/healthcheck", interval="10s", tags=service_tags)
    return s