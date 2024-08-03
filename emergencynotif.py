from twilio.rest import Client

account_sid = 'ACcde19b90629037ec61101f50ab16ed75'
auth_token = '9cc7d1e378b6bc39bd1d64c7e3ad4a5f'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+17209031383', body='test',
  to='+16473337612'
)

print(message.sid)