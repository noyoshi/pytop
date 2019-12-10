import time
import os


from prettycli import red, green, blue, cyan

from modules.disk import disk_usage
from modules.docker import docker_usage
from modules.tmux import tmux
from modules.mem import memory_usage

def draw(callbacks, delay=2):
    while True:
        string = ""
        for func in callbacks:
            string += str(func()) + "\n"
        
        # Clear the screen
        os.system("clear")
        print(string)
        time.sleep(delay)




# disk_usage()
# docker_usage()
# tmux()

draw([disk_usage, memory_usage, docker_usage, tmux])