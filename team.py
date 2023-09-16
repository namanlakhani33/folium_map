import streamlit as st
import folium
from streamlit_folium import folium_static

# Streamlit app title
st.title("Multiple Location Map")

# Default coordinates and location names
locations_data = [
    {"name": "Karuna hospital", "lat": 19.24260168397352, "lon": 72.85320203456234},
    {"name": "lotus hospital", "lat": 19.24381721140674, "lon": 72.8571502462596},
    {"name": "Ashok Hospital", "lat": 19.247205446695535, "lon": 72.85124301935589},
    {"name": "Apex Hospital", "lat": 19.252877671887852, "lon": 72.84695148490235},
    {"name": "M.M Hospital", "lat": 19.257739423097867, "lon": 72.8556203844985},
    {"name": "Narendra Hospital", "lat": 19.252148396777663, "lon": 72.85768032103618},
    {"name": "Purohit Hospital", "lat": 19.24876016297229, "lon": 72.86258854893989}
]

# Create a Folium map
m = folium.Map(location=[19.25, 72.85], zoom_start=13)

# Plot pins for each default location with tooltips and popups
for i, location_data in enumerate(locations_data):
    lat, lon = location_data["lat"], location_data["lon"]
    name = location_data["name"]

    # Create a tooltip with the location name
    tooltip = f"{name}"

    # Create a custom HTML popup with a link to Google Maps
    popup_html = f'<a href="https://www.google.com/maps?q={lat},{lon}" target="_blank">View on Google Maps</a>'

    folium.Marker(
        location=[lat, lon],
        tooltip=tooltip,
        popup=folium.Popup(popup_html, max_width=300),
    ).add_to(m)

# Display the map using st_folium
folium_static(m)
