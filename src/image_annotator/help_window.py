from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTextBrowser
from PyQt5.QtCore import Qt
from soft_dark_stylesheet import soft_dark_stylesheet
from default_stylesheet import default_stylesheet

class HelpWindow(QDialog):
    def __init__(self, dark_mode=False, font_size=10):
        super().__init__()
        self.setWindowTitle("Help")
        self.setModal(False)  # Make it non-modal
        self.setGeometry(100, 100, 800, 600)
        layout = QVBoxLayout()
        self.text_browser = QTextBrowser()
        self.text_browser.setOpenExternalLinks(True)
        layout.addWidget(self.text_browser)
        self.setLayout(layout)
        
        if dark_mode:
            self.setStyleSheet(soft_dark_stylesheet)
        else:
            self.setStyleSheet(default_stylesheet)
        
        self.font_size = font_size
        self.apply_font_size()
        self.load_help_content()
        
    def show_centered(self, parent):
        parent_geo = parent.geometry()
        self.move(parent_geo.center() - self.rect().center())
        self.show()
    
    def apply_font_size(self):
        self.setStyleSheet(f"QWidget {{ font-size: {self.font_size}pt; }}")
        font = self.text_browser.font()
        font.setPointSize(self.font_size)
        self.text_browser.setFont(font)

    def load_help_content(self):
        help_text = """
        <h1>Image Annotator Help Guide</h1>

        <h2>Overview</h2>
        <p>Image Annotator is a user-friendly GUI tool designed for generating masks for image segmentation and object detection. It allows users to create, edit, and save annotations in various formats, including COCO-style JSON, YOLO v8, and Pascal VOC. Annotations can be defined using manual tools like the polygon tool or in a semi-automated way with the assistance of the Segment Anything Model (SAM-2) pre-trained model. The tool supports multi-dimensional images such as TIFF stacks and CZI files and provides dark mode and adjustable application font sizes for enhanced GUI experience.</p>

        
        
        """
        self.text_browser.setHtml(help_text)
