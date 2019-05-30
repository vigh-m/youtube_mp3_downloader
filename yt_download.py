#!/usr/bin/python
import youtube_dl
import argparse
 
def download(link):
	print('Downloading the video')
	opts={
		'format':'bestaudio/best',
                 'postprocessors':[{
                         'key':'FFmpegExtractAudio',
                        'preferredcodec':'mp3',
			'preferredquality':'192',
                        }]
		}
	youtube_dl.YoutubeDL(opts).download([link])
	print('Completed the download')

def parse_the_arguments():
        parsed_arguments = []
        parser = argparse.ArgumentParser(description='Script to dl audio from YT videos')
        parser.add_argument('-l', help="Link to the video")
        args = parser.parse_args()
        parsed_arguments.append(args.l)
        return parsed_arguments

def main():
        parsed_arguments = parse_the_arguments()
        if 'youtube.com' in parsed_arguments[0]:
                download(parsed_arguments[0])
        else:
                print('Non-youtube link entered')


if __name__ == "__main__":
         main()


