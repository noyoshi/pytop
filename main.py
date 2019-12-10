import time
import os

from prettycli import red, green, blue, cyan

from modules.disk import disk_usage
from modules.docker import docker_usage
from modules.tmux import tmux
from modules.mem import memory_usage
from modules.network import neetwork
from modules.cpu import cpu


def draw(callbacks, delay=1):
    while True:
        string = ""
        for func in callbacks:
            s = str(func())
            if s:
                string += s + "\n"

        # Clear the screen
        os.system("clear")
        print(string)
        time.sleep(delay)


if __name__ == "__main__":
    draw([disk_usage, memory_usage, docker_usage, tmux, neetwork, cpu])
