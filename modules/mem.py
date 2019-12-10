import psutil
from .Classes import DataGroup, OutputData
from fs import filesize

def memory_usage():
    mem = psutil.virtual_memory()
    total = filesize.traditional(mem.total)
    avaliable = filesize.traditional(mem.available)
    used = filesize.traditional(mem.used)

    return DataGroup("Memory", [
        OutputData("Total", total),
        OutputData("Avaliable", avaliable),
        OutputData("Used", used)
    ])



if __name__ == "__main__":
    memory_usage()