from twilio.rest import Client

account_sid = 'ACcde19b90629037ec61101f50ab16ed75'
auth_token = '5b48f2e770e217517669a8f4ddce1a38'
client = Client(account_sid, auth_token)

message = client.messages.create(body="test",
  from_='+17209031383',
  to='+16473337612'
)

print(message.sid)