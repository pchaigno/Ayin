# Ayin

Ayin let's you upload all your images from motion to your Dropbox account.


Installation
=====

1. See [this quick tutorial](http://www.maketecheasier.com/setup-motion-detection-webcam-ubuntu/) to install **motion**. [This tutorial](http://www.instructables.com/id/Raspberry-Pi-as-low-cost-HD-surveillance-camera/step7/Installing-the-motion-detection-software/) is an equivalent for Raspberry-PIs.
2. Retrieve the project: `git clone https://github.com/pchaigno/ayin && cd ayin/`
3. Create password file: `echo '[your dropbox access token]' > dropbox_api_password`
4. Restrict access to password file: `chmod go-r dropbox_api_password && sudo chown motion:motion dropbox_api_password`
5. Create log files: `touch error.log ayin.log && sudo chown motion:motion error.log ayin.log`
6. Update motion's config file: Replace `; on_picture_save value` by `on_picture_save python3 [absolute path to ayin folder]/ayin.py %f 2>> [absolute path to ayin folder]/error.log`
7. Create a new *Dropbox API App* in your Dropbox account. It only needs an access to files it creates. The name you enter will be the name of the folder where the images will be uploaded.
