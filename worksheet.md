# Lights Out!

In this resource you can find out how to make a fast paced fun reaction game using the Explorer HAT. The zombies are coming - can you turn the lights off quick enough? 

## Setting up 

**Before you start**, make sure your Raspberry Pi is powered down and switched off 

1. Carefully mount the Explorer HAT onto the GPIO pins on your Raspberry Pi, then boot up the Pi.

2. Open Python 3 from the applications menu, under **Programming**:

![](images/python3-app-menu.png)

3. Create a new file by clicking `File > New File` and type in `import explorerhat` before pressing F5 to run your program.

If everything is working you should see a message saying "Explorer HAT Pro detected". If not, check that you have [installed the software](software.md) correctly and connected your Explorer HAT to the GPIO pins. 

The Explorer HAT has touch buttons labelled 1-4, and four LED lights in different colours. The **aim of the game** is to code the Explorer HAT to randomly choose a light to turn on, and the user must press the corresponding button to turn the light off. If the player is too slow or if they press the wrong button, the game is over.  


## Turning on lights

1. You can use Python to tell the Explorer HAT which lights to turn on and off. Add the new lines of code into your Python file, then run the program to see what it does:

```python
import explorerhat
from time import sleep

explorerhat.light.red.on()
sleep(2)
explorerhat.light.red.off()
sleep(1)
explorerhat.light.on()
sleep(5)
```

Can you work out how to...
* Turn the other coloured lights on individually (blue, yellow, green)?
* Turn all of the lights off?




## Adding randomness to your game

This would be a pretty easy game if the lights came on in the same order, for the same length of time. To make it as tricky as possible for the player we need to add some randomness! Here are the things we will decide randomly:

* Which light is chosen to turn on
* How long the user gets to press the button
* How long the pause is in between one light turning off and the next light turning on


