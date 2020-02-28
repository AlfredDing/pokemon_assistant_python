import os 
import sys

filename   = sys.argv[1]
local_path = os.getcwd()

print('./' + filename + '.hex')
if os.path.exists('./' + filename + '.hex'):
    comm = 'dfu-programmer atmega16u2 erase'
    print(comm)
    ret  = os.system(comm)

    comm = 'dfu-programmer atmega16u2 flash {:}.hex'.format(filename)
    print(comm)
    ret  = os.system(comm)

    comm = 'dfu-programmer atmega16u2 reset'
    print(comm)
    ret  = os.system(comm)
