import os

class File():
    def __init__(self, filename):
        self.filename = filename

    def run_file(self):
        run = os.system(f'cmd /k "python {self.filename}') 
        return run
    
