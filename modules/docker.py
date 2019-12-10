import docker
from .Classes import DataGroup, OutputData

def docker_usage():
    rows = []
    try:
        containers = docker.from_env().containers.list()
        for container in containers:
            rows.append(OutputData(container.label, container.status))
    except:
        pass
    
    return DataGroup("Docker Info", rows)

