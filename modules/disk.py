import shutil
from .Classes import DataGroup, OutputData

def disk_usage():
    total, used, free = shutil.disk_usage("/")

    total = OutputData("Total", total // (2**30), "GiB")
    used = OutputData("Used", used // (2**30), "GiB")
    free = OutputData("Free", free // (2**30), "GiB")

    return DataGroup("Disk Usage", [total, used, free])
