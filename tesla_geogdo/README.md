# Tesla Garage Door Opener

This Home Assistant add-on triggers your garage door when your Tesla enters a defined radius using Tesla API.

## Configuration

Edit `configuration.yaml` in Home Assistant UI or use Add-on options:

```yaml
client_id: "your-client-id"
client_secret: "your-client-secret"
redirect_uri: "https://your-home-assistant-url/auth/external/callback"
refresh_token: "your-refresh-token"
latitude: "51.0848"
longitude: "-114.1291"
radius: 100
