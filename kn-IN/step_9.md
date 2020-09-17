## ಟೈಮರ್ ಅನ್ನು ಸೇರಿಸುವ ವಿಧಾನ

ನೀವು ಬೆಳಕನ್ನು ಆನ್ ಮಾಡಿದ ನಂತರ, ನೀವು ಟೈಮರ್ ಅನ್ನು ಪ್ರಾರಂಭಿಸಬೇಕು ಮತ್ತು ಗುಂಡಿಯನ್ನು ಒತ್ತಲು ಆಟಗಾರನು ಎಷ್ಟು ಸಮಯ ತೆಗೆದುಕೊಳ್ಳುತ್ತಾನೆ ಎಂಬುದನ್ನು ಪರಿಶೀಲಿಸಬೇಕು.

- ಮೊದಲನೆಯದಾಗಿ, ನೀವು Python ಗೆ timer function ಆಮದು(import) ಮಾಡಲು ಹೇಳಬೇಕಾಗುತ್ತದೆ. ನಿಮ್ಮ ಇತರ `import` ಹೇಳಿಕೆಗಳ ಜೊತೆ, `from time import time` ಸಾಲನ್ನು ಸೇರಿಸುವ ಮೂಲಕ `time` function ಅನ್ನು ಬಳಸಲು ಬಯಸುತ್ತೀರಿ ಎಂದು Pythonಗೆ ತಿಳಿಸಿ.

- ನಿಮ್ಮ ಪ್ರೋಗ್ರಾಂನಲ್ಲಿ ಗುಂಡಿಯನ್ನು ಒತ್ತಲಾಗಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸುವ ಕೋಡ್ ಇರುವ ಸ್ವಲ್ಪ ಮೊದಲ ಸಾಲಿಗೆ ಹೋಗಿ. ಪ್ರಸ್ತುತ ಸಮಯವನ್ನು ದಾಖಲಿಸಲು `start` ಎಂಬ ಹೊಸ ವೇರಿಯೇಬಲ್(Variable) ಅನ್ನು ಬಳಸಿ. ಪ್ರಸ್ತುತ ಸಮಯವನ್ನು ನಿಮ್ಮRaspberry Pi ಒದಗಿಸುತ್ತದೆ ಮತ್ತು ಇದು ತುಂಬಾ ನಿಖರವಾಗಿದೆ.
    
    ```python
    # ...other code above
    
    # Record the current time
    start = time()
    
    # ... other code below
    
    ```

- ದೀಪವನ್ನು ಆನ್ ಮಾಡಿದ ನಂತರ ಆಟಗಾರನು ಎಷ್ಟು ಸೆಕೆಂಡುಗಳ ವರೆಗೆ ಗುಂಡಿಯನ್ನು ಒತ್ತಿಟ್ಟುಕೊಳ್ಳಬೇಕೆಂದು ನೀವು ಆಯ್ಕೆ ಮಾಡಬಹುದು. ನಿಮ್ಮ ಪ್ರೋಗ್ರಾಂನಲ್ಲಿ, ನೀವು ಆಯ್ಕೆ ಮಾಡಿದ ಮೌಲ್ಯದ **constant** ಅನ್ನು `game_in_progress` ವೇರಿಯಬಲ್ (variable) ನಂತರ ಸೇರಿಸಿ. ನಮ್ಮ ಆಟಗಾರನಿಗೆ 1.5 ಸೆಕೆಂಡುಗಳನ್ನು ಅನುಮತಿಸಲು ನಾವು ಆರಿಸಿದ್ದೇವೆ:
    
    ```python
    game_in_progress = True
    TIME_ALLOWED = 1.5
    
    ```
    
    ಸಂಖ್ಯೆ ಚಿಕ್ಕದಾದಷ್ಟು, ಆಟಗಾರನು ಚುರುಕಾಗಿರಬೇಕಾಗುತ್ತದೆ!

