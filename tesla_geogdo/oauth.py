import os
import requests
import time

ADDON_OPTIONS = {
    "client_id": os.getenv("CLIENT_ID", ""),
    "client_secret": os.getenv("CLIENT_SECRET", ""),
    "redirect_uri": os.getenv("REDIRECT_URI", ""),
    "refresh_token": os.getenv("REFRESH_TOKEN", ""),
    "latitude": float(os.getenv("LATITUDE", "0")),
    "longitude": float(os.getenv("LONGITUDE", "0")),
    "radius": int(os.getenv("RADIUS", "100"))
}

def refresh_access_token():
    token_url = "https://auth.tesla.com/oauth2/v3/token"
    data = {
        "grant_type": "refresh_token",
        "client_id": ADDON_OPTIONS["client_id"],
        "client_secret": ADDON_OPTIONS["client_secret"],
        "refresh_token": ADDON_OPTIONS["refresh_token"],
        "scope": "openid email offline_access"
    }
    response = requests.post(token_url, json=data)
    response.raise_for_status()
    tokens = response.json()
    return tokens["access_token"]

def main():
    try:
        token = refresh_access_token()
        print(f"[INFO] Access token refreshed.")

        # Add Tesla API vehicle location poll logic here
        # Compare with latitude/longitude & trigger garage door

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
