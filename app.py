#!/bin/python3

"""
Original GoPro file naming convention

	Chaptered Video:
		G[Encoding][Chapter][Filenumber].mp4

		Eg. 
			GH011234.mp4, GH021234.mp4, GH031234.mp4 belong to the same clip but different sections
			GH011234.mp4, GH011235.mp4, GH011236.mp4 are all the first section of different videos

My optimized file naming convention
	{dir}/G{encoding}_{filenumber}_{chapter}.mp4


"""

from sys import argv
from os import listdir, rename
from os.path import isdir, isfile, join

try:

	if isdir(argv[1]):
		media_directory = argv[1] # First argument after script call

		if media_directory[-1] == "/":
			media_directory = media_directory[:-1]


	file_list = [f for f in listdir(media_directory) if isfile(join(media_directory, f))]

	for file in file_list:

		encoding = file[1]
		chapter = file[2:4]
		filenumber = file.lower().split(".mp4")[0][-4:] # Last 4 digits of file


except NameError as name_error:
	print( f"{argv[1]} is not a valid directory" )
	print( "Please pass a valid directory name\nExample: python3 app.py C:/User/Documents" )
except IndexError as index_error:
	print( "Run this script in the command line with arguments\nExample: python3 app.py C:/User/Documents" )