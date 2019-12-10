import time
import os

from prettycli import red, green, blue, cyan

from modules.disk import disk_usage
from modules.docker import docker_usage
from modules.tmux import tmux
from modules.mem import memory_usage

def draw(callbacks, delay=2, file=None):
    while True:
        string = ""
        for func in callbacks:
            string += str(func()) + "\n"
        
        # Clear the screen
        os.system("clear")
        if file:
            with open(file, "w+") as f:
                f.write(str(string))
        else:
            print(string)
        time.sleep(delay)


if __name__ == "__main__":
    draw([disk_usage, memory_usage, docker_usage, tmux], file="temp.txt")
