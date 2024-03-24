import os
from concurrent.futures import ThreadPoolExecutor as pool

os.system("pkg install play-audio")

def song_list():
	os.system("play-audio fun.mp3")
	




def main():
	print ("logo")
	hero=input("choice")
	
	
with pool(max_workers=3) as k:
	k.submit(song_list)
	k.submit(main)