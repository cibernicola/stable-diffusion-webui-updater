# stable-diffusion-webui-extensions-updater
Updates WebUI extensions

Requirements:
  inputimeout==1.0.4
  

Clone or download this repo in "stable-diffusion-webui\extensions". Then In webui-user.bat set this line:

python "YOUR PATH TO FILE\custom-updates.py"

The update will be requested, with a timeout of 10 seconds, the default answer being NO. Y key or empty means Yes, any other means No:

![image](https://user-images.githubusercontent.com/4579387/210354834-866da2aa-206d-4f7e-bb34-90348c95304d.png)

Pre alpha.
