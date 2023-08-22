from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk
import pyowm
from tkinter.font import Font

root=Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg='#57adff')
root.resizable(False,False)


def getWeather():
    city=textfield.get()

    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()

    result=obj.timezone_at(lng=location.longitude,lat=location.latitude)

    

    location_info = f" {location.address}\nLatitude: {round(location.latitude,4)} °N\nLongitude: {round(location.longitude,4)} °E "
    long_lat.config(text=location_info)


    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    #weather
    #api=f"https://api.openweathermap.org/data/2.5/weather?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=c51e914d394463d5420402223fc86cc3"
    
    #api=f"https://api.openweathermap.org/data/3.0/onecall?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&units=metric&exclude=hourly&appid=c51e914d394463d5420402223fc86cc3"
    api=f"https://api.openweathermap.org/data/2.5/forecast?q="+city+"&appid=001bce92ce017bb66a426009bea31bf5"
    
    json_data=requests.get(api).json()

    
    
    
    for entry in json_data['list']:
        
        temperature = entry['main']['temp']
        humidity = entry['main']['humidity']
        pressure = entry['main']['pressure']
        wind_speed = entry['wind']['speed']
        weather_description = entry['weather'][0]['description']

        t.config(text=(temperature,"°C"))
        h.config(text=(humidity,"%"))
        p.config(text=(pressure,"hPa"))
        w.config(text=(wind_speed,"m/s"))
        d.config(text=(weather_description))

 

    #timezone.config(text=result)
    #long_lat.config(text=f"{location.latitude}{location.longitude}")


    #1stcell
    firstdayimage=json_data['list'][0]['weather'][0]['icon']
    img=(Image.open(f"icons/{firstdayimage}@2x.png"))
    resized_image=img.resize((50,50))
    photo1=ImageTk.PhotoImage(resized_image)
    firstimage.config(image=photo1)
    firstimage.image=photo1
    firstimage.place(x=15, y=50)
    
    '''photo1=ImageTk.PhotoImage(file=f"images/cc.png")
    firstimage.config(image=photo1)
    firstimage.image=photo1
    firstimage.place(x=35, y=50)'''

    small_font = Font(size=10)

    first_day_data = json_data['list'][0]
    tempday1 = first_day_data['main']['temp_max']
    tempnight1 = first_day_data['main']['temp_min']

    
    day1temp.config(text=f"Day: {tempday1}°C\nNight: {tempnight1}°C", anchor='center',font=small_font)
    day1temp.place(x=100,y=20)
    
    #2ndcell
    seconddayimage=json_data['list'][1]['weather'][0]['icon']
    img=(Image.open(f"icons/{seconddayimage}@2x.png"))
    resized_image=img.resize((40,40))
    photo2=ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.image=photo2
    secondimage.place(x=10, y=40)

    small_font = Font(size=7)

    first_day_data = json_data['list'][1]
    tempday2 = first_day_data['main']['temp_max']
    tempnight2 = first_day_data['main']['temp_min']

    
    day2temp.config(text=f"Day: {tempday2}°C\nNight: {tempnight2}°C", anchor='center',font=small_font)
    day2temp.place(x=1,y=95)


    #3rdcell
    thirddayimage=json_data['list'][2]['weather'][0]['icon']
    img=(Image.open(f"icons/{thirddayimage}@2x.png"))
    resized_image=img.resize((40,40))
    photo3=ImageTk.PhotoImage(resized_image)
    thirdimage.config(image=photo3)
    thirdimage.image=photo3
    thirdimage.place(x=10, y=40)

    small_font = Font(size=7)

    first_day_data = json_data['list'][2]
    tempday3 = first_day_data['main']['temp_max']
    tempnight3 = first_day_data['main']['temp_min']

    
    day3temp.config(text=f"Day: {tempday3}°C\nNight: {tempnight3}°C", anchor='center',font=small_font)
    day3temp.place(x=1.4,y=95)

    #4thcell
    fourthdayimage=json_data['list'][3]['weather'][0]['icon']
    img=(Image.open(f"icons/{fourthdayimage}@2x.png"))
    resized_image=img.resize((40,40))
    photo4=ImageTk.PhotoImage(resized_image)
    fourthimage.config(image=photo4)
    fourthimage.image=photo4
    fourthimage.place(x=10, y=40)

    small_font = Font(size=7)

    first_day_data = json_data['list'][3]
    tempday4 = first_day_data['main']['temp_max']
    tempnight4 = first_day_data['main']['temp_min']

    
    day4temp.config(text=f"Day: {tempday4}°C\nNight: {tempnight4}°C", anchor='center',font=small_font)
    day4temp.place(x=1.4,y=95)

    #5thcell
    fifthdayimage=json_data['list'][4]['weather'][0]['icon']
    img=(Image.open(f"icons/{fifthdayimage}@2x.png"))
    resized_image=img.resize((40,40))
    photo5=ImageTk.PhotoImage(resized_image)
    fifthimage.config(image=photo5)
    fifthimage.image=photo5
    fifthimage.place(x=10, y=40)

    '''tempday1=json_data['list'][0]['temp']['day']
    tempnight1=json_data['list'][0]['temp']['night']

    day1temp.config(text=f"Day:{tempday1}\n Night:{tempnight1}")'''

    small_font = Font(size=7)

    first_day_data = json_data['list'][4]
    tempday5 = first_day_data['main']['temp_max']
    tempnight5 = first_day_data['main']['temp_min']

    
    day5temp.config(text=f"Day: {tempday5}°C\nNight: {tempnight5}°C", anchor='center',font=small_font)
    day5temp.place(x=1.4,y=95)


    small_font = Font(size=10)

    first_day_data = json_data['list'][0]
    tempday1 = first_day_data['main']['temp_max']
    tempnight1 = first_day_data['main']['temp_min']

    #day1temp.config(text=f"Day:{tempday1}\n Night:{tempnight1}")
    day1temp.config(text=f"Day: {tempday1}°C\nNight: {tempnight1}°C", anchor='center',font=small_font)
    day1temp.place(x=77,y=57)
    


    #6thcell
    sixthdayimage=json_data['list'][5]['weather'][0]['icon']
    img=(Image.open(f"icons/{sixthdayimage}@2x.png"))
    resized_image=img.resize((40,40))
    photo6=ImageTk.PhotoImage(resized_image)
    sixthimage.config(image=photo6)
    sixthimage.image=photo6
    sixthimage.place(x=10, y=40)

    small_font = Font(size=7)

    first_day_data = json_data['list'][5]
    tempday6 = first_day_data['main']['temp_max']
    tempnight6 = first_day_data['main']['temp_min']

    
    day6temp.config(text=f"Day: {tempday6}°C\nNight: {tempnight6}°C", anchor='center',font=small_font)
    day6temp.place(x=1.4,y=95)

    #7thcell
    seventhdayimage=json_data['list'][6]['weather'][0]['icon']
    img=(Image.open(f"icons/{seventhdayimage}@2x.png"))
    resized_image=img.resize((40,40))
    photo7=ImageTk.PhotoImage(resized_image)
    seventhimage.config(image=photo7)
    seventhimage.image=photo7
    seventhimage.place(x=10, y=40)

    small_font = Font(size=7)

    first_day_data = json_data['list'][6]
    tempday7 = first_day_data['main']['temp_max']
    tempnight7 = first_day_data['main']['temp_min']

    
    day7temp.config(text=f"Day: {tempday7}°C\nNight: {tempnight7}°C", anchor='center',font=small_font)
    day7temp.place(x=1.4,y=95)
    
    
    #days

    first=datetime.now()
    day1.config(text=first.strftime("%A"))

    second=first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third=first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth=first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth=first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth=first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh=first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))




