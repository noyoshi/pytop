import docker
from .Classes import DataGroup, OutputData

def docker_usage():
    containers = docker.from_env().containers.list()
    rows = []
    for container in containers:
        rows.append(OutputData(container.label, container.status))
    
    return DataGroup("Docker Info", rows)
