import tkinter as tk

import requests

import requests
import datetime

def getcoviddata():
    api="https://disease.sh/v3/covid-19/all"
    json_data=requests.get(api).json()
    total_cases=str(json_data['cases'])
    total_deaths=str(json_data['deaths'])
    today_cases=str(json_data['todayCases'])
    today_recovered=str(json_data['todayRecovered'])
    updated_at=json_data['updated']
    date=datetime.datetime.fromtimestamp(updated_at/1e3)
    label.config(text="total caese : "+ total_cases + "\n"
                 + "total deaths : " + total_deaths + "\n"
                 + "today deaths : " + total_deaths + "\n"
                 + " today recovered : " + today_recovered)
    label2.config(text=date)




canvas=tk.Tk()
canvas.geometry("400x400")
canvas.title("corona tracker ")

f=("poppins",15,"bold")

button=tk.Button(canvas,font=f,text="load",command=getcoviddata)
button.pack(pady=20)

label=tk.Label(canvas,font=f)
label.pack(pady=20)

label2=tk.Label(canvas,font=f)
label2.pack(pady=20)
getcoviddata()
canvas.mainloop()
