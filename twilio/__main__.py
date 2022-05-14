from os import environ
from twilio.rest import Client

client = Client(environ.get("TWILIO_ACCOUNT_SID"),
                environ.get("TWILIO_AUTH_TOKEN"))

wa = "whatsapp:+14155238886"
to = "whatsapp:+2348067397793"

# message = client.messages.create(
#     from_=wa,
#     to=to,
#     body='Hello From meji'
# )


message = client.messages.create(
    to="+2348067397793",
    from_="+19793105860",
    body="Hello there!"
)

print(message)
