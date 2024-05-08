import os, sys
try:
    __import__("kiron").approval()
except Exception as e:
    exit(str(e))
