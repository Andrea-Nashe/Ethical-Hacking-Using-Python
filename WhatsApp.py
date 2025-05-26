import pywhatkit

phone_number = "+263788202721"  # Replace with the recipient's phone number
message = "Hello, this is a test message from Python!"  # Replace with your message 
time_hour = 1  # Replace with the hour you want to send the message (24-hour format)
time_minute = 1  # Replace with the minute you want to send the message        

pwk = pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_minute, 15, True, 2)
print("Message sent successfully!")