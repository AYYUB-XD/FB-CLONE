import os, sys, platform
try:os.system('git pull')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    import kiron
    kiron.approval()
elif bit == '32bit':
    os.system("exit")
