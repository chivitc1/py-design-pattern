import smtplib
from collections import defaultdict
from email.mime.text import MIMEText


def send_email(subject, message, from_addr, *to_addrs, host='localhost', port=1025, **headers):
    headers = {} if headers is None else headers
    email = MIMEText(message)
    email['Subject'] = subject
    email['From'] = from_addr

    for header, value in headers.items():
        email[header] = value

    sender = smtplib.SMTP(host=host, port=port)

    for addr in to_addrs:
        del email['To']
        email['To'] = addr
        sender.sendmail(from_addr=from_addr, to_addrs=addr, msg=email.as_string())
    sender.quit()


class MailingList:
    '''Manage groups of e-mail addresses for sending e-mails.'''
    def __init__(self):
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def emails_in_group(self, *groups):
        groups = set(groups)
        emails = set()
        for e, g in self.email_map.items():
            '''add the e-mail address to the set of return
            values only if the passed in groups intersect with the e-mail address groups'''
            if g.intersection(groups):
                emails.add(e)
        return emails

    def send_mailing(self, subject, message, from_addr, *groups, headers=None):
        emails = self.emails_in_group(*groups)
        send_email(subject, message, from_addr, *emails, headers=headers)
