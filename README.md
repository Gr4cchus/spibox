# spibox
<b>Unofficial spibox software pulled from a spibox sd card via spibox.zip</b> <br />
* /spibox would be placed into /home/pi/spibox/ 
* *.desktop files would be placed into /home/pi/Desktop

## Hardware notes
* PIR sensors and the Raspberry Pi 3 sometimes don't get along - if you're having false trigger reports, make sure the PIR Sensor is far away from the Pi 3
* Runs on 5v-12V power
* Digital signal output is 3.3V high/low
* Sensing range ~6-7 meters
* 110-120 x 70 degree cone
### Wiring
    VCC(+)  Pin 2(5v)
    OUT     Pin 7(GPIO4)
    GND(-)  Pin 6(Ground)
### Hardware notes extended
Based on the Parallax datasheet-slightly different model-of their sensor<br/>
>"The PIR Sensor requires a ‘warm-up’ time in order to function properly.  This is due to the settling time 
involved  in  ‘learning’  its  environment.    This  could  be  anywhere  from  10-60  seconds.    During  this  time 
there should be as little motion as possible in the sensors field of view."
* Human body IR wavelength of 9.4um
    *  Infrared in this range will not pass through many types of material that pass visible light such as ordinary window glass and plastic.
## Tuning notes
![https://learn.adafruit.com/assets/13829](https://cdn-learn.adafruit.com/assets/assets/000/013/829/original/proximity_PIRbackLabeled.jpg?1390935476)<br/>
* PIR sensors seem to come set with default Delay Time of full rotation clockwise @ 2.5 Seconds, and Sensitivity set to the middle.
* Spibox sensors seem to deviate from the above diagram and instead have the Jumper placed on the other side of the "Adjusts". As well as having the jumper settings to "non-retriggering" based upon markings on the circuit board; L @ top and H @ bottom relative to above diagram orientation.
<br/>

Sensor pointed to the sky:
* *clockwise* makes it more sensitive
* left adjust sets *Delay Time* (2.5-250 seconds)
* right adjust sets *Sensitivity*
<br/>

Jumper Positioning:
* non-retriggering mode: L (Default?)
* retriggering mode: H (Suggested?)
 
#### Reference Material
[Sensor Overview](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor?view=all)

[RPi.GPIO module basics](https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/)