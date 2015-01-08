#mm_mantid_example.py
print "*********************"
print "*********************"
print "This program demonstrates using a memory map like a file to create and then run a script"
print "This memory mapped script can also be written to file"
print "In this example, the auto generated script is written to the same directory as this scipt is run from"
print "The user will need to ensure that the path to the file is correct"
print "This program will:"
print "  1. Read in a Mantid data file"
print "  2. Open a memory mapped file"
print "  3. Write a script to the memory mapped file"
print "  4. Execute the script using the memory mapped file"
print "  5. Write the script to a disk file"
print "  6. Execute the script from the disk file"
print "*********************"
raw_input("Press Enter to continue")
import sys,os
print "** Setting up Mantid environment"

sys.path.append(os.environ['MANTIDPATH'])
from mantid.simpleapi import *
print "Mantid environment initialized"

#read in a mantid workspace
wsfile='C:\Users\mid\Documents\Mantid\Powder\zrh_1000.nxs'
print "** Loading workspace: ",wsfile
ws=Load(Filename=wsfile)

#open a memory mapped file
import mmap
Nbytes=80*10 #80 chars per line times 10 lines 
print "** Creating mmap object"
mm = mmap.mmap(-1,Nbytes) #need to define the space - length is in bytes
mm.write("print 'Projecting workspace'\n")
mm.write("ws_proj=ConvertToMD(ws,'|Q|','Direct')\n")
mm.write("print 'Projecting workspace complete'\n")
term="eof\n"
mm.write(term) #create my own terminator marker for later
#mm.close()
print "*********************"

print "** Executing mmap object line by line"
#reposition mm pointer to beginning of mfile
mm.seek(0)
#now read individual lines and execute them
while True:
    line=mm.readline()
    if line == "": break
    elif line == term: break
    print "executing line: ",line
    exec line
print "*********************"

print "** Writing mmap object to file line by line"
#point to file beginning
mm.seek(0)
#open a file to write a script to
filename="mm_mantid_generated_script.py"
f=open(filename, "wb")
while True:
    line=mm.readline()
    if line == "": break
    elif line == term: break
    print "writing line: ",line
    f.write(line)
f.close()
print "*********************"
#now let's execute the file we just created as a cross check
print "** Executing using the file created from the mmap object"
execfile(filename)
print "*********************"