import os
import smtplib
from email.message import EmailMessage
import imghdr

# Access Email and Password saved in Environment Variables
EMAILADDRESS = os.environ.get('MYEMAIL_ADDRESS')
EMAILPASSWORD = os.environ.get('MYEMAIL_PASSWORD')

#To send to multiple contacts
contacts = ["mazqoty.01@gmail.com", "test@example.com"]

try:
    msg = EmailMessage()
    msg['From'] = EMAILADDRESS
    msg['To'] = 'mazqoty.01@gmail.com'
    #To send to multiple contacts
    #msg['To'] = ", ".join(contacts)
    msg['Subject'] = "Test"
    msg.set_content("Hello There")
    
    files = ['./image1.jpg', './image2.jpg']
    
    for file in files:
        with open(file, "rb") as f:
            fileData = f.read()
            fileType = imghdr.what(f.name)
            fileName = f.name
        #for image file types
        msg.add_attachment(fileData, maintype = 'image', subtype = fileType, filename = fileName)
        #for other file types
        #msg.add_attachment(fileData, maintype = 'application', subtype = 'octet-stream', filename = fileName)
        #also remove line "fileType = imghdr.what(f.name)" in above code
except Exception as e:
    print(f"Error: {str(e)}")


try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAILADDRESS, EMAILPASSWORD)
        smtp.send_message(msg)
except Exception as e:
    print(f"Error: {str(e)}")
    