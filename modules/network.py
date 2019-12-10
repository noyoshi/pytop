import psutil
from prettycli import magenta
from fs import filesize
from .Classes import DataGroup, OutputData


def neetwork():
    new_value = psutil.net_io_counters().bytes_sent + \
        psutil.net_io_counters().bytes_recv

    if neetwork.old_value:
        value = new_value - neetwork.old_value
    else:
        value = new_value

    value = filesize.traditional(value)

    neetwork.old_value = new_value

    return DataGroup("Network", [
        OutputData("IO", value, color=magenta)
    ])


neetwork.old_value = 0
