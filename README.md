# rpi-fb-weather

Raspberry pi based project that gets weather info from OpenWeather API and sends it as a facebook message every morning.

To run it:
* Clone the repository.
* Set up data/config.yaml as follows:

```
#OpenWeather API configuration
url: http://api.openweathermap.org/data/2.5/forecast?
defaultCity: <your-default-city>
appKey: <your-app-key-from-Openweathermap>
fbUsername: <your-facebook-username>
password: <your-facebook-password>
usersToSend: [<list-of-friends-to-send>]
```
* Install required libraries from requirements.txt (`pip install -r requirements.txt`)
* Create `/logs` directory where logs.log file will be saved.
* Run `python main -env=prod/dev` command: `prod` version sends the message to selected users, `dev` - prints it to the console.
* If you want additional information/delay time/error log - check `logs/logs.log` file.