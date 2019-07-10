# build-monitor
Build monitory in 64x32 pixel goodness

sudo ./build.py --led-chain=2 --led-multiplexing=1 --text="Muy build" -b=20

pi@raspberrypi:~/rpi-rgb-led-matrix/bindings/python/samples/build-monitor $ git config --global user.name "atoth"
pi@raspberrypi:~/rpi-rgb-led-matrix/bindings/python/samples/build-monitor $ git config --global user.email "github@unfunkyufo.com"
pi@raspberrypi:~/rpi-rgb-led-matrix/bindings/python/samples/build-monitor $ git clone https://github.com/AlexanderToth/build-monitor.git
pi@raspberrypi:~/rpi-rgb-led-matrix/bindings/python/samples/build-monitor $ git remote add origin https://github.com/AlexanderToth/build-monitor.git
pi@raspberrypi:~/rpi-rgb-led-matrix/bindings/python/samples/build-monitor $ git push origin master
git status
git add build.py
git diff build.py
git log
git commit -m "Hey there"

