import os, platform
bit = platform.architecture()[0]
if "64bit" in bit:
  import tt
else:
  print(" Not Supported your 32 bit device ")
