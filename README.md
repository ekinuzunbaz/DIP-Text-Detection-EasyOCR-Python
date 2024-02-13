# Capturing Book Cover
This project is a simple graphical user interface (GUI) application that allows users to load an image of a book cover and extract the possible title using optical character recognition (OCR). The project is implemented in Python and utilizes the OpenCV, EasyOCR, and Tkinter libraries.

## Notes
Ensure you have the required libraries installed using the following command:

``` pip install opencv-python easyocr matplotlib ```

## Usage
1. Run the script, and a GUI window titled "Book Title Extraction" will appear.
2. Load an image of a book cover by clicking the "Load Image of Book Cover" button.
3. Select the language of the text on the book cover (English or Turkish) from the drop-down menu.
4. Click the "Extract Title" button to initiate the OCR process and extract the possible title.
5. The extracted text will be displayed in a new window. You can copy it to the clipboard using the "Copy to Clipboard" button.
