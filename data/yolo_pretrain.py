from ultralytics import YOLO

# Instantiating a pre-trained YOLOv8n model
model = YOLO("C:/Users/ashis/OneDrive/Desktop/PSU/imageannotatermaster/image-annotater-master/data/YOLO11n-model-yaml/yolo11n-seg.pt")

# Path to your image
source = "c:/Users/ashis/OneDrive/Desktop/PSU/zebrafishimages/Jpg_images/20_1727_10-3dpfC 10.jpg"

# Perform inference with just one line
results = model(source)  # 

print(results)