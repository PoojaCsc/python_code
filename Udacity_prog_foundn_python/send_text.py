# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACfce64db77a642cf221e3273745a51635'
auth_token = '58cf1f333ce61f9bd67c393ce67bf12d'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there! SMS sending through Twilio API',
                              from_='+15183339448',
                              to='+919425247321'
                          )

print(message.sid)