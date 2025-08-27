import smtplib

my_email = "samaygangwal07@gmail.com"
password = "ejmcksxmyxqljunz"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="samaygangwal21@gmail.com",
        msg="Subject:HELLO!!\n\nThis is the body of email"
    )
