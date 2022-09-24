import json
from plotly.graph_objs import Layout
from plotly import offline

filename = 'data/eq_data_30_day_m1.json'
with open(filename) as data:
    earthquake_data = json.load(data)

earthquake_dicts = earthquake_data['features']

magnitudes, longs, lats, hover_text = [], [], [], []
for x in earthquake_dicts:
    magnitudes.append(x['properties']['mag'])
    longs.append(x['geometry']['coordinates'][0])
    lats.append(x['geometry']['coordinates'][1])
    hover_text.append(x['properties']['title'])
# ---------------------------------------------------- Visualization Code -------------------------------------------
map_data = [{
    'type': 'scattergeo',
    'lon': longs,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [5*mag for mag in magnitudes],
        'color': magnitudes,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar':{'title': 'Magnitude'}
    }
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': map_data, 'layout': my_layout}

offline.plot(fig, filename='global_earthquakes.html')