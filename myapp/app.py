from flask import Flask,render_template,request
import math

app = Flask(__name__)

def calculate_distance(lat1, lon1, lat2, lon2):
  lat1_rad = math.radians(lat1)
  lon1_rad = math.radians(lon1)
  lat2_rad = math.radians(lat2)
  lon2_rad = math.radians(lon2)

  dlon = lon2_rad - lon1_rad
  dlat = lat2_rad - lat1_rad
  a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
  radius = 6371
  distance = radius * c

  return distance

@app.route("/", methods=['POST','GET'])
def calculate():
    distance = ""

    if request.method == 'POST': 
      lat1 = float(request.form.get('lat1'))
      lat2 = float(request.form.get('lat2'))
      lon1 = float(request.form.get('lon1'))
      lon2 = float(request.form.get('lon2'))
      distance = calculate_distance(lat1, lon1, lat2, lon2)
    return render_template("index.html", distance=distance)