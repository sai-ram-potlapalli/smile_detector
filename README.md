<<<<<<< HEAD
# Smile Detector

A real-time smile detection system that uses computer vision to detect faces and smiles from a webcam feed, measures smile intensity, and visualizes the data.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/smile_detector.git
cd smile_detector

# Install dependencies
pip install -r requirements.txt

# Run the smile detector
python src/app.py

# Visualize results (after collecting data)
python src/graph.py
```

## 📁 Project Structure

```
smile_detector/
├── src/                    # Source code
│   ├── app.py             # Main smile detection application
│   └── graph.py           # Data visualization script
├── models/                 # ML models
│   ├── haarcascade_frontface.xml
│   └── haarcascade_smile.xml
├── data/                   # Data files
│   └── smile_records.csv   # Recorded smile data
├── docs/                   # Documentation
│   ├── INSTALLATION.md     # Installation guide
│   └── USAGE.md           # Usage guide
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── .gitignore             # Git ignore rules
```

## ✨ Features

- **Real-time Detection**: Live face and smile detection using Haar cascade classifiers
- **Smile Measurement**: Calculates and displays smile intensity ratios
- **Data Collection**: Automatically records smile data with timestamps
- **Interactive Visualization**: Creates beautiful, interactive graphs using Bokeh
- **Cross-platform**: Works on Windows, macOS, and Linux

## 📋 Requirements

- Python 3.6+
- Webcam access
- Good lighting conditions

## 🔧 Installation

See [INSTALLATION.md](docs/INSTALLATION.md) for detailed installation instructions.

## 📖 Usage

See [USAGE.md](docs/USAGE.md) for comprehensive usage guide.

### Basic Usage

1. **Start Detection**:
   ```bash
   python src/app.py
   ```
   - Press 'ESC' to exit
   - Blue rectangle = detected face
   - Green rectangle = detected smile
   - Smile meter shows intensity

2. **View Results**:
   ```bash
   python src/graph.py
   ```
   - Creates interactive HTML visualization
   - Shows smile ratios over time
   - Highlights high smile periods

## 🧠 How It Works

1. **Face Detection**: Uses Haar cascade classifier to detect faces in video frames
2. **Smile Detection**: Within detected faces, identifies smile regions using another Haar cascade
3. **Smile Measurement**: Calculates smile ratio (width/height of smile region)
4. **Data Recording**: Saves smile ratios above 1.8 threshold with timestamps
5. **Visualization**: Creates time-series plots of smile intensity

## 📊 Data Format

The system records:
- **Smile Ratio**: Calculated as `smile_width / smile_x_coordinate`
- **Timestamp**: Precise time of each measurement
- **Threshold**: Only records ratios above 1.8

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenCV for computer vision capabilities
- Haar cascade classifiers for face and smile detection
- Bokeh for interactive data visualization

## 📞 Support

If you encounter any issues:
1. Check the [troubleshooting section](docs/USAGE.md#troubleshooting)
2. Review the [installation guide](docs/INSTALLATION.md)
3. Open an issue on GitHub

---

**Note**: Ensure good lighting and position your face clearly in the camera for optimal detection results.
=======
# smile_detector
>>>>>>> 1f07ad560640c9b4d625086507db3693f835bf4a
