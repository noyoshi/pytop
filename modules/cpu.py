import psutil

from .Classes import DataGroup, OutputData


def cpu():
    cpu_times = psutil.cpu_times()
    user = cpu_times.user
    system = cpu_times.system
    total = user + system
    # Not exactly sure what these numbers mean

    return DataGroup("CPU", [
        OutputData("User", user),
        OutputData("System", system),
        OutputData("Total", total)
    ])
