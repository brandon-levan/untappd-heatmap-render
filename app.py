from flask import Flask, render_template
import os
import folium

app = Flask(__name__)


@app.route('/')
# def index():
#     start_coords = (46.9540700, 142.7360300)
#     folium_map = folium.Map(location=start_coords, zoom_start=14)
#     return folium_map._repr_html_()

def render_the_map():
	return render_template('map.html')


if __name__ == '__main__':
    # Get port from environment variable (Render sets PORT)
    port = int(os.environ.get('PORT', 8000))
    # Use 0.0.0.0 to bind to all available network interfaces
    app.run(host='0.0.0.0', port=port, debug=False)
    