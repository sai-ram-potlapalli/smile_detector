import cv2
import pandas as pd
import os
from datetime import datetime

# Get the project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(PROJECT_ROOT, 'models')
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')

# Load Haar cascade classifiers
face_classifier = cv2.CascadeClassifier(os.path.join(MODELS_DIR, 'haarcascade_frontface.xml'))
smile_classifier = cv2.CascadeClassifier(os.path.join(MODELS_DIR, 'haarcascade_smile.xml'))

# Initialize data collection lists
times = []
smile_ratios = []

# Initialize video capture
cap = cv2.VideoCapture(0)

print("Smile Detector Started - Press 'ESC' to exit")

while True:
    ret, img = cap.read()
    if not ret:
        break
        
    # Convert to grayscale and apply blur
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    
    # Detect faces
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)
        
        # Extract region of interest (face area)
        roi_gray = gray[y:y + h, x:x + w]
        roi_img = img[y:y + h, x:x + w]
        
        # Detect smiles within face region
        smiles = smile_classifier.detectMultiScale(roi_gray, scaleFactor=1.2,
                                                  minNeighbors=22,
                                                  minSize=(25, 25))
        
        for (sx, sy, sw, sh) in smiles:
            # Draw rectangle around smile
            cv2.rectangle(roi_img, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 1)
            
            # Calculate smile ratio
            sm_ratio = round(sw / sx, 3)
            
            # Display smile meter
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, f'Smile meter: {sm_ratio}', (10, 50), font, 1, (200, 255, 155), 2, cv2.LINE_AA)
            
            # Record data if smile ratio is above threshold
            if sm_ratio > 1.8:
                smile_ratios.append(sm_ratio)
                times.append(datetime.now())
    
    # Display the image
    cv2.imshow('Smile Detector', img)
    
    # Check for exit key (ESC)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Save data to CSV
if smile_ratios:
    data = {'smile_ratio': smile_ratios, 'times': times}
    df = pd.DataFrame(data)
    output_file = os.path.join(DATA_DIR, 'smile_records.csv')
    df.to_csv(output_file, index=False)
    print(f"Saved {len(smile_ratios)} smile records to {output_file}")

# Clean up
cap.release()
cv2.destroyAllWindows()
print("Smile Detector stopped")
