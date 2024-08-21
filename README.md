# image_to_ascii

**image_to_ascii** is a Python-based application that converts images into ASCII art, generating a text file representing the visual content of the image using ASCII characters. This tool is useful for creating text-based art from images, preserving the image's visual structure in a creative way.

## Features

- **Image Conversion:** Converts images (PNG, JPG, JPEG, WEBP) to ASCII art.
- **User-Friendly Interface:** Utilizes the `easygui` module to provide a simple file selection dialog.
- **Automatic Text File Generation:** Saves the ASCII art directly to a text file (`ascii.txt`) in the current directory.

## Installation and Setup

To use **image_to_ascii**, please follow these steps:

1. **Download the Project Files:**
   - Download or clone the project repository containing the Python script.

2. **Ensure Prerequisites are Installed:**
   - **Python:** Ensure that Python is installed on your computer. If not, download and install Python from [here](https://www.python.org/downloads/).
   - **Required Modules:** The program relies on external Python modules. To install them, use `pip` as follows:

     ```bash
     pip install Pillow easygui
     ```

   - The `Pillow` module is a powerful image processing library, and `easygui` provides a simple GUI for file selection.

3. **Run the Program:**
   - Navigate to the directory where the script is located and run the Python script:

     ```bash
     python image_to_ascii.py
     ```

   - A file selection dialog will appear, allowing you to choose an image file to convert.

## Usage

Once the program is running:

1. **Select an Image:** Use the file dialog to choose the image you wish to convert.
2. **Conversion:** The program will process the image and create an ASCII representation of it.
3. **Output:** The ASCII art will be saved to a file named `ascii.txt` in the same directory as the script. The text file will automatically open after the conversion is complete.

If you encounter any issues, make sure that all necessary modules are installed and that Python is properly configured on your system.
