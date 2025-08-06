from ultralytics import YOLO

model = YOLO("yolov8n.pt") 

results = model.predict('Videos/fan_vs_lee.mp4',save=True)

print(results[0])
print('==========================================')
for box in results[0]:
    print(box)