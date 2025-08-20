import tkinter as tk
import requests 

API_KEY = "PUT YOUR KEY HERE"  #put your key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")

        #size of the app
        window_width = 400
        window_height = 500
        x , y  = self.situation_app(window_width , window_height)
        self.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        #font and color
        self.resizable(False, False)
        self.bg_color = "#6b6e6c"
        self.text_color = "#eeeeee"
        self.bg_btn = '#d93030'
        self.font = ("Segoe UI", 14)
        self.configure(bg=self.bg_color)

        #Input and Output frame
        input_error_frame = tk.Frame(self, bg=self.bg_color)
        input_error_frame.pack(pady = 10,padx = 10 , side = "top")

        output_frame = tk.Frame(self,bg = self.bg_color)
        output_frame.pack(pady = 10 , padx = 20 , side = "top")

        #Label for the question
        self.ask_label = tk.Label(
            input_error_frame,
            text="Enter the city :",
            fg=self.text_color,
            bg=self.bg_color,
            font=self.font,
            justify= "center"
        )
        self.ask_label.pack(pady=(20, 5))

        #getting the input
        self.entry_city = tk.Entry(
            input_error_frame,
            font=self.font,
            width=25,
            justify="center" 
        )
        self.entry_city.pack(pady=(10, 10))

        #button for submit
        self.click_btn = tk.Button(input_error_frame , text = "Get the weather" , font = self.font , bg = self.bg_btn , fg = self.text_color , justify= "center" , command= self.get_weather)
        self.click_btn.pack(pady = 10 , padx = 10)

        #label for error
        self.error_label = tk.Label(
            input_error_frame,
            text = '',
            font = self.font ,
            bg = self.bg_color , 
            fg = self.text_color,
            justify = "center"
        )
        self.error_label.pack(pady = 10 , padx = 10) 

        #showing the result
        self.result_label = tk.Label(output_frame , font = self.font , justify= "center" , text = "" , bg = self.bg_color)
        self.result_label.pack(padx = 10 , pady  =10)
    #how to place app
    def situation_app(self , width , height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) //4
        y = (screen_height - height)//4
        return x,y

    #getting the information
    def get_weather(self):
        #delete the error if it exists
        self.error_label.config(text = "")

        #delete the previous result
        self.result_label.config(text = "")

        city = self.entry_city.get()
        if not city :
            self.error_label.config(text = "Plaese Enter a City")
            return
        params  = {
            "q":city,
            "appid":API_KEY,
            "units":"metrics",
            "lang":"eng"
        }
        try :
            response = requests.get(BASE_URL , params = params)
            data = response.json()
            if data['cod'] != 200:
                self.error_label.config(text = f"An error : {data['message']} ")
                return
            else:
                temp = data["main"]["temp"]
                weather = data["weather"][0]["description"]
                humidity = data["main"]["humidity"]
                wind = data["wind"]["speed"]
                weather_text = (
                f"City: {city.title()}\n"
                f"Temperature: {temp}°C\n"
                f"Weather: {weather}\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind} m/s"
                 )
                self.result_label.config(text = weather_text)
        except Exception as e :
            self.error_label.config(text = "An error occured : " + str(e))
                
if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
