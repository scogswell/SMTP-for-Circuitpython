# SMTP Support for Circuitpython

This is a routine which enables sending SMTP email messages from an embedded device running Circuitpython.  

This is based on uMail (MicroMail) for MicroPython by Shawwwn https://github.com/shawwwn/uMail

This has been tested on ESP32-S2 and ESP32-S3 and Pico-w platforms running Circuitpython 8.x. Tested with gmail smtp using App Passwords.  https://support.google.com/accounts/answer/185833?hl=en.  Hopefully it works with other SMTP servers.  

This supports SSL (port 465) and STARTTLS (port 587) connections, but currently STARTTLS connections on ESP32 will cause a hard fault. (See https://github.com/adafruit/circuitpython/issues/7314 ).  STARTTLS connections work fine on Pico-w. You probably should use `use_ssl=True` from the start anyway rather than relying on STARTTLS. 

The library uses `binascii` internally which is usually a builtin on ESP32 and Pico-w platforms.

You can pass `debug=True` during initialization to enable printing out the message transactions between Circuitpython and the SMTP server.  

This falls into the category of "works for me" but I can only do limited testing. It may not work for you. An example program is included in `code.py`/`secrets.py`

Example usage snippet:
```py

import smtp_circuitpython

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
```