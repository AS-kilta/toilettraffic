toilet traffic
==============

Control looted traffic lights in AS_ guild room based on the restroom status.
Perhaps also modulate the lights or something to indicate the amount of available coffee.

.. _AS: http://as.fi/

* Green - both free
* Yellow - one (50 %) free
* Red - both reserved


Roadmap
-------

* Design a sensor for the locks
* Build the two sensors
* Transmit the door status somehow somewhere (ESP8266?)
* Read the status and control the lights
* Bonus: easy interface for a temporary disco party mode


Details
-------

* Current control: relays, parallel port's data bus, lower three bits. Lowest for the topmost lamp (red)
* See the docs directory
* Remember to "modprobe -r lp"
* use pyparallel, for example
* Future: usb, arghduino, leds?


Overengineering
---------------

Perhaps update everything inside the lamp chassis.

* Replace the incandescent bulbs with LEDs such that the fresnel lenses still work
* Get rid of the relays and stuff - low voltage LEDs would be easy and safe to control
