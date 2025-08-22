import os
from utils import vars









class Reader():
    def __init__(self):
        path = vars.path_logs
    
    def process_line(self,line):
            print(line.strip())
            return line.strip() 
    
    def reader(self):
        files_routes = [entry.path for entry in os.scandir(vars.path_logs)]
        for routes in files_routes:
            with open(routes, "r") as f:
                for line in f:
                    self.process_line(line)
    