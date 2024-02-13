# Capturing Book Cover
This project is a simple graphical user interface (GUI) application that allows users to load an image of a book cover and extract the possible title using optical character recognition (OCR). The project is implemented in Python and utilizes the OpenCV, EasyOCR, and Tkinter libraries. <br />

Leveraging the OpenCV and EasyOCR libraries, the function takes an image and a language code as input, detecting and extracting text with a specified confidence threshold. It utilizes bounding boxes to highlight the identified text regions and displays both the recognized text and the annotated image using Matplotlib.

## Notes
Ensure to install the necessary dependencies, including OpenCV, EasyOCR, Matplotlib, and NumPy.

## Usage
1. Run the script, and a GUI window titled "Book Title Extraction" will appear.
2. Load an image of a book cover by clicking the "Load Image of Book Cover" button.
3. Select the language of the text on the book cover (English or Turkish) from the drop-down menu.
4. Click the "Extract Title" button to initiate the OCR process and extract the possible title.
5. The extracted text will be displayed in a new window. You can copy it to the clipboard using the "Copy to Clipboard" button.

## Screenshots
![Book Title Extraction](https://github.com/ekinuzunbaz/DIP-Text-Detection-EasyOCR-Python/assets/73299618/3f9173b4-f4ee-4d62-8f88-495a86bda38a)
<br /><br />
![Load Image of Book Cover](https://github.com/ekinuzunbaz/DIP-Text-Detection-EasyOCR-Python/assets/73299618/516dd1dd-31a1-44a0-ada3-3da66d62cd0d)
<br /><br />
![Lanuage Selection](https://github.com/ekinuzunbaz/DIP-Text-Detection-EasyOCR-Python/assets/73299618/3f9173b4-f4ee-4d62-8f88-495a86bda38a)
<br /><br />
![Extract Title](https://github.com/ekinuzunbaz/DIP-Text-Detection-EasyOCR-Python/assets/73299618/ec158974-da2d-48e6-ab84-8be8c20cf01b)
