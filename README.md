Photos Picker
=========
Hi photograhers,
As a photographer as well as a developer, 

I understand that choosing the right pictures from the list of customers are so frustrating and time-consuming. 

To solve this problem, I have developed a multi-platform application to help **automatically select the right photos from customers list.**

## Features
- Select photos based on user input list
- Multi-platform support (Windows, macOS, Linux)
- Easy to use GUI

## How to Use
1. Choose the input folder containing RAW photos.
2. Choose the output folder where selected photos will be saved.
3. Provide a text file containing the list of desired photo names.
4. Click on the "Kiểm tra" button to start the process.
5. The list shows copiable photos, unfound photos, and duplicates photos
6. Finally, click on the "Tiến hành lọc ảnh" button to copy the selected photos to the output folder.

## Installation
To export the application:
```bash
pyinstaller --onefile --noconsole --name="Photos Picker" --icon=icon.ico .\photos_picker.py
```
