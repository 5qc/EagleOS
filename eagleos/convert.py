import os, os.path, re
from .error import *

class convert:
    def __init__(self, file):
        if os.path.exists(file):
            f = open(file)
            data = f.read()

            newF = open(f"{file}.py", "w")
            
            data = re.sub(re.compile(r"for \((.*?) in (.*?)\) do \((.*?)\)", "gs"), r"for \1 in \2:\3", data)
            data = re.sub(re.compile(r"if \((.*?) is (.*?)\) do \((.*?)\)", "gs"), r"if \1 == \2:\3", data)
            data = re.sub(r"echo (.*)", r"print(\1)", data)
            data = re.sub(r"set (.*?): (.*?)", r"\1 = \2", data)

            newF.write(data)
            newF.close()
            
            os.system(f"python3 {file}.py")
            os.remove(f"{file}.py")
        else:
            error(error.preset("filenotexists"))
