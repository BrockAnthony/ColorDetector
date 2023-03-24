# ColorDetector

Command line color detector written in Python that identifies the color name of a user-selected pixel in an image

To use, make sure you have Python installed on your computer, along with the OpenCV and pandas libraries.
Download the "Colors.csv" file, which contains color data in CSV format.
Open a terminal window and navigate to the directory where the program file and the "Colors.csv" file are located.
Run the program by entering the command "python <program_file_name.py> -i <image_file_path>" in the terminal, where <program_file_name.py> is the name of the program file and <image_file_path> is the path to the image file you want to analyze.
The program will display the image in a new window. Click on any pixel in the image to obtain the color name and RGB values of that pixel.
The program will display the color name, RGB values, and a rectangle box highlighting the selected pixel's location in the image.
Press the esc key or "Q" to exit the program.
Note: The program will only work with images that are in a format supported by OpenCV, such as JPEG, PNG, or BMP. Also, make sure that the "Colors.csv" file is located in the same directory as the program file, and that the file name is spelled correctly.
