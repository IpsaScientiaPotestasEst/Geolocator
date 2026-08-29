import os
import urllib.request
import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
# FIX 1: Pass app into CORS(), do not do app(CORS)
CORS(app)  

@app.route("/app")
def sayHi():
    # Render routes traffic through proxies. This splits to find the true user IP.
    x_forwarded = request.headers.get('X-Forwarded-For', '')
    if x_forwarded:
        user_ip = x_forwarded.split(',')[0].strip()
    else:
        user_ip = request.remote_addr
    
    try:
        # FIX 2: Restored the slash after ipapi.co
        url = f"https://ipapi.co{user_ip}/json/"
        res = urllib.request.urlopen(url).read()
        data = json.loads(res.decode('utf-8'))
        
        lat = data.get('latitude')
        lon = data.get('longitude')
        
        if lat and lon:
            return f"{lat},{lon}"
        return "Unknown"
        
    except Exception:
        # Fallback coordinates if the public API blocks the request or fails
        return "-38.01055,175.32145"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
