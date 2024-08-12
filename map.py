import streamlit as st
import folium
from streamlit_folium import st_folium

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
    {"name": "Himalayas", "location": [27.9878, 86.9250], "description": "The Himalayas are the highest mountain range in the world, home to Mount Everest and several other peaks over 8,000 meters."},
    {"name": "Western Ghats", "location": [10.8505, 76.2711], "description": "The Western Ghats are a UNESCO World Heritage Site, known for their rich biodiversity and tropical forests."},
    {"name": "Aravalli Range", "location": [24.5937, 73.7085], "description": "The Aravalli Range is one of the oldest mountain ranges in the world, running across Rajasthan, Haryana, and Delhi."},
    {"name": "Eastern Ghats", "location": [15.6916, 80.1524], "description": "The Eastern Ghats run parallel to the Bay of Bengal, with significant biodiversity and home to several hill stations."},
    {"name": "Vindhya Range", "location": [23.4733, 77.9479], "description": "The Vindhya Range forms a natural barrier between North and South India, with ancient significance in Indian history and mythology."},
    {"name": "Satpura Range", "location": [22.1500, 78.8333], "description": "The Satpura Range runs parallel to the Vindhya Range, known for its dense forests and wildlife sanctuaries."},
    {"name": "Karakoram Range", "location": [35.8825, 76.5133], "description": "The Karakoram Range, located in the northern part of India, is home to K2, the second-highest peak in the world."},
    {"name": "Pir Panjal Range", "location": [33.5036, 74.8793], "description": "The Pir Panjal Range is part of the lesser Himalayas, located primarily in Jammu and Kashmir, known for its scenic beauty and challenging trekking routes."},
    {"name": "Zanskar Range", "location": [33.6105, 77.1672], "description": "The Zanskar Range is located in the Ladakh region, known for its stark landscapes and being part of the Trans-Himalayan zone."},
    {"name": "Nilgiri Hills", "location": [11.4064, 76.7054], "description": "The Nilgiri Hills are part of the Western Ghats, famous for hill stations like Ooty and a rich variety of flora and fauna."},
    {"name": "Patkai Range", "location": [26.0173, 95.9384], "description": "The Patkai Range is located in Northeast India, forming the border between India and Myanmar, known for dense forests and tribal cultures."},
    {"name": "Shivalik Hills", "location": [30.3165, 78.0322], "description": "The Shivalik Hills are the outermost range of the Himalayas, extending across the northern states of India."},
    {"name": "Annamalai Hills", "location": [10.2390, 77.4890], "description": "The Annamalai Hills, part of the Western Ghats, are located in Tamil Nadu and Kerala, known for tea plantations and Anamudi, the highest peak in South India."},
    {"name": "Lushai Hills", "location": [23.1645, 92.9376], "description": "The Lushai Hills are located in Mizoram, part of the Patkai range, known for their dense forests and rich cultural heritage."},
    {"name": "Cardamom Hills", "location": [9.5930, 77.1721], "description": "The Cardamom Hills are located in Kerala and Tamil Nadu, named after the cardamom spice grown there and part of the Western Ghats."},
]

st.title("Explore Rivers and Mountains of India")

# Create a map centered around India
m = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add rivers to the map
for river in rivers:
    folium.Marker(
        location=river["location"],
        popup=f"<b>{river['name']}</b><br>{river['description']}",
        icon=folium.Icon(color="blue", icon="tint"),
    ).add_to(m)

# Add mountain ranges to the map
for mountain in mountains:
    folium.Marker(
        location=mountain["location"],
        popup=f"<b>{mountain['name']}</b><br>{mountain['description']}",
        icon=folium.Icon(color="green", icon="cloud"),
    ).add_to(m)

# Display the map
st_folium(m, width=700, height=500)

# User interaction for learning
st.sidebar.title("Learn About India")
option = st.sidebar.selectbox("Choose a Category", ("Rivers", "Mountain Ranges"))

if option == "Rivers":
    st.sidebar.subheader("Rivers")
    for river in rivers:
        if st.sidebar.button(river['name']):
            st.subheader(river['name'])
            st.write(river['description'])
elif option == "Mountain Ranges":
    st.sidebar.subheader("Mountain Ranges")
    for mountain in mountains:
        if st.sidebar.button(mountain['name']):
            st.subheader(mountain['name'])
            st.write(mountain['description'])
