import tkinter as tk
import requests
from PIL import Image, ImageTk
import io

class WeatherApp:
    def __init__(self, master):
        self.master = master
        master.title("Weather Application")
        master.geometry("300x400")

        self.city_entry = tk.Entry(master)
        self.city_entry.pack(pady=10)

        self.search_button = tk.Button(master, text="Search", command=self.get_weather)
        self.search_button.pack(pady=5)

        self.location_label = tk.Label(master, text="")
        self.location_label.pack(pady=5)

        self.temp_label = tk.Label(master, text="")
        self.temp_label.pack(pady=5)

        self.desc_label = tk.Label(master, text="")
        self.desc_label.pack(pady=5)

        self.icon_label = tk.Label(master)
        self.icon_label.pack(pady=5)

    def get_weather(self):
        city = self.city_entry.get()
        api_key = "YOUR_API_KEY_HERE"  # Replace with your OpenWeatherMap API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            self.location_label.config(text=f"Location: {data['name']}, {data['sys']['country']}")
            self.temp_label.config(text=f"Temperature: {data['main']['temp']}°C")
            self.desc_label.config(text=f"Description: {data['weather'][0]['description']}")

            icon_url = f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
            icon_response = requests.get(icon_url)
            icon_image = Image.open(io.BytesIO(icon_response.content))
            icon_photo = ImageTk.PhotoImage(icon_image)
            self.icon_label.config(image=icon_photo)
            self.icon_label.image = icon_photo
        else:
            self.location_label.config(text="Error fetching weather data")

root = tk.Tk()
app = WeatherApp(root)
root.mainloop()