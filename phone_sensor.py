import time
import requests


PHONE_IP = "http://10.153.165.222:8080"  

URL = f"{PHONE_IP}/get?accX&accY&accZ"

print("📡 Connecting to smartphone telemetry stream...")
print("Move your phone around to see live data! Press Ctrl+C to stop.\n")

try:
    while True:
        response = requests.get(URL)
        data = response.json()
        
        x = data['buffer']['accX']['buffer'][0]
        y = data['buffer']['accY']['buffer'][0]
        z = data['buffer']['accZ']['buffer'][0]
        
        status = "Stable"
        if abs(x) > 5.0 or abs(y) > 5.0 or abs(z) > 5.0:
            status = "🚨 phone ah olunga pudi!"

        print(f"X: {x:+.2f} | Y: {y:+.2f} | Z: {z:+.2f} --> Status: {status}")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n🛑 Telemetry stream stopped.")
except Exception as e:
    print(f"\n❌ Error. Detail: {e}")
