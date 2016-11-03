# Lights Out!

In this resource you can find out how to make a fast paced fun reaction game using the Explorer HAT. The zombies are coming - can you turn the lights off quick enough? 

The Explorer HAT has touch buttons labelled 1-4, and four LED lights in different colours. The **aim of the game** is to code the Explorer HAT to randomly choose a light to turn on, and the user must press the corresponding button to turn the light off. If the player is too slow or if they press the wrong button, the game is over.  

## Setting up 

**Before you start**, make sure your Raspberry Pi is powered down and switched off 

1. Carefully mount the Explorer HAT onto the GPIO pins on your Raspberry Pi, then boot up the Pi.

2. Open Python 3 from the applications menu, under **Programming**: ![](images/python3-app-menu.png)

3. Create a new file by clicking `File > New File` and type in `import explorerhat` before pressing F5 to run your program.

If everything is working you should see a message saying "Explorer HAT Pro detected...". If not, check that you have [installed the software](software.md) correctly and connected your Explorer HAT to the GPIO pins. 


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
    * Turn all of the lights off at once?
    * Change the length of time lights are turned on and off for?


## Adding randomness to your game

This would be a pretty easy game if the lights came on in the same order, for the same length of time! To make it as tricky as possible for the player we need to add some randomness! Here are the things we will decide randomly:

* Which light is chosen to turn on
* How long the Explorer HAT waits before turning the next light on
* How long the user gets to press the button before they lose

1. To generate random numbers we need to use Python's `random` library. Find the line in your program that says `from time import sleep`, and underneath it type in `import random`. Delete all of the code beneath this where you experimented with turning the lights on and off.

2. Firstly we will ask Python to choose a random light to turn on. Add this code to your program:

    ```python
    light = random.randint(1,4)
    ```

    This code chooses a random integer (whole number) between 1 and 4 and assigns it to the variable `light`. We are choosing lights by number rather than colour because later on we will need to test whether the user pressed the corresponding numbered button.

3. Now add some code to turn on a light depending on which light was randomly chosen. Can you finish off the rest of the code - 3 is the red light and 4 is the green light:

    ```python
    if light == 1:
        explorerhat.light.blue.on()
    elif light == 2:
        explorerhat.light.yellow.on()
    ```

    Run your program several times to check that each time the program runs, a different light is randomly chosen and lights up immediately. 

4. To make the game more fun, there needs to be an unpredictable gap between the lights, so we will add some code to wait a random length of time before turning on the next light:

Underneath the code where you chose which light to turn on, add a new line of code:

```python
light = random.randint(1,4)
wait_for_next = random.uniform(0.5, 3.5)

sleep(wait_for_next)
```
This time we are using the `random.uniform` function which allows us to choose decimal numbers. In the code above, Pytho chooses a number which could be anything between half a second (0.5) and 3 and a half seconds (3.5) and then waits for that number of seconds. You can change these values if you want to be more (or less) mean to your player!

## 




