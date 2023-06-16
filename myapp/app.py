from flask import Flask,render_template,request
import math

app = Flask(__name__)

def calculate_distance(lat1, lon1, lat2, lon2):

  lat1_rad = math.radians(float(lat1))
  lon1_rad = math.radians(float(lon1))
  lat2_rad = math.radians(float(lat2))
  lon2_rad = math.radians(float(lon2))

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
      pointA = request.form.get('pointA')
      pointB = request.form.get('pointB')
      latA, lonA = map(float, pointA.split(','))
      latB, lonB = map(float, pointB.split(','))
      distance = calculate_distance(latA, lonA, latB, lonB)
      distance = "{:.2f}".format(distance)

    distance_with_units = f"{distance} km"
    return render_template("index.html", distance=distance_with_units)
    return render_template("maps.html")

if __name__ == '__main__':
  app.run()