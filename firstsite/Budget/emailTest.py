import smtplib 
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('','')
problems = server.sendmail('@gmail.com', '@.com', 'it worked')
server.quit()


