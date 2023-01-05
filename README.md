# stable-diffusion-webui-extensions-updater

Updates WebUI extensions

**Requirements:**
  inputimeout==1.0.4
  
**Installation**
To install, simply go to the "Extensions" tab in the SD Web UI, select "Install from url:", paste "https://github.com/cibernicola/stable-diffusion-webui-updater", click "install".

Then In webui-user.bat set this line:

python "YOUR PATH to \stable-diffusion-webui\extensions\stable-diffusion-webui-updater\scripts\custom-updates.py"

The update will be requested, with a timeout of 10 seconds, the default answer being NO. Y key or empty (only Enter) means Yes, any other means No:

![image](https://user-images.githubusercontent.com/4579387/210830869-92771abf-5d6d-4b4f-a303-193076957973.png)


$$
Pre alpha.
$$
