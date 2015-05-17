# Include the Dropbox SDK
import dropbox
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Covert communication using git repositories")
	parser.add_argument("filepath", help="File to the new file to send to Dropbox", type=str)
	args = parser.parse_args()
	
	basename = os.path.basename(args.filepath)
	script_dir = os.path.dirname(os.path.abspath(__file__))
	password_file = os.path.join(current_dir, "password")

	with open(password_file, 'r') as content_file:
		dropbox_api_password = content_file.read()

	client = dropbox.client.DropboxClient(dropbox_api_password)
	#print 'linked account: ', client.account_info()

	f = open(args.filepath, 'rb')
	response = client.put_file(basename, f)
	#print 'uploaded: ', response
