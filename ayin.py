#!/usr/bin/env python3
import dropbox
import argparse
import os
import time

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Send motion files to Dropbox")
	parser.add_argument("filepath", help="File to the new file to send to Dropbox", type=str)
	#parser.add_argument("changed_pixels", help="Changed pixels", type=str)
	#parser.add_argument("noise_level", help="Noise level", type=str)
	args = parser.parse_args()

	basename = os.path.basename(args.filepath)
	script_dir = os.path.dirname(os.path.abspath(__file__))
	password_file = os.path.join(script_dir, "dropbox_api_password")
	log_file = os.path.join(script_dir, "ayin.log")

	fo = open(log_file, "a")
	fo.write(args.filepath+"\n")
	#fo.write(args.changed_pixels+"\n")
	#fo.write(args.noise_level+"\n\n")
	fo.close()

	with open(password_file, 'r') as content_file:
		dropbox_api_password = content_file.read().strip()

	client = dropbox.client.DropboxClient(dropbox_api_password)
	#print 'linked account: ', client.account_info()

	f = open(args.filepath, "rb")
	try:
		response = client.put_file(basename, f)
		#print 'uploaded: ', response
		f.close()
	except dropbox.rest.ErrorResponse:
		f.close()
		time.sleep(1)
		f = open(args.filepath, "rb")
		response = client.put_file(basename, f)

	os.remove(args.filepath)
