def send_email(user, pwd, recipient, subject, body):
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

# send_email("gauravtalele@gmail.com","talele1234","kajal17talele@gmail.com","Shree Swami Samartha","This is a text body")

def send_sms():
    import way2sms
    q=way2sms.sms('9969351313','gauravtalele123')
    q.send( '9082463267', 'hello Mam, Good Morning' )
    print(q.msgSentToday())
    q.logout()

send_sms()



