# Mailing list manager. 
The manager will keep track of e-mail addresses categorized into named groups. 
When it's time to send a message, we can pick a group and send the message to 
all e-mail addresses assigned to that group.

We ought to have a safe way to test it, without sending e-mails to a bunch of real people. 

## Start an SMTP server running on port 1025 on the local machine:

$ python -m smtpd -n -c DebuggingServer localhost:1025

We've instructed it to use the DebuggingServer
class (it comes with the built-in SMTP module), which, instead of sending mails
to the intended recipients, simply prints them on the terminal screen as it receives them

## Run example code from Python console
from mailing_list import sendmail
sendmail.send_email("A model subject", "The message contents",
    "from@example.com", "to1@example.com", "to2@example.com")
    
## Let's work on the e-mail group management system
We'll need an object that somehow matches e-mail
addresses with the groups they are in. Since this is a many-to-many relationship
(any one e-mail address can be in multiple groups; any one group can be associated
with multiple e-mail addresses)   

from mailing_list.sendmail import MailingList
m = MailingList()
m.add_to_group("friend1@example.com", "friends")
m.add_to_group("friend2@example.com", "friends")
m.add_to_group("friend3@example.com", "friends")
m.add_to_group("family1@example.com", "family")
m.add_to_group("family2@example.com", "family")
m.add_to_group("chinv@nal.com.vn", "business")

m.send_mailing("A Party",
"Friends and family only: a party", "me@example.com", "friends",
"family", headers={"Reply-To": "me2@example.com"})