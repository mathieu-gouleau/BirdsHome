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

4) download the "server" folder on your machine from github, open a cmd in this folder, write theses commands to run the server:
- Set FLASK_APP= BirdHouse_server.py
- flask run -h "IP Adress"

you need to paste your Ipv4 Adress that you copied just before 

What the server can do ? 


Get method: 
returns: INT variable 
"http://"your IP Adress":5000/get"
get the data from the server, in this example it's a int variable that increment each time a bird enters the bird house. 

Post method: 
returns: INT variable
"http://"your IP Adress":5000/post"
post the data from arduino, there a list where we append elements each time the PIR sensor detect mouvement.
In this element we got a date and a value.



###IONIC CLIENT### 

The IONIC app is in the folder "Client", it's a simple app in order to see on your phone if birds have passed . 

1) Install node on your machine, follow this link : "https://nodejs.org/fr/"
2) open a cmd and run this command : 
- npm install -g @ionic/cli native-run cordova-res
- npm i -g native-run@latest

Then if you want to install on an android device you gonna need to change severals things it's very important if you want it to work :

1)download the "server" folder on your machine from github, GO to the "Client" folder, then in the "src" folder", then in the "app" folder, then in the "service" folder and then open with your editor the "data.service.ts" file. Path: "Client\src\app\service"
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

The idea of the project is to have a sensor which gonna detect if birds came into the bird house. We need to have to have an energy independent modul, that we will never touch again until 1 years. The setup is located outside, we also need to make something waterproof. 

###EQUIPMENT##
To make the setup you can follow this TUTO, it's well detailled and well explained. ==> https://randomnerdtutorials.com/power-esp32-esp8266-solar-panels-battery-level-monitoring/


This tuto is only for the energy part, for our project we globaly need:
- ESP32 ==>
https://www.amazon.fr/AZ-Delivery-NodeMCU-d%C3%A9veloppement-d%C3%A9nergie-successeur/dp/B071P98VTG/ref=sxts_sxwds-bia-wc-p13n1_0?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&cv_ct_cx=esp32&dchild=1&keywords=esp32&pd_rd_i=B071P98VTG&pd_rd_r=153390f1-9788-42c5-9e34-84cc4c6ccd4e&pd_rd_w=cXAUZ&pd_rd_wg=OCVqG&pf_rd_p=b7b6f9d7-ff29-487f-946f-367a6949f052&pf_rd_r=2YBFMJ11N9C55DP8C2KN&psc=1&qid=1588274358&sr=1-1-c8b680f7-0dc9-4abe-aa5a-ccfde0ac07ae

- PIR movement detector module (HC-SR501) ==>
https://www.amazon.fr/AZDelivery-sr04-Capteur-ultrasons-T%C3%A9l%C3%A9m%C3%A8tre-Raspberry/dp/B07CNBYRQ7/ref=sr_1_2_sspa?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=HC-SR501&qid=1588274264&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyQkcxM1M5UVBLNjAmZW5jcnlwdGVkSWQ9QTAzNzcyOTEyREJUMlZGQkxJOVFBJmVuY3J5cHRlZEFkSWQ9QTA4NDU1NjcxTDhTUEw2T0RMM1pEJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==


Then connect your PIR sensor with the esp323 card ==>

-plug the GND pin to the GND pin of the esp32
-plug the 5v pin to the 5v piof th esp32
-plug the data pin(the middle one) to the GPIO33pin of the esp32 


###ESP32 CODE###

To use esp32 you need to follow this procedure: 

1) download arduino IDE and install it on your machine ==> https://www.arduino.cc/en/main/software

2) Install the dependencies for esp32 
follow this link it's well explained ==>https://randomnerdtutorials.com/installing-the-esp32-board-in-arduino-ide-windows-instructions/

3)download my code on your machine, it's the "arduino" file.

4)Where there is "PUT YOUR WIFI ID" , "PUT YOUR WIFI MDP" , "PUT YOUR IP ADRESS" , write your own data(IP ADRESS is the IP Adress of where you run your python server) 

ex:
const char* ssid = "sfrtavez";

const char* password =  "carotte2020";

http.begin("http://192.166.25.3:5000/post");

3) Try to DEPLOY the code into your ESP32, you could have problem with the usb cable and with the reset button ===>
- try different usb cable, i think old usb cables are not adapted( i tryed 6 differents usb cable until i found the good one)
- when you got the message " connecting.......___' push the button reset 5sec and then it will deploy on your card



4) Voila your ESP32 his sending to your python server data each time someone pass in front of the PIR sensor.




