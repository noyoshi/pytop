import libtmux
import time

from prettycli import cyan
from .Classes import DataGroup, OutputData

def tmux():
    server = libtmux.Server()
    sessions = server.list_sessions()
    rows = []
    for sess in sessions:
        sess_name = sess.get("session_name")
        sess_created_time = int(sess.get("session_created"))
        sess_time = time.localtime(sess_created_time)
        parsed_time = time.strftime("%m/%d/%Y %H:%M", sess_time)
        rows.append(OutputData(sess_name, parsed_time, color=cyan().bold()))
    
    return DataGroup("Tmux", rows)
