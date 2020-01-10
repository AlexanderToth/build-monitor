# build-monitor
Build monitory in 64x32 pixel goodness


cd pi@raspberrypi:~/rpi-rgb-led-matrix/bindings/python/samples/build-monitor $

sudo ./build.py --led-chain=2 --led-multiplexing=1 --text="Muy build" -b=20

git config --global user.name "atoth"

git config --global user.email "github[at]unf**ufo.com"

git clone https://github.com/AlexanderToth/build-monitor.git

git remote add origin https://github.com/AlexanderToth/build-monitor.git

git push origin master

git status

git add build.py

git diff build.py

git log

git commit -m "Hey there"

# Build Env
https://code.visualstudio.com/docs/python/python-tutorial#_select-a-python-interpreter
