# List resulting timestamps from input files
# By Steffan Davies

import argparse, os, moviepy, time
from moviepy.editor import VideoFileClip

def GetContentsFromFolder(path):
	
	contents = os.listdir(path)
	absolutepaths = []
	
	for file in contents:
		fullpath = os.path.join(path, file)
		absolutepaths.append(fullpath)

	return absolutepaths

def GetTimestamps(files):
	
	timestamps = []

	for file in files:
		clip = VideoFileClip(file)
		duration = clip.duration
		timestamps.append(duration)

	timestamps.pop()
	return timestamps

def AddTimestamps(timestamps):
	
	addedTimestamps = []
	sum = 0
	
	addedTimestamps.append(time.strftime('%H:%M:%S', time.gmtime(sum)))
	for index, duration in enumerate(timestamps):
		sum += duration
		addedTimestamps.append(time.strftime('%H:%M:%S', time.gmtime(sum)))

	return addedTimestamps


def WriteToFile(timestamps, output):
	
	file = open(output, 'w')

	for time in timestamps:
	    file.write(str(time)+'\n')
	
	file.close()

def main():
	
	parser = argparse.ArgumentParser(description='List timestamps from input files')
	parser.add_argument('path', metavar='folder_path', type=str)
	parser.add_argument('output', metavar='output_name', type=str)
	args = parser.parse_args()

	files = GetContentsFromFolder(args.path)
	timestamps = GetTimestamps(files)
	addedTimestamps = AddTimestamps(timestamps)
	WriteToFile(addedTimestamps, args.output)
	



if __name__ == "__main__":
	main()
