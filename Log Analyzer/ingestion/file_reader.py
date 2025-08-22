import os
from utils import vars



def process_line(line):
    print(line.strip())
    return line.strip() 


def reader():
    files_routes = [entry.path for entry in os.scandir(vars.path_logs)]
    for routes in files_routes:
        with open(routes, "r") as f:
            for line in f:
                process_line(line)

 



