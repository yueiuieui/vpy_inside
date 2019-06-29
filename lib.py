def vin(word):
    return input(word)
def vout(word):
    return print(word)
def write_file(file,mode,content):
    with open(file,mode) as f:
        f.write(content)
    return 0
def read_file(file,mode):
    with open(file,mode) as f:
        return f.read()
def until(exp,fuc):
    while exp == True:
        return fuc
        break
    else:    
        continue