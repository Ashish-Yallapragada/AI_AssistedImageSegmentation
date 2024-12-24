"AI_AssistedImageSegmentation and Annotation"

Requirements:

-> Download the Python 3.11 version to ensure easy download of modules
-> Download the below modules of Python using pip install (Eg: pip install PyQt5)
PyQt5>=5.15.7

Pillow>=9.0.0

numpy>=1.21.0

tifffile>=2023.3.15

czifile>=2019.7.2

opencv-python >=4.10.0

pyyaml>=6.0.2

scikit-image>=0.24.0

json>=2.0.9

ultralytics>=8.2.94

plotly>=5.24.1

shapely>=2.0.6

Download YOLO models:
https://docs.ultralytics.com/tasks/segment/#models
Recommended YOLO model for better performance: https://github.com/ultralytics/assets/releases/download/v8.3.0/yolo11n-seg.pt

Download SAM plugins:
https://docs.ultralytics.com/models/sam-2/

Download links of different types of SAM models:
Tiny: https://github.com/ultralytics/assets/releases/download/v8.2.0/sam2_t.pt
Small: https://github.com/ultralytics/assets/releases/download/v8.2.0/sam2_s.pt
Base: https://github.com/ultralytics/assets/releases/download/v8.2.0/sam2_b.pt
Large: https://github.com/ultralytics/assets/releases/download/v8.2.0/sam2_l.pt

Make sure to download all the SAM models in the working directory (src/imageannotator/). Where main.py is located.


