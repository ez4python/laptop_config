import subprocess

def get_connected_wifi():
    try:
        # Get only the SSID of the connected WiFi
        result = subprocess.run(
            ['nmcli', '-t', '-f', 'active,ssid', 'dev', 'wifi'],
            capture_output=True, text=True, check=True
        )
        # Look for the line where 'active' is 'yes'
        for line in result.stdout.splitlines():
            if line.startswith("yes:"):
                wifi_name = line.split(":")[1]  # Extract SSID
                print(wifi_name)
                return
        print("No WiFi connected")  # If no active connection is found
    except subprocess.CalledProcessError as e:
        print("Error fetching WiFi info:", e)

if __name__ == "__main__":
    get_connected_wifi()
