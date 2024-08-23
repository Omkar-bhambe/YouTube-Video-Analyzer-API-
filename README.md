# YouTube-Video-Analyzer-API

## Overview

<p><h3>The YouTube Video Analyzer API is a Python-based tool designed to fetch, analyze, and visualize data from YouTube videos using the YouTube Data API. It allows users to retrieve video statistics, analyze trends, and generate insightful visualizations using libraries such as Matplotlib.</h3></p>

## Features 
- Video Data Retrieval: Fetch detailed statistics of YouTube videos, including views, likes, comments, and more.
  
- Visualization: Generate visual representations of data using Matplotlib for better insights.

## Prerequisites
- Python 3.6 or higher
- A valid YouTube Data API v3 key create one sign up at [Google Cloud Console](https://console.cloud.google.com/welcome?_gl=1*1jpi0pq*_up*MQ..&gclid=6fee5bd906181f19f5443d1e43428b92&gclsrc=3p.ds&hl=en&project=yt-media-432209)
- And following python packages:
  
  - 'google-api-python-client'
 
  - 'random'
    
  - 'matplotlib'
    
  - 'pandas'
    
  - 'numpy'
    
  - 'seaborn' (optional, for enhanced visualization)

## Installation 

1. Clone the repository :
    ```bash
    git clone https://github.com/Omkar-bhambe/Weathe_API.git
    cd Weather_API
    ```
2. Install virtual environment on your system and activate it :
     ```bash
     python3 -m venv venv
     source venv\Scripts\activate
     ```
3. Install required packages :
    ```bash
    pip install -r requirements.txt
    ```
4. Set Up your API KEY :
   ```bash
   API_KEY = 'YOUR_API_KEY'
   ```
5. Give YouTube Video ID :
   ```bash
   Video_ID = 'ID_OF_THE_VIDEO'
   ```
   #### Both 4th and 5th steps are to be used at the time of execution

## Usage 

This allows the user to fetch data of any data available on YouTube and plots graph for views, likes, and comments showcases a table which consist statistical analysis and views per day from the date of upload till current date. 

1. Set Up API KEY :

```bash
API_KEY = 'YOUR_API_KEY'
```

2. Choose a YouTube Video ID :

```bash
video_id = 'YOUR_VIDEO_ID'
```

3. Run the script

```bash
python youtube_video_analysis.py
```

4. View the Result
   
 - After running the script, the following outputs will be displayed:
   
    - ```Video Title``` : The title of the YouTube video.
    - ```Count of Likes``` : The number of likes the video has received.
    - ```Count of Comments``` : The number of comments on the video.
    - ```Views Per Day``` : The average number of views per day since the video was published.
    - ```Statistical Analysis``` : Mean, median, and standard deviation of views, likes, and comments.
  
5. Visualize the Data

  - The script will generate and display the following visualizations:

      - ```Bar Chart``` : Shows the counts of views, likes, and comments.
      - ```Pie Chart``` : Represents the proportional distribution of views, likes, and comments.
      - ```Scatter Plot``` : Plots the counts of views, likes, and comments as individual points.
      - ```Statistics Table``` : Displays a table of the calculated statistics.
   
6. Customize the Script

- If desired, you can customize the script by modifying the plot_data() function to change the style, color, or type of plots generated.

#### Example Output

```
Title : Me at the zoo
Count of Likes : 16696290
Count of Comments : 10362874
Views Per Day : 46913.00 views/day

Statistical Analysis:
Mean Value for Views,Like,Comments: 119438911.33
Median Value for Views,Like,Comments: 16696290.00
Standard Deviation Value Views,Like,Comments: 183467670.61
Views Per Day: 46913.00
```
## An Overview of how the plot will it look like after execution

### Bar Plot

<img src = "YouTube Video Analysis Output/Bar Plot.png" height = 380 width = 600>

### Pie Plot

<img src = "YouTube Video Analysis Output/Pie - Chart.png">

### Scatter Plot

<img src = "YouTube Video Analysis Output/Scatter Plot.png" height = 380 width = 600>

### Statistical Table

<img src = "YouTube Video Analysis Output/Statistical Analysis Table.png">
