import pandas as pd
import smtplib

df = pd.read_csv("F:/PyCharm/SecretSanta/Secret Santa List.csv")
names = []
[names.append(x) for x in df['Name'] if x not in names]
emails = []
[emails.append(x) for x in df['Email'] if x not in emails]
gifts = []
[gifts.append(x) for x in df['Gifts'] if x not in gifts]
sender = "name@example.com"

pairs = []

for name in names:
    # first check if it is an odd/even  entry and then pair
    if len(names) % 2 != 0:
        if len(names) - names.index(name) > 2:

            above_2 = [name, names[names.index(name) + 2]]
            pairs.append(above_2)
        else:

            less_than_2 = [name, names[names.index(name) - 3]]
            pairs.append(less_than_2)

    else:
        if len(names) - names.index(name) > 1:

            above_2 = [name, names[names.index(name) + 1]]
            pairs.append(above_2)
        else:

            less_than_1 = [name, names[names.index(name) - 2]]
            pairs.append(less_than_1)

for i in pairs:
    # this will enable you see how the pairing is
    print(i[0] + " gives gift to " + i[1] + " send this email to " + emails[
        names.index(i[1])] + " List of gifts  includes: " + gifts[names.index(i[0])])

    giver = i[0]
    recipient = i[1]
    email = emails[names.index(giver)]
    gift = gifts[names.index(recipient)]
    text = """Subject: Secret Santa. This is another test

    Hi {giver} , you are to act as secret santa to {recipient}, list of helpful gifts include: {gift}"""

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    s.login(sender, "your_password")
    s.sendmail(sender, email, text.format(sender=sender, giver=giver, recipient=recipient, gift=gift))
    s.quit()
