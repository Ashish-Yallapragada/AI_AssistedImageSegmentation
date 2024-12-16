import sys
import os
import PyQt5
from PyQt5.QtWidgets import QApplication
from annotator_window import ImageAnnotator


def main():
    """
    Main function to run the Image Annotator application.
    """
    app = QApplication(sys.argv)
    window = ImageAnnotator()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
