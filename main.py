#Guanchen Liu
#SLDP project
#20190403
from flask import Flask, render_template
import serial
app = Flask(__name__)
#arduinoData = serial.Serial('/dev/cu.usbserial-DN050M9K', 9600) #com -> devicename connects to arduino


@app.route("/")
def scratch():
    #serialData = (arduinoData.readline().strip()) #comment out if not connected to arduino
    #serialData = serialData.decode('utf-8')
    serialData = "dasfasfafa, asdfasf" #mock data
    serialData1, serialData2 = serialData.split(', ')

    return render_template("scratch.html", serialData1=serialData1, serialData2=serialData2)

'''@app.route("/about") #about page if needed
def about():
    return render_template("about.html")'''

if __name__ == "__main__":
    app.run(debug=True)