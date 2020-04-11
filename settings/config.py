
import os



## App settings
name = "Virus Forecaster"

host = "0.0.0.0"

port = int(os.environ.get("PORT", 5000))

threaded = False

debug = True

contacts = "https://www.linkedin.com/in/mauro-di-pietro-56a1366b/"

code = "https://github.com/mdipietro09/FlaskApp_VirusForecaster"

fontawesome = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'

logo = "logo.jpg"



## File system
root = os.path.dirname(os.path.dirname(__file__)) + "/"



## DB
