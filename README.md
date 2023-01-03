# stable-diffusion-webui-extensions-updater
Updates WebUI extensions

Requirements:
  inputimeout==1.0.4
  
Installation
To install, simply go to the "Extensions" tab in the SD Web UI, select "Install from url:", paste "https://github.com/cibernicola/stable-diffusion-webui-updater", click "install".

Then In webui-user.bat set this line:

python "YOUR PATH TO FILE\custom-updates.py"

The update will be requested, with a timeout of 10 seconds, the default answer being NO. Y key or empty means Yes, any other means No:

![image](https://user-images.githubusercontent.com/4579387/210420553-b51de553-136e-4e10-9626-f77e1b31593f.png)


Pre alpha.
