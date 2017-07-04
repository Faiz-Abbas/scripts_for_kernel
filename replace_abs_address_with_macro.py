#Read File Line by line
#Ignoring all spaces, find out if the line starts with 0x
#command line arguments ar1 and arg2
#Replace the line with arg1(0x{number+arg2}, whatever came in brackets after
import os
import sys

#Find a set of paranthesis in a line and return whats inside
def get_in_paranthesis(line):
    s = ""
    flag = 0
    for x in line:
        if (x == '('):
            flag=1
            continue
        if(x == ')'):
            break
        if (flag == 1):
            s = s + x
            
    return s

def get_indent(string):
    indent=""
    for i in string:
        if (i == ' ' or i == '\t'):
            indent = indent + i 
        if(i.isalnum()):
            break;
    return indent



filename = sys.argv[1]
base_addr = int(sys.argv[2],16)
macro = sys.argv[3]
f = open(filename,"r+")
new = open(filename+".temp","w")
for line in f:
    line1 = line;
    indent=get_indent(line)
    line = line.strip()
    if (line[0:2] == '0x' and line.find("(") > 0):
        i = int(line[2:5],16)
        i = base_addr + i
        string = macro+"("+hex(i)+", "+get_in_paranthesis(line)+")\n"
        new.write(indent + string);
    else:
        new.write(line1)

f.close()
os.remove(filename)
new.close()
os.rename(filename+".temp",filename);
          