##icon
image_icon=PhotoImage(file="images/logo.png")
root.iconphoto(False,image_icon)

Round_box=PhotoImage(file="images/1stbox1.1.png")
Label(root,image=Round_box,bg="#57adff").place(x=30,y=125)


#label
label1=Label(root,text="Temperature",font=('Helvetica',11),fg="white",bg="#203243")
label1.place(x=60,y=160)

label2=Label(root,text="Humidity",font=('Helvetica',11),fg="white",bg="#203243")
label2.place(x=60,y=180)

label3=Label(root,text="Pressure",font=('Helvetica',11),fg="white",bg="#203243")
label3.place(x=60,y=200)

label4=Label(root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="#203243")
label4.place(x=60,y=220)

label5=Label(root,text="Decription",font=('Helvetica',11),fg="white",bg="#203243")
label5.place(x=60,y=240)


#search box

Search_image=PhotoImage(file="images/search.png")
myimage=Label(image=Search_image,bg="#57adff")
myimage.place(x=250,y=160)


weat_image=PhotoImage(file="images/cloud.png")
weatherimage=Label(root,image=weat_image,bg="#203243")
weatherimage.place(x=255,y=170)

textfield=tk.Entry(root,justify='center',width=28,font=('poppins',20,'bold'),bg="#203342",border=0,fg="white")
textfield.place(x=300,y=169)
textfield.focus()


Search_icon=PhotoImage(file="images/sear4.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#203243",command=getWeather)
myimage_icon.place(x=692,y=175)

