# In[5]:


import pandas as pd
import random
import folium

# Link: https://stackoverflow.com/questions/30246435/generate-random-data-with-lat-long/30247616 
# By: Scott
def generate_random_data(lat, lon, num_rows):
    points = {"lat": [], "lng": []}
    for _ in range(num_rows):
        lt = random.uniform(-1, 1)*radius + latitude
        lng = random.uniform(-1, 1)*radius + longitude

        points["lat"].append(lt)
        points["lng"].append(lng)
    return points


# In[12]:


center = (-8.047692, -34.887040)

points = pd.DataFrame(data=generate_random_data(center[0], center[1], 0.0002, 10))

recife_antigo = folium.Map(
    location=[center[0], center[1]],
    zoom_start=15
)


# In[13]:


for i in points.values:
    folium.Marker(
        location=[i[0], i[1]],
    ).add_to(recife_antigo)

recife_antigo


# In[ ]:




