##################### Hard Starting
import pandas
import datetime as dt
today=dt.datetime.now()
today_tupple= (today.month,today.day)
data = pandas.read_csv("birthdays.csv")


 birthdays_dict = {
    (month, day): data_row
 }


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



