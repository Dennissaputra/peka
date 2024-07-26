import time
from ultralytics import YOLO
import cv2
import math  # Import the math module
import numpy as np

def video_detection(path_x):
    video_capture = path_x
    cap = cv2.VideoCapture(video_capture)
    frame_width = int(cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1040))
    frame_height = int(cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 880))

    model = YOLO("best.pt")
    classNames = ['Adik', 'Apa', 'Ayah', 'Baik', 'Bau', 'Berapa', 'Berhenti', 'Buruk', 'Cantik', 'Cinta', 'Datang', 'Diam', 'Dimana', 'Ganteng', 'Hai', 'Ibu', 'Janji', 'Kacamata', 'Kaget', 'Kakak', 'Kakek', 'Kamu', 'Kapan', 'Kemana', 'Lagi', 'Lari', 'Maaf', 'Makan', 'Marah', 'Mendengar', 'Minum', 'Mobil', 'Mohon', 'Motor', 'Ngantuk', 'Pergi', 'Pintar', 'Rumah', 'Sama-sama', 'Saya', 'Sedih', 'Sedikit', 'Selamat pagi', 'Selamat tinggal', 'Senang', 'Takut', 'Telepone', 'Terimakasih', 'Tidur', 'Tolong']

    colors = np.random.uniform(0, 255, size=(len(classNames), 3))

    start_time = time.time()
    frame_count = 0

    while True:
        success, img = cap.read()
        if not success:
            break
        
        frame_count += 1
        
        results = model(img, stream=True)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cls = int(box.cls[0])
                color = colors[cls]

                cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
                conf = math.ceil((box.conf[0] * 100)) / 100
                class_name = classNames[cls]
                label = f'{class_name} {conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                cv2.rectangle(img, (x1, y1), c2, color, -1, cv2.LINE_AA)  # filled
                cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

        yield img

        # Calculate frame rate
        elapsed_time = time.time() - start_time
        fps = frame_count / elapsed_time
        print(f"Frame rate: {fps:.2f} fps")

    cap.release()
    cv2.destroyAllWindows()