##Bottom Box
frame=Frame(root,width=900,height=185,bg="#212120")
frame.pack(side=BOTTOM)

#bottom boxes
firstbox=PhotoImage(file="images/rr 1.png")
secondbox=PhotoImage(file="images/rrlong1.png")

Label(frame,image=firstbox,bg="#212120").place(x=30,y=5)
Label(frame,image=secondbox,bg="#212120").place(x=250,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=350,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=450,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=550,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=650,y=30)
Label(frame,image=secondbox,bg="#212120").place(x=750,y=30)


##clock to place item
clock=Label(root,font=("Helvetica",30,'bold'),fg='white',bg='#57adff')
clock.place(x=70,y=30)

##timezone
timezone=Label(root,font=("Helvetica",20),fg='white',bg='#57adff')
timezone.place(x=700,y=20)

long_lat=Label(root,font=("Helvetica",10),fg='white',bg='#57adff')
long_lat.place(x=700,y=20)

#thpwd
t=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
t.place(x=160,y=160)

h=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
h.place(x=160,y=180)

p=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
p.place(x=160,y=200)

w=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
w.place(x=160,y=220)

d=Label(root,font=("Helvetica",11),fg="white",bg="#203243")
d.place(x=160,y=240)

#1stcell
firstframe=Frame(root,width=177,height=120,bg="#203243")
firstframe.place(x=44,y=330)

day1=Label(firstframe,font="arial 15",bg="#203243",fg="#fff")
day1.place(x=30,y=7)

firstimage=Label(firstframe,bg="#282829")
firstimage.place(x=1,y=15)

day1temp=Label(firstframe,bg="#203243",fg="#57adff",font="arial  15 bold")
day1temp.place(x=20,y=50)

#2ndcell
secondframe=Frame(root,width=70,height=130,bg="#07075f")
secondframe.place(x=256,y=320)

day2=Label(secondframe,font="arial 10",bg="#07075f",fg="#fff")
day2.place(x=5,y=5)

secondimage=Label(secondframe,bg="#282829")
secondimage.place(x=1,y=15)

day2temp=Label(secondframe,bg="#07075d",fg="#fff",font="arial  15 bold")
day2temp.place(x=10,y=70)

#3rdcell
thirdframe=Frame(root,width=70,height=130,bg="#07075f")
thirdframe.place(x=356,y=320)

day3=Label(thirdframe,font="arial 10",bg="#07075f",fg="#fff")
day3.place(x=5,y=5)

thirdimage=Label(thirdframe,bg="#282829")
thirdimage.place(x=1,y=15)

day3temp=Label(thirdframe,font="arial 10",bg="#07075d",fg="#fff")
day3temp.place(x=10,y=5)

#4thcell
fourthframe=Frame(root,width=70,height=130,bg="#07075f")
fourthframe.place(x=456,y=320)

day4=Label(fourthframe,font="arial 10",bg="#07075f",fg="#fff")
day4.place(x=5,y=5)

fourthimage=Label(fourthframe,bg="#282829")
fourthimage.place(x=1,y=15)

day4temp=Label(fourthframe,font="arial 10",bg="#07075d",fg="#fff")
day4temp.place(x=10,y=5)

#5thcell
fifthframe=Frame(root,width=70,height=130,bg="#07075f")
fifthframe.place(x=556,y=320)

day5=Label(fifthframe,font="arial 10",bg="#07075f",fg="#fff",anchor="center")
day5.place(x=5,y=5)

fifthimage=Label(fifthframe,bg="#282829")
fifthimage.place(x=1,y=15)

day5temp=Label(fifthframe,font="arial 10",bg="#07075d",fg="#fff")
day5temp.place(x=10,y=5)

#6thcell
sixthframe=Frame(root,width=70,height=130,bg="#07075f")
sixthframe.place(x=656,y=320)

day6=Label(sixthframe,font="arial 10",bg="#07075f",fg="#fff")
day6.place(x=5,y=5)

sixthimage=Label(sixthframe,bg="#282829")
sixthimage.place(x=1,y=15)

day6temp=Label(sixthframe,font="arial 10",bg="#07075d",fg="#fff")
day6temp.place(x=10,y=5)

#7thcell
seventhframe=Frame(root,width=70,height=130,bg="#07075f")
seventhframe.place(x=756,y=320)

day7=Label(seventhframe,font="arial 10",bg="#07075f",fg="#fff")
day7.place(x=5,y=5)

seventhimage=Label(seventhframe,bg="#282829")
seventhimage.place(x=1,y=15)

day7temp=Label(seventhframe,font="arial 10",bg="#07075d",fg="#fff")
day7temp.place(x=10,y=5)


root.mainloop()