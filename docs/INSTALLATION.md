# Installation Guide

## Prerequisites

- Python 3.6 or higher
- Webcam access
- Good lighting conditions for optimal detection

## Step-by-Step Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/smile_detector.git
cd smile_detector
```

### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify Installation
```bash
python src/app.py
```
Press 'ESC' to exit the application.

## Troubleshooting

### Common Issues

1. **OpenCV Installation Issues**
   ```bash
   pip uninstall opencv-python
   pip install opencv-python-headless
   ```

2. **Webcam Not Found**
   - Ensure your webcam is connected and not in use by other applications
   - Try changing the camera index in `src/app.py` (line 18):
     ```python
     cap = cv2.VideoCapture(1)  # Try different indices: 0, 1, 2
     ```

3. **Permission Denied**
   - On macOS/Linux, ensure camera permissions are granted
   - On Windows, check privacy settings for camera access

### System Requirements

- **Windows**: Windows 10 or later
- **macOS**: macOS 10.14 or later
- **Linux**: Ubuntu 18.04 or later (with GUI support)

## Dependencies

- **opencv-python**: Computer vision library for face and smile detection
- **pandas**: Data manipulation and CSV handling
- **bokeh**: Interactive data visualization 