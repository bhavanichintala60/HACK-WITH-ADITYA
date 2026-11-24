from flask import Flask, render_template, request, jsonify
from datetime import datetime, timezone
from math import radians, sin, cos, sqrt, atan2

app = Flask(__name__)
REPORTS = []

# Fictional sample patrols for demonstration only; not real police units.
PATROLS = [
    {"id":"DEMO-01","name":"Demo Patrol A","lat":17.6868,"lng":83.2185,"available":True},
    {"id":"DEMO-02","name":"Demo Patrol B","lat":17.7200,"lng":83.3000,"available":True},
    {"id":"DEMO-03","name":"Demo Patrol C","lat":17.6500,"lng":83.1500,"available":False},
]

def km(a,b,c,d):
    r=6371
    x,y=radians(c-a),radians(d-b)
    h=sin(x/2)**2+cos(radians(a))*cos(radians(c))*sin(y/2)**2
    return 2*r*atan2(sqrt(h),sqrt(1-h))

def priority(category, description):
    # Transparent keyword rules for demo; this is NOT trained AI.
    t=(category+" "+description).lower()
    if any(w in t for w in ["fire","unconscious","life threat","major accident","severe injury","trapped","robbery","landslide"]): return "High"
    if any(w in t for w in ["accident","injury","blocked","medical"]): return "Medium"
    return "Low"

def nearest_patrol(lat,lng):
    if lat is None or lng is None: return None
    available=[p for p in PATROLS if p["available"]]
    if not available: return None
    p=min(available,key=lambda q:km(lat,lng,q["lat"],q["lng"]))
    return {"id":p["id"],"name":p["name"],"distance_km":round(km(lat,lng,p["lat"],p["lng"]),2),
            "note":"Simulated sample patrol; not connected to police dispatch."}

@app.get("/")
def home(): return render_template("index.html")

@app.post("/api/reports")
def create_report():
    d=request.get_json(silent=True) or {}
    if not str(d.get("category","")).strip() or not str(d.get("description","")).strip():
        return jsonify(error="Incident type and description are required."),400
    try:
        lat=float(d["latitude"]) if d.get("latitude") not in ("",None) else None
        lng=float(d["longitude"]) if d.get("longitude") not in ("",None) else None
    except (TypeError,ValueError):
        return jsonify(error="Invalid GPS coordinates."),400
    report={"id":f"RCS-{len(REPORTS)+1:04d}","category":d["category"],
      "description":d["description"][:2000],"language":d.get("language","English"),
      "latitude":lat,"longitude":lng,"created_at":datetime.now(timezone.utc).isoformat(),
      "priority":priority(d["category"],d["description"]),"status":"Received (demo)",
      "patrol":nearest_patrol(lat,lng)}
    REPORTS.append(report)
    return jsonify(message="Demo report received.",report=report),201

@app.get("/api/reports")
def get_reports(): return jsonify(list(reversed(REPORTS)))

if __name__=="__main__": app.run(debug=True,host="127.0.0.1",port=5000)
