from ultralytics import YOLO

model = YOLO("/Users/lilahu/Desktop/Code/table-tennis-detection/models/best.pt") 

results = model.predict('/Users/lilahu/Desktop/Code/table-tennis-detection/runs/detect/predict/fan_vs_harimoto.mp4',save=True)

print(results[0])
print('==========================================')
for box in results[0]:
    print(box)