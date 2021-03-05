## الضغط على الزر

- تحتاج إلى معرفة متى يقوم اللاعب بالضغط على زر على Explorer HAT ، والزر الذي قام بالضغط عليه. أضف هذا السطر في الجزء **السفلي** من تعليماتك البرمجية:
    
    ```python
    explorerhat.touch.pressed(button_pressed)
    ```

- عند الضغط على زر، سيتم استدعاء دالة `button_pressed`، لذا تحتاج إلى كتابة هذه الدالة. ضع التعليمة البرمجية التالية في **بداية** ملفك ، مباشرة بعد عبارة `import`:
    
    ```python
    def button_pressed(channel, event):
        print("You pressed button " + str(channel) )
        explorerhat.light.off()
    ```
    
    يحتوي المتغير `channel` على رقم الزر، الذي تم الضغط عليه (1-4). اختبر برنامجك وسترى أنه عند الضغط على زر، سيتم عرض رقم الزر الذي ضغطت عليه في Python shell وسيتم إطفاء جميع الأضواء.
    
    ![رسالة تخبرك بالزر الذي تم الضغط عليه](images/pressed-button.png)