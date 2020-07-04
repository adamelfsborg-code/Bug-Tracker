import sys 
from file import File
filename = sys.argv[1]

f = File(filename)

print(f.run_file())

