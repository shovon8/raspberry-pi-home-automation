# Running the App
Clone the GitHub repository:
> git clone https://github.com/shovon8/raspberry-pi-home-automation.git

Navigate to the newly created project directory:
> cd raspberry-pi-home-automation

Navigate to static/ directory:
> cd static

Download Font Awesome:
> wget https://use.fontawesome.com/releases/v5.15.1/fontawesome-free-5.15.1-web.zip

Unzip Font Awesome in the static/ directory:
> unzip fontawesome-free-5.15.1-web.zip

Rename Font Awesome directory to fontawesome/:
> mv -v fontawesome-free-5.15.1-web fontawesome

Navigate to the project root:
> cd ..

Copy the systemd service to /etc/systemd/system/:
> sudo cp -v raspi-home-automation.service /etc/systemd/system/

Reload the systemd daemons:
> sudo systemctl daemon-reload

Add the systemd service to the system startup:
> sudo systemctl enable raspi-home-automation.service

For the changes to take effect, reboot the Raspberry Pi:
> sudo reboot

Check if the systemd service is active/running:
> sudo systemctl status raspi-home-automation.service

Find the IP address of your Raspberry Pi:
> hostname -I

Access the Web App from your favorite web browser at `http://<ip-addr>:5000`



# NOTE: 
Make sure to change the appliance data and pin numbers as required in the `server.py` script. 
