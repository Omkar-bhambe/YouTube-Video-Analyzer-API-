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

1. ```generator_api.py``` : This provides a graphical user interface (GUI) for user registration, login, and graph generation using Matplotlib.

   1. Registration : This provides the 'User Regitration Interface' for the API

   2. Login : This provides the 'User Login Interface' for the API

   3. Generate Graphs :

      - On the Graph Generation Page, you can select the type of graph you want to generate: Line, Bar, or Scatter.
   
      - Use the dropdown menu to choose the graph type.
   
      - Click the Generate Graph button to create and display the graph based on sample data.
   
      - The graph will be displayed on the right side of the screen.

    4. Exiting the application :

       - To the application, simply close the application.
