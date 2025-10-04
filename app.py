from flask import Flask, render_template, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/auto_threshold", methods=["POST"])
def get_auto_threshold():
    """
    This simulates samples and auto threshold calculation.
    """
    data = request.get_json()
    variable = data.get("variable")
    lat = data.get("lat")
    lon = data.get("lon")
    day = int(data.get("day"))

    # Simulate data based on variable
    if variable == "temperature":
        mean = 30
    elif variable == "precipitation":
        mean = 10
    elif variable == "windspeed":
        mean = 5
    elif variable == "airquality":
        mean = 80
    else:
        mean = 20

    samples = np.random.normal(mean, mean*0.2, 30).tolist()  # 30 sample points
    threshold = round(np.mean(samples) + np.std(samples), 2)

    return jsonify({"threshold": threshold, "samples": samples})

if __name__ == "__main__":
    app.run(debug=True)
