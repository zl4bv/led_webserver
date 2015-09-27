# LED Webserver

The goal of this project is to make an
[LED light strip](http://www.dx.com/p/300796) controllable from a web interface.

Basic setup adapted from
[this](http://alexba.in/blog/2013/01/06/setting-up-lirc-on-the-raspberrypi/)
blog post.

Configuration for LIRC from
[this](http://ocsovszki-dorian.blogspot.co.nz/2015/06/controlling-tingkam-5050rgb-led-strip.html)
blog post.

Feel free to use / adapt as you wish.

## Usage

This project is designed to run on a Raspberry PI, however any system with a
working LIRC configuration should work fine too.

Install [web.py](http://webpy.org):

```
sudo easy_install web.py
```

Now run the web server:

```
python led_webserver.py
```

Open your browser and visit http://127.0.0.1:8080/ (or whatever address is
displayed when you run the script). For an example of how this can be used
visit http://127.0.0.1:8080/example.
