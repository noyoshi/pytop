import time
import os

from prettycli import red, green, blue, cyan

from modules.disk import disk_usage
from modules.docker import docker_usage
from modules.tmux import tmux
from modules.mem import memory_usage
from modules.network import neetwork
from modules.cpu import cpu


def draw_pairs(callbacks, delay=1):
    while True:
        string = ""
        prev = None
        for func in callbacks:
            f = func()
            s = str(f)

            if s and prev:
                string += join_data_groups(f, prev)
                prev = None
                continue

            if s and not prev:
                # string += s + "\n"
                prev = f

        if prev:
            string += join_data_groups(prev, "")

        # Clear the screen
        os.system("clear")
        print(string)
        time.sleep(delay)


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


def join_data_groups(data_group1, data_group2):
    """
    Joins the two data groups so they are side by side
    in the output
    """
    s1 = str(data_group1)
    s2 = str(data_group2)

    lines1 = list(filter(lambda x: len(x.strip()) > 0, s1.split("\n")))
    lines2 = list(filter(lambda x: len(x.strip()) > 0, s2.split("\n")))

    output = ""
    for i, line in enumerate(lines1):
        if i > len(lines2) - 1:
            output += line + " " * 40 + "\n"
            continue
        output += line + lines2[i] + "\n"

    i += 1
    while i < len(lines2):
        output += " " * 40 + lines2[i] + "\n"
        i += 1

    return output


if __name__ == "__main__":
    draw_pairs([disk_usage, memory_usage, docker_usage, tmux, neetwork, cpu])
