## ದೀಪಗಳನ್ನು ಹಚ್ಚುವುದು (ದೀಪಗಳನ್ನುಆನ್ ಮಾಡುವುದು)

- ಯಾವ ದೀಪಗಳನ್ನು ಆನ್ ಮತ್ತು ಆಫ್ ಮಾಡಬೇಕೆಂದು Explorer Hat ‌ಗೆ ಹೇಳಲು ನೀವು Python ಬಳಸಬಹುದು. ನಿಮ್ಮ Python file ‌ಗೆ ಈ ಕೆಳಗಿನ ಹೊಸ ಸಾಲುಗಳನ್ನು ಸೇರಿಸಿ, ನಂತರ ಅದು ಏನು ಮಾಡುತ್ತದೆ ಎಂಬುದನ್ನು ನೋಡಲು ಪ್ರೋಗ್ರಾಂ ಅನ್ನು run ಮಾಡಿ:
    
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
    
    ನಿಮ್ಮ ಪ್ರೋಗ್ರಾಮ್ ಈ ಕೆಲಸಗಳನ್ನು ಹೇಗೆ ಮಾಡಬೇಕೆಂಬುದುದರ ಬಗ್ಗೆ ನೀವು ಅಭ್ಯಾಸ ಮಾಡಬಹುದೇ?
    
    - ಇತರ ಬಣ್ಣದ ದೀಪಗಳನ್ನು ಪ್ರತ್ಯೇಕವಾಗಿ ಆನ್ ಮಾಡಿ (ನೀಲಿ, ಹಳದಿ, ಹಸಿರು)
    - ಎಲ್ಲಾ ದೀಪಗಳನ್ನು ಒಮ್ಮೆಗೇ ಆಫ್ ಮಾಡಿ
    - ದೀಪಗಳನ್ನು ಆನ್ ಮತ್ತು ಆಫ್ ಮಾಡಿದ ಸಮಯದ ಅವಧಿಯನ್ನು ಬದಲಾಯಿಸಿ