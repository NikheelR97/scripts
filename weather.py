import schedule
import time

def get_weather(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}}&longitude={longitude}}&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    response = requests.get(base_url)
    data = response.json()
    return data

def send_message(body):
    account_sid = "twilio_sid"
    auth_token = "twilio_token"
    from_phone_no = "from_phone_no"
    to_phone_no = "to_phone_no"

    client = Client(account_sid,auth_token)

    message = client.messages.create(
        body=body,
        from=from_phone_no,
        to=to_phone_no
    )

    print("Text Message Sent")

def send_weather_update():
    latitude = -29.7043
    longitude = 30.9761

    weather_data = get_weather(latitude, longitude)
    temperature_celcius = weather_data["hourly"]["temperature_2m"][0]
    humidity = weather_data["hourly"]["relativehumindty_2m"][0]
    windspeed = weather_data["hourly"]["windspeed_10m"][0]

    weather_info = (
        f"Good Morning!"\n
        f"Current weather in Phoenix:"\n
        f"Temperature: {temperature_celcius}"\n
        f"Humidity: {humidity}"\n
        f"Wind Speed: {windspeed}"
    )

    send_message(weather_info)

def main():
    schedule.every().day.at("08:00").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep(1)