import africastalking

# To Initialize Africa's Talking
username = "sandbox"  
api_key = ",mnbvxfyujno9"
africastalking.initialize(username, api_key)
sms = africastalking.SMS


def send_sms(to, message):
    response = sms.send(message, [to])
    print(response)
