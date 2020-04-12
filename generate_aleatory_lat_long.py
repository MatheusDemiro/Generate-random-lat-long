# In[27]:


import pandas as pd
import random
import folium
import pycristoforo as pyc

# Link: https://stackoverflow.com/questions/30246435/generate-random-data-with-lat-long/30247616 
# By: Scott
def generate_random_data(lat, lon, num_rows):
    points = {"lat": [], "lng": []}
    for _ in range(num_rows):
        hex1 = '%012x' % random.randrange(16**12) # 12 char random string
        flt = float(random.randint(0,100))
        dec_lat = random.random()/100
        dec_lon = random.random()/100

        points["lat"].append(lat + dec_lat)
        points["lng"].append(lon + dec_lon)
    return points


# In[41]:


center = (-8.047692, -34.887040)

points = pd.DataFrame(data=generate_random_data(center[0], center[1], 100))

recife_antigo = folium.Map(
    location=[points.median()[1], points.median()[0]],
    zoom_start=15
)

# In[42]:


for i in points.values:
    folium.Marker(
        location=[i[1], i[0]],
    ).add_to(recife_antigo)

recife_antigo


# In[ ]:




