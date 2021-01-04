from pytube import YouTube

try:
	link = input("Enter URL: ")
except:
	print("Try again !")

vid = YouTube(link)

res = int(input("Pick a resolution (1: highest / 2: lowest): "))

path = input("Enter full path where you want to download the video: ")

if res==1:
	vid.streams.get_highest_resolution().download(output_path=path)
elif res ==2:
	vid.streams.get_lowest_resolution().download(output_path=path)
else:
	print("Unvalid choice.")