# Usage Guide

## Quick Start

### 1. Run the Smile Detector
```bash
python src/app.py
```

### 2. Visualize Results
```bash
python src/graph.py
```

## Detailed Usage

### Smile Detection Application (`src/app.py`)

The main application provides real-time smile detection with the following features:

#### Controls
- **ESC Key**: Exit the application
- **Real-time Display**: Shows live video with detection overlays

#### Visual Indicators
- **Blue Rectangle**: Detected face boundary
- **Green Rectangle**: Detected smile within the face
- **Smile Meter**: Numerical value showing smile intensity

#### Data Collection
- Automatically records smile ratios above 1.8 threshold
- Saves data to `data/smile_records.csv`
- Includes timestamps for each measurement

### Data Visualization (`src/graph.py`)

Creates interactive visualizations of collected smile data:

#### Features
- **Time Series Plot**: Shows smile ratios over time
- **Interactive Elements**: Zoom, pan, and hover for details
- **Highlighting**: Red circles mark high smile ratios (>2.0)
- **Export**: Saves as `smile_graph.html` in project root

#### Output
- Interactive HTML file with Bokeh visualization
- Can be opened in any web browser
- Supports data exploration and analysis

## Understanding the Data

### Smile Ratio
- **Calculation**: `smile_width / smile_x_coordinate`
- **Threshold**: Values above 1.8 are recorded
- **High Smile**: Values above 2.0 are highlighted in graphs

### Data Format
```csv
smile_ratio,times
1.897,2023-12-01 15:24:52.691
2.031,2023-12-01 15:24:52.768
```

### File Locations
- **Input Data**: `data/smile_records.csv`
- **Output Graph**: `smile_graph.html` (project root)
- **Models**: `models/haarcascade_*.xml`

## Best Practices

### For Optimal Detection
1. **Lighting**: Ensure good, even lighting on your face
2. **Position**: Face the camera directly
3. **Distance**: Maintain 1-2 feet from the camera
4. **Background**: Use a plain, uncluttered background

### For Data Collection
1. **Session Length**: Run for 5-10 minutes for meaningful data
2. **Natural Expressions**: Use genuine smiles for accurate measurements
3. **Consistent Conditions**: Maintain similar lighting and positioning

### For Analysis
1. **Multiple Sessions**: Collect data across different times/days
2. **Context Notes**: Consider what activities were happening during high smile periods
3. **Trend Analysis**: Look for patterns in smile intensity over time

## Troubleshooting

### No Face Detected
- Check lighting conditions
- Ensure face is clearly visible
- Try adjusting camera position

### No Smile Detected
- Smile more broadly
- Ensure good lighting on face
- Check if face detection is working

### Poor Data Quality
- Ensure stable camera position
- Use consistent lighting
- Avoid rapid movements

## Advanced Usage

### Customizing Thresholds
Edit `src/app.py` line 47 to change the smile recording threshold:
```python
if sm_ratio > 1.8:  # Change this value
```

### Batch Processing
Run multiple sessions and combine data:
```python
# In Python
import pandas as pd
df1 = pd.read_csv('data/session1.csv')
df2 = pd.read_csv('data/session2.csv')
combined = pd.concat([df1, df2])
combined.to_csv('data/combined_sessions.csv')
``` 