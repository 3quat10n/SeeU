import folium

def plot(ip,latitude, longitude):

    folium.Marker(
        location=[latitude, longitude],
        popup=f"Location:{latitude},{longitude}\nIP:{ip}",
    ).add_to(map_object)

map_object = folium.Map(location=[0, 0], zoom_start=2)

data = open("ips.txt","r")

for line in data.readlines():
    cord = line.strip().split(";")
    ip , latitude , longitude = cord[0] , cord[1] , cord[2]
    plot(ip,latitude,longitude)

data.close()
map_object.save("map.html")

print("[+] map.html")