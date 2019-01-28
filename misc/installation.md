## Installation
These are instructions if you wish to run this locally or on binder:
If you are a beginner (haven't done CNNs yet) simply click [this link](https://mybinder.org/v2/gh/sachinruk/deepschool.io/master) instead of following the installation comands below. It launches a live notebook server with these notebooks using [binder](https://beta.mybinder.org/): [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/sachinruk/deepschool.io/master)

In general (ignoring binder):
1. Install Docker https://www.docker.com/
2. Use the following commands to run from docker<sup>[1](#myfootnote1)</sup>.
```
git clone https://github.com/sachinruk/deepschool.io.git
cd deepschool.io
bash run.sh
```
3. Now go to `localhost:9000` on your browser to start using the jupyter notebooks.
4. (Optional) If you are on a mac/windows some of the examples may not work because the docker image may run out of memory. Hence under preferences in docker there is the option to increase the allocated memory. I have set it to 8GB. Run `bash run.sh` again if you reset memory.

See [here](./misc/windows_instructions.md) for installing on windows.