# Make a Birds Home Connected via Flask Server, an IONIC APP and Arduino setup
Birds home project 

This project is a Bird's home connected in local server. I use a python flask server to get the data, an ionic app to display the data on a phone and an arduino setup which send data to the python server. In order to run the project you will need differents things, that i will explain in each part. 



###FLASK SERVER###

The flask server is in the folder "server", if you want to use it and run it  FOLLOW theses commands: 

1) install python on your machine and don't forget to check the " Add Python3.7 to PATH" box : https://www.python.org/downloads/ 
1) open a cmd and write theses commands: 
- pip install flask 
- pip install flask-cors --upgrade

3) open an other cmd an write this command: 
- ipconfig 
==> write your Ipv4 Address or copy it ( it's something like "192.168.x.y") 

4) open the folder where the "server" folder is and open a cmd in this folder, write theses commands to run the server:
- Set FLASK_APP= BirdHouse_server.py
- flask run -h "IP Adress"

you need to paste your Ipv4 Adress that you copied just before 

What the serveur can do ? 


Get method: 
returns: INT variable 
"http://"your IP Adress":5000/get"
get the data from the server, in this example it's a int variable that increment each time a bird enters the bird house. 

Post method: 
returns: INT variable
"http://"your IP Adress":5000/post"
post the data from arduino


###IONIC CLIENT### 

The IONIC app is in the folder "Client", it's a simple app in order to see on your phone if birds have passed . 

1) Install node on your machine, follow this link : "https://nodejs.org/fr/"
2) open a cmd and run this command : 
- npm install -g @ionic/cli native-run cordova-res
- npm i -g native-run@latest

Then if you want to install on an android device you gonna need to change severals things it's very important if you want it to work :

1)GO to the "Client" folder, then in the "src" folder", then in the "app" folder, then in the "service" folder and then open with your editor the "data.service.ts" file. Path: "Client\src\app\service"
==>  in the function "getDatafromBirdHouse()' write  yout ip adress where i wrote "PUT YOUT IP ADRESS". 
ex: " return this.httpclient.get("http://192.167.6.64:5000/get",httpOptions) "



3)plug your phone one your computer, you will have to enable the debug mode or developer mode on your device, follow this video it's well explained: https://www.youtube.com/watch?v=Jf4RydXv7X8

3) Open a cmd in the "client" folder and run this command
- ionic build android

2)GO to the "Client" folder, then in the "resources" folder, then in the "android" folder, then in the "xml" folder and open the file "network_security_config.xml" with your editor. Path: "Client\resources\android\xml".
==> add this line "<domain>PUT YOUT IP ADRESS</domain>" line just bellow thsi line :
"<domain includeSubdomains="true">localhost</domain>", and don't forget to change the text "PUT YOUT IP ADRESS" still by your own ip adress. 
ex:" <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">localhost</domain>
        <domain>192.167.6.64</domain>
    </domain-config> "

4) Re Open a cmd in the "client" folder and re-run this command
- ionic build android

5) follow the path in the cmd "Client\platforms\android\app\build\outputs\apk\debug"
==> copy the file "app-debug.apk" on your device and then run this file on your device

Voila you can see the data on your phone now ( if the arduino is set up of course) ! Don't forget to connect your phone and yout computer to the same network of course ! 


###ARDUINO SETUP###







