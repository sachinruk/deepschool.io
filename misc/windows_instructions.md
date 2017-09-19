# Additional instructions for Windows users
Install VirtualBox from [here](https://www.virtualbox.org/wiki/Downloads). You may also need `git` if you have not installed it already from [here](https://git-scm.com/download/win).
1. Enable the port 9000
```
"/C/Program Files/Oracle/VirtualBox/VBoxManage" modifyvm default --natpf1 "jupyter,tcp,,9000,,9000"
```
2. Share the folder where you have downloaded the repo.
Open a terminal with bash support:
* Mount the folder on the VM, this is needed only once:
```
"/C/Program Files/Oracle/VirtualBox/VBoxManage" sharedfolder add default -name deepschool -hostpath d:/github/deepschool.io --automount
```
* Access the virtual image
```
docker-machine ssh default
```
* Create the folder:
```
sudo mkdir /deep_school
```
* Mount the shared folder into the container (you will have to repeat this step every time):
```
sudo mount -t vboxsf deepschool /deep_school
```
* When you want to launch the container:
```
docker run -v /deep_school:/notebook -p 9000:8888 deepschoolio_app
```
