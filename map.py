import geopandas as gpd
import folium
import streamlit as st
# Simplified datasets for major rivers and mountain ranges
rivers = [
    {"name": "Ganga", "location": [25.5941, 85.1376], "description": "The Ganga is the longest river in India, flowing through the northern plains and considered sacred by Hindus."},
    {"name": "Yamuna", "location": [28.7041, 77.1025], "description": "The Yamuna is a major river in Northern India, flowing alongside the Ganga and passing through Delhi."},
    {"name": "Brahmaputra", "location": [26.2006, 92.9376], "description": "The Brahmaputra is a transboundary river that flows through Tibet, India, and Bangladesh, known for its powerful current."},
    {"name": "Godavari", "location": [17.0005, 81.8040], "description": "The Godavari is the second-longest river in India, often referred to as the 'Ganga of the South.'"},
    {"name": "Krishna", "location": [16.5738, 80.3573], "description": "The Krishna River flows through Maharashtra, Karnataka, Telangana, and Andhra Pradesh, supporting vast agricultural lands."},
    {"name": "Narmada", "location": [22.5173, 76.0045], "description": "The Narmada River flows westward, unlike most other major Indian rivers, and forms the traditional boundary between North and South India."},
    {"name": "Cauvery", "location": [12.6191, 78.7047], "description": "The Cauvery River, flowing through Karnataka and Tamil Nadu, is vital for irrigation in the region."},
    {"name": "Mahanadi", "location": [20.2594, 85.7812], "description": "The Mahanadi River flows through Odisha and Chhattisgarh, known for the Hirakud Dam, one of the longest dams in the world."},
    {"name": "Tapti", "location": [21.1702, 73.0650], "description": "The Tapti River flows westward, parallel to the Narmada, draining into the Arabian Sea."},
    {"name": "Indus", "location": [34.0163, 74.8090], "description": "The Indus River, one of the longest in the world, flows through China, India, and Pakistan, and is the cradle of the ancient Indus Valley Civilization."},
    {"name": "Ravi", "location": [32.2637, 75.7382], "description": "The Ravi River is one of the five rivers that give Punjab its name and flows into Pakistan."},
    {"name": "Beas", "location": [31.5546, 75.6815], "description": "The Beas River originates in the Himalayas and merges with the Sutlej River, playing a crucial role in the agriculture of Punjab."},
    {"name": "Sutlej", "location": [31.1471, 75.3412], "description": "The Sutlej River is the easternmost tributary of the Indus River and is known for the Bhakra Dam, which is one of the largest in India."},
    {"name": "Ghaghara", "location": [26.8467, 81.0004], "description": "The Ghaghara River is a major tributary of the Ganga and flows through the plains of Uttar Pradesh."},
    {"name": "Kosi", "location": [26.5116, 86.7322], "description": "The Kosi River, often called the 'Sorrow of Bihar' due to frequent flooding, is a major tributary of the Ganga."},
]


mountains = [
    {"name": "Himalayas", "location": [27.9878, 86.9250], "description": "The Himalayas are the highest mountain range in the world."},
    {"name": "Western Ghats", "location": [10.8505, 76.2711], "description": "The Western Ghats are a UNESCO World Heritage Site."},
    {"name": "Aravalli Range", "location": [24.5937, 73.7085], "description": "The Aravalli Range is one of the oldest mountain ranges in the world."},
    # Add more mountain ranges here
]
# Create a base map centered on India
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add rivers to the map
for river in rivers:
    folium.Marker(
        location=river["location"],
        popup=f"{river['name']}: {river['description']}",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Add mountains to the map
for mountain in mountains:
    folium.Marker(
        location=mountain["location"],
        popup=f"{mountain['name']}: {mountain['description']}",
        icon=folium.Icon(color='green', icon='info-sign')
    ).add_to(m)

# Save map to an HTML file
m.save("india_rivers_mountains.html")
