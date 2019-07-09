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
def getResult(whatgetresult):
    return whatgetresult
    
ver="inside"
def vin(word):
    '''This is a input fuction,it can get what user entered.
    For example:
    >>a=vin("hi_")
    hi_t
    >>vout(a)
    "t"'''
    return input(str(word))
def vout(word):
    '''This is a output fuction,it can show what did you say to user.
    For example:
    >>vout(i)
    i
    >>vout(3=5)
    False
    >>vout(3+5)
    8'''
    print(word)
def write_file(file,mode,content):
    with open(file,mode) as f:
        f.write(content)
def read_file(file,mode):
    with open(file,mode) as f:
        return f.read()
def check_ver():
    return ver
