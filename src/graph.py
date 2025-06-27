import pandas as pd
import os
from bokeh.plotting import figure, show, output_file
from datetime import datetime

def create_smile_graph():
    """Create and display smile ratio visualization"""
    try:
        # Get the project root directory
        PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
        
        # Load data
        data_file = os.path.join(DATA_DIR, 'smile_records.csv')
        df = pd.read_csv(data_file)
        
        if df.empty:
            print("No smile data found. Run app.py first to collect data.")
            return
            
        # Extract data
        smile_ratios = list(df['smile_ratio'])
        times = list(df['times'])
        
        # Convert string times to datetime objects
        date_time = [datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f') for d in times]
        
        # Create plot (updated for newer Bokeh version)
        p = figure(width=800, height=400, 
                  x_axis_type='datetime',
                  title='Smile Ratio Over Time',
                  x_axis_label='Time',
                  y_axis_label='Smile Ratio')
        
        # Plot line
        p.line(date_time, smile_ratios, alpha=0.7, line_width=2, legend_label='Smile Ratio')
        
        # Highlight high smile ratios
        for ratio, dt in zip(smile_ratios, date_time):
            if ratio > 2.0:
                p.circle(dt, ratio, color="red", alpha=0.8, size=8, legend_label='High Smile (>2.0)')
        
        # Save and show
        graph_file = os.path.join(PROJECT_ROOT, 'smile_graph.html')
        output_file(graph_file)
        show(p)
        print(f"Graph saved as {graph_file}")
        
    except FileNotFoundError:
        print("smile_records.csv not found. Run app.py first to collect data.")
    except Exception as e:
        print(f"Error creating graph: {e}")

if __name__ == "__main__":
    create_smile_graph()
