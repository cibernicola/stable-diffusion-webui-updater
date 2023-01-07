# stable-diffusion-webui-extensions-updater

Updates WebUI extensions

**Requirements:**
  inputimeout==1.0.4
  
**Installation**
To install, simply go to the "Extensions" tab in the SD Web UI, select "Install from url:", paste "https://github.com/cibernicola/stable-diffusion-webui-updater", click "install".

Then In webui-user.bat set this line:

python "YOUR PATH to \stable-diffusion-webui\extensions\stable-diffusion-webui-updater\scripts\custom-updater.py"

The update will be requested, with a timeout of 10 seconds, the default answer being NO. Y key or empty (only Enter) means Yes, any other means No:

![image](https://user-images.githubusercontent.com/4579387/210862028-bd320321-93e7-4d13-9e39-740db9a6eca1.png)


$$
Alpha 1.
=======
TO-DO: Auto insert in bat/sh files.
$$
