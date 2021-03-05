## الإعداد

قبل أن تبدأ، تأكد من ان Raspberry Pi متوقفة عن العمل ومطفأة.

- قم بتركيب Explorer HAT بعناية على GPIO pins على Raspberry Pi الخاص بك، ثم قم بتشغيل Pi.

- افتح Python 3 من قائمة Programming:
    
    ![فتح Python 3](images/python3-app-menu.png)

- قم بإنشاء ملف جديد بالنقر فوق **File** > **New File** واكتب التعليمة البرمجية `import explorerhat` قبل الضغط على **F5** لتشغيل برنامجك.

إذا كان كل شيء يعمل ، يجب أن ترى رسالة تقول "Explorer HAT Pro detected...". إذا لم يكن الأمر كذلك ، تحقق من أنك قد قمت بـ[تثبيت البرنامج](what-you-will-need)، وأنك قمت بتوصيل Explorer HAT الخاص بك بشكل صحيح مع دبابيس GPIO.