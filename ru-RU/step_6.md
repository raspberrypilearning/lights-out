## Using the random library

This would be a pretty easy game if the lights always came on in the same order, for the same length of time! To make it as tricky as possible for the player, you need to add some randomness. You will randomize which light is turned on, and how long the program will wait before turning the next light on.

- To generate random numbers, you need to use Python's `random` library. Find the line in your program that says `from time import sleep`, and underneath it type in `import random`. Delete all of the code beneath this (where you experimented with turning the lights on and off).

- First, you will ask Python to choose a random light to turn on. Add this code to your program:
    
    ```python
    light = random.randint(1,4)
    ```
    
    This code chooses a random integer (whole number) between 1 and 4 and assigns it to the variable `light`.

- Now add some code to turn one light on depending on the number which was randomly chosen. Can you finish off the rest of the code? Note that 3 is the red light and 4 is the green light:
    
    ```python
    if light == 1:
        explorerhat.light.blue.on()
    elif light == 2:
        explorerhat.light.yellow.on()
    ```
    
    Run your program several times. Check that, each time the program runs, a different light is randomly chosen. The light should turn on immediately.

- To make the game more fun, there needs to be an unpredictable gap between the lights turning on, so let's add some code to make the program wait a random length of time before turning on the next light:
    
    Underneath the code where you chose which light to turn on, add two new lines of code:
    
    ```python
    light = random.randint(1,4)     
    
    wait_for_next = random.uniform(0.5, 3.5)
    sleep(wait_for_next)
    ```
    
    This time you are using the `random.uniform` function which allows you to choose numbers with fractional parts (decimals). In the code above, Python chooses a number which could be anything between half (0.5) and three and a half (3.5) and then waits for that number of seconds. You can change these values if you want to be more (or less) mean to your player!