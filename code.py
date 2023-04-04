# SMTP with Circuitpython demo program
# Steven Cogswell
#
# Note the library requires adafruit_binascii in /lib for base64 encoding, or 
# binascii in your builtin functions. 

import wifi
import ssl
import socketpool
import smtp_circuitpython

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

# Connect to WiFi
try:
    from secrets import secrets
except ImportError:
    print("WiFi and Email credentials are kept in secrets.py - please add them there!")
    raise
print("Connecting to %s" % secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s, IPv4 address %s" % (secrets["ssid"],wifi.radio.ipv4_address))

# Create a socket pool and SSL context
pool = socketpool.SocketPool(wifi.radio)
ssl_context = ssl.create_default_context()

mail_to = "your-recipient@example.com"
mail_subject="Email Test"
mail_body= "This is an email test from Circuitpython\r\n"
mail_body += "IP Address is "+str(wifi.radio.ipv4_address)

smtp = smtp_circuitpython.SMTP(host=SMTP_SERVER, port=SMTP_PORT,
            pool=pool, ssl_context=ssl_context, use_ssl = True,
            username=secrets['gmail_user'],password=secrets['gmail_password'],
            debug = True)
smtp.to(mail_to)
smtp.body("Subject: "+mail_subject+"\r\n\r\n"+mail_body)
smtp.quit()