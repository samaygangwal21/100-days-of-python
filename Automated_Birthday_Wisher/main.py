# import smtplib
#
# my_email = "samaygangwal07@gmail.com"
# password = "ejmcksxmyxqljunz"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="samaygangwal21@gmail.com",
#         msg="Subject:HELLO!!\n\nThis is the body of email"
#     )

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
date_of_birth = dt.datetime(year= 2004, month= 7, day=21)
print(now)
print(date_of_birth)
print(year, month, day_of_week)
print(now - date_of_birth)