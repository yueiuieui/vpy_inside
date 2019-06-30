import os
import os
import platform
def run(pro):
    sv=platform.system()
    if sv == 'Darwin':
        os.system('chmod a+x '+pro)
        os.system(pro)
    elif sv == 'Windows':
        os.system('python '+pro)
    elif sv == 'Linux':
        os.system('sudo python3 '+pro)
global ver
ver="inside"
def vin(word):
    return input(str(word))
def vout(word):
    print(word)
def write_file(file,mode,content):
    with open(file,mode) as f:
        f.write(content)
def read_file(file,mode):
    with open(file,mode) as f:
        return f.read()
def check_ver():
    return ver
