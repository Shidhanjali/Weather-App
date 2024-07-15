from tkinter import*
from tkinter import ttk
import requests

# city="jodhpur"
# data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+" &appid=0ba527d87ae8542233642cf8a867834e").json()
# print(data)

# def data_get():
#     city=city_name.get()
#     data=requests.get("https://api.openweathermap.org/data/2.5/weather?q={city}&appid=0ba527d87ae8542233642cf8a867834e").json()
#     wc_label1.config(text=data["weather"][0]["main"])
#     wd_label1.config(text=data["weather"][0]["description"])
#     temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
#     pres_label1.config(text=data["main"]["pressure"])
#     humi_label1.config(text=data["main"]["humidity"])
#     wind_label1.config(text=data["wind"]["speed"])

def data_get():
    city = city_name.get()
    api_key = "0ba527d87ae8542233642cf8a867834e"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    data = requests.get(url).json()
    wc_label1.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pres_label1.config(text=data["main"]["pressure"])
    humi_label1.config(text=data["main"]["humidity"])
    wind_label1.config(text=data["wind"]["speed"])



win=Tk()
win.title("Weather App")
win.config(bg="lightblue")
win.geometry("500x600")


name_label=Label(win,text="Weather App",
                 font=("georgia",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name=StringVar()
list_name=("Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry")
com=ttk.Combobox(win,text="Weather App",
                 values=list_name,
                 font=("georgia",15),
                 textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)




wc_label=Label(win,text="Weather Climate",font=("cambria",12,"bold"))
wc_label.place(x=30,y=260,height=40,width=150)

wc_label1=Label(win,text="",font=("cambria",12,"bold"))
wc_label1.place(x=250,y=260,height=40,width=150)


wd_label=Label(win,text="Weather Description",font=("cambria",11,"bold"))
wd_label.place(x=30,y=310,height=40,width=150)
wd_label1=Label(win,text="",font=("cambria",11,"bold"))
wd_label1.place(x=250,y=310,height=40,width=150)


temp_label=Label(win,text="Temperarure",font=("cambria",12,"bold"))
temp_label.place(x=30,y=360,height=40,width=150)
temp_label1=Label(win,text="",font=("cambria",12,"bold"))
temp_label1.place(x=250,y=360,height=40,width=150)


pres_label=Label(win,text="pressure",font=("cambria",12,"bold"))
pres_label.place(x=30,y=410,height=40,width=150)
pres_label1=Label(win,text="",font=("cambria",12,"bold"))
pres_label1.place(x=250,y=410,height=40,width=150)


humi_label=Label(win,text="Humidity",font=("cambria",12,"bold"))
humi_label.place(x=30,y=460,height=40,width=150)
humi_label1=Label(win,text="",font=("cambria",12,"bold"))
humi_label1.place(x=250,y=460,height=40,width=150)


wind_label=Label(win,text="wind speed",font=("cambria",12,"bold"))
wind_label.place(x=30,y=510,height=40,width=150)
wind_label1=Label(win,text="",font=("cambria",12,"bold"))
wind_label1.place(x=250,y=510,height=40,width=150)


done_button=Button(win,text="Done",
                 font=("georgia",15,"bold"), command=data_get)
done_button.place(x=200,y=190,height=50,width=100)

win.mainloop()















