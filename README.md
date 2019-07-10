1. First need to install python modules, open up terminal and run

 pip install flask socketio flask-socketio

 to install all the modules needed to run

2. Run python app.py, this is the starting up the server

3. Once you run python app.py, there should be a link, mine was

 http://127.0.0.1:5000
 
 This will establish the user connection to the server. It will connect to /user namespace (essentiallity a different channel)

 The server should then tell you that a user has connected.

3. Open another terminal window and run python pi.py, this will establish pi's socket connection to the server.
 It will connect to /pi namespace\s

 The server should then tell you that a pi has connected.\s\s

 It'll take you to a web page with a simple button named 'Blazers' for blazers theme, I just chose a random one.

4. If you open up developer console you should see that when you establish a connection, an event
 will be triggered to the server notifying that the user joined. 

5. Click the button, this will send the value of the button to the server,
 and ultimately be forwared to the pis, then the pis will respond with a response
 to the server and ultimately the user.