# Untappd_Heatmap

## About
Visualizing my Untappd check-ins through a Folium interactive heat map and create an embeddable link by deploying the map as a Render web application.

## Interactive Map
The interactive map was created with the folium package in python as well as altair and geopandas. 

## Deploying to the Web
The map was deployed to the web with Render.

## Local Development
To run this application locally:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Open your browser and navigate to `http://localhost:5000`

## Deployment on Render
This application is configured to deploy on Render's free tier. The deployment uses:
- Python 3.9.16
- Gunicorn as the WSGI server
- Automatic deployment from the main branch