- ಆಟಗಾರನು ತನಗೆ ನೀಡಿದ ಸಮಯವನ್ನು ಮೀರಿದ್ದಾನೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಲು ಈಗ ಲೂಪ್ ಸೇರಿಸಿ. ಈ ಲೂಪಿನ ನಿರಂತರ ಪರಿಶೀಲನೆಯನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಲು, ನೀವು ದೀರ್ಘ ಕಾರು ಪ್ರಯಾಣದಲ್ಲಿ ಮತ್ತೊಬ್ಬರ ಜೊತೆಗೆ ಇರುತ್ತೀರಿ ಎಂದು ಊಹಿಸಿ. ಅವರು ಪದೆಪದೆ "ನಾವು ಇನ್ನೂ ಅಲ್ಲಿದ್ದೇವೆಯೇ?", "ನಾವು ಈಗ ಅಲ್ಲಿದ್ದೇವೆಯೇ?", "ಈಗ ಹೇಗೆ?" ಎಂದು ಪ್ರಶ್ನಿಸುವ ಹಾಗೆ!
    
    ```python
    ...
    
    # Record the current time
    start = time()
    
    waiting_for_press = True
    while waiting_for_press and game_in_progress:
    
        # What's the time now?
        now = time()
        time_taken = now - start
    
        # Check if they have taken more time than they were allowed
        if time_taken > TIME_ALLOWED:
            print("You took too long!")
            explorerhat.light.off()
            game_in_progress = False    # Lose the game
    
        else:
            explorerhat.touch.pressed(button_pressed)
    
    
    ```
    
    ಬಟನ್ ಪ್ರೆಸ್‌ಗೆ ಸಂಬಂಧಿಸಿದ ಕೋಡ್ ಅನ್ನು `else` ಭಾಗಕ್ಕೆ ಸರಿಸಿ. ಅದು ಸರಿಯಾದ ಸ್ಥಳದಲ್ಲಿರಲು ನೀವು **indent** ಮಾಡಬೇಕಾಗುತ್ತದೆ.

- ನೀವು ಈ ಕೋಡ್ ಅನ್ನು ಚಲಾಯಿಸಿದರೆ(run), ನೀವು ಸರಿಯಾದ ಗುಂಡಿಯನ್ನು ತ್ವರಿತವಾಗಿ ಒತ್ತಿದರೂ ಸಹ, ಪ್ರೋಗ್ರಾಂ ನಿಮಗೆ ತುಂಬಾ ಸಮಯ ತೆಗೆದುಕೊಂಡಿದೆ ಎಂದು ಘೋಷಿಸುತ್ತದೆ. ಇದಕ್ಕೆ ಕಾರ‌ಣವೇನೆಂದರೆ, ಗುಂಡಿಯನ್ನು ಒತ್ತಿದಾಗ ಸಮಯವಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸುವುದನ್ನು ನಿಲ್ಲಿಸುವಂತೆ ನೀವು ಆಟಕ್ಕೆ ಹೇಳದಿರುವುದು. ಗುಂಡಿಯನ್ನು ಒತ್ತಿದಾಗ ಟೈಮರ್ ಅನ್ನು ನಿಲ್ಲಿಸಲು `button_pressed` ಕೋಡ್ ಅನ್ನು ಬದಲಾಯಿಸಿ.
    
    ```python
        def button_pressed(channel, event):
            print("You pressed " + str(channel) )
    
            explorerhat.light.off()
    
            global waiting_for_press
            waiting_for_press = False
    
    ```
    
    ಈ ಕೋಡ್‌ನಲ್ಲಿ, `global`, ನಮಗೆ `waiting_for_press` ವೇರಿಯೇಬಲ್(Variable) ಮೌಲ್ಯವನ್ನು ಬದಲಾಯಿಸಲು function ಒಳಗಿನಿಂದ ಅನುವು ಮಾಡುತ್ತದೆ.