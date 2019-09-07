from config import *
from parse_map_data import *

def search_cmd( cmd ):
    cmd_dict={
        '0f':'whole map',
        '0': '1',
        '3': '2',
        '2': '3',
        '1': '5',
    }
    try:
        result = cmd_dict[cmd]
    except:
        result = 0
    return result


def divUselessHead(line):
    a = line.find(g_wifi_line_heed)
    line=line[a+len(g_wifi_line_heed)]
    return line


def isWifiLine(line):
    a=line.find(g_wifi_line_heed)
    if(a==-1):
        return True
    else:
        return False




def parse_line(line):
    a=isWifiLine(line)
    if(a):
        pass
        return
    pass