from django.shortcuts import redirect, render
# from requests.api import request
from django.http import request
from django.contrib import messages
from mutualFund.models import Service, CustomerQuery
import requests
from datetime import datetime

# Create your views here.

def sendEmail(emailData):
    url = "https://email-sender1.p.rapidapi.com/"

    fromEmail = emailData['email']
    phone = emailData['phone']
    name = emailData['name']
    query_type = emailData['query_type']
    message = emailData['message']
    toEmail= 'wealthbazzar2021@gmail.com'
    ccEmail= 'ashi.patel546@gmail.com'

    email_send_data = f'''
    Sender Name: {name}
    Sender email id: {fromEmail}
    Sender Phone: {phone}
    Query for Product(s): {query_type}
    Sender Message: {message}
    '''
        

    querystring = {"txt_msg":email_send_data,"to":toEmail,"from":"noReply_iStock","subject":"test message from iStock","reply_to":"ashi.patel546@gmail.com","cc":ccEmail}
    # querystring = {"txt_msg":"test of the body","to":"ashi.patel546@gmail.com","from":"iStock","subject":"test of the subject","bcc":"sandhyagond88@gmail.com","reply_to":"ashi.patel546@gmail.com","html_msg":"<html><body><b>test of the body</b></body></html>","cc":"cc-mail@gmail.com"}

    payload = "{\r\n    \"key1\": \"value\",\r\n    \"key2\": \"value\"\r\n}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-host': "email-sender1.p.rapidapi.com",
        'x-rapidapi-key': "bbdc55e275mshd5fbb490f999f4cp1300fbjsn631c6dc46a59"
        }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    return response

services = Service.objects.all()
    
data = {
        'services': services,
        }

def home(request):
    
    return render (request, 'index.html', data)
    

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        query_type = request.POST.get('query_type')
        email_data = {'name': name,
                      'email': email,
                      'phone': phone,
                      'query_type': query_type,
                      'message':message
                        }
        query = CustomerQuery (cust_name=name, cust_email= email, cust_phone=phone, query_product=query_type, query_message=message, date = datetime.today())
        query.save()
        emailResponse = sendEmail(email_data)
        messages.success(request, f'Query Id: "{query.query_id}". Your Query has been submitted successfully. Our representative will contact you soon!!!')
        return render(request, 'index.html', data)
        