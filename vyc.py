from standard import *
vout("------vy compiler ------")
cp=vin("> ")
with open(cp+'.vy','r') as f:
    temp=f.read()
write_file('temp.py','w','from standard import *\n'+temp)
run('temp.py')
