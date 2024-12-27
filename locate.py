import folium
import requests


def plot(ip,latitude, longitude):
    # Plot point on the map
    folium.Marker(
        location=[latitude, longitude],
        popup=f"{ip}",
    ).add_to(map_object)


def aproximation(ip):
    r = requests.get(f"http://ip-api.com/json/{ip}")  # Getting aproximation latitude and longitude using ip-api 
    
    with open(ip, 'w') as file:                       # Write ip information 
        file.write(r.text)
    
    return r.json()['lat'] , r.json()['lon'] 

map_object = folium.Map(location=[0, 0], zoom_start=2)

data = open("ips.txt","r")

for line in data.readlines():
    cord = line.strip().split(";")
    ip , latitude , longitude = cord[0] , cord[1] , cord[2]

    if cord[1] == "None":
        latitude,longitude = aproximation(ip)
        print(f"[~] Target {ip} Found aproximation address")
    else:
        print(f"[+] Target {ip} Found ({latitude},{longitude})")
    
    plot(ip,latitude,longitude)


data.close()
map_object.save("map.html")

print("[+] map.html")
