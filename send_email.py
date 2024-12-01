import smtplib as s

ob = s.SMTP("smtp.gmail.com", 587)
ob.ehlo()
ob.starttls()
ob.login("r38401713@gmail.com", "wnir aypc lzwb czmb")
subject = "test python"
body = "I Love Python"
listadd = ["coolguy.eddy14@gmail.com", "ramswaroopnath71@gmail.com"]
message = f"Subject: {subject}\n\n{body}"
ob.sendmail("ramswaroopnath71@gmail.com", listadd, message)
print("Send Email")
ob.quit()
