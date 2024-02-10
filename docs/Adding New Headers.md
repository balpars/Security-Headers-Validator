## How do I add a new header?

By following steps below you can add new headers and/or integrate your custom header seamlessly.

1 - Navigate to headers folder and create the <header_name>.py file eg. user_agent.py

2 - Copy the contents of template_header.py into your header file.

3 - Modify your header file as needed.

4 - Find the list variable "header_files" in the header_compiler.py

5 - Append the file name to header_files eg.   
    ```
    header_files = ["x_content_type_options.py", "user_agent.py"]
    ```

#### Warnings
Header file names should not contain dashes. Instead use underscore. This is to prevent import errors.

Correct: user_agent.py
Incorrect: user-agent.py


---


TR

Aşağıdaki adımları izleyerek yeni header ekleyebilir veya kendi özel header'larınızı projeye entegre edebilirsiniz.

1 - headers klasörüne gidin ve <header_name>.py dosyasını oluşturun, mesela user_agent.py

2 - template_header.py dosyasının içeriğini yeni header dosyanıza kopyalayın.

3 - Header dosyanızı gerektiği gibi düzenleyin.

4 - Proje klasöründeki header_compiler.py dosyasında header_files listesini bulun.

5 - Dosya adını header_files listesine ekleyin. Örnek:

    ```
    header_files = ["x_content_type_options.py", "user_agent.py"]
    ```
#### Uyarılar
Dosya adları kısa çizgi içermemelidir. Bunun yerine alt tire kullanın. Bu, import hatalarını önlemek içindir.

Doğru: user_agent.py
Yanlış: user-agent.py
