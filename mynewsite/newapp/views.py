from django.shortcuts import render
from .forms import Order
import requests
import json

url = 'https://order.drcash.sh/v1/order'
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer NWJLZGEWOWETNTGZMS00MZK4LWFIZJUTNJVMOTG0NJQXOTI3',
}

def order(request):
    sent = False
    text = ''
    if request.method == 'POST':
        form = Order(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            body = {
                    'stream_code': 'iu244',
                    'client': {
                        'name': cd['name'],
                        'phone': cd['phone'],
                    },
                    'sub1': cd['hidden_field'],
            }
            form.save()
            response = requests.post(url, headers=headers, data=json.dumps(body))

            if response.status_code == 200:
                text = 'Спасибо за заказ'
                sent = True
            else:
                text = 'Ошибка'
                sent = True
    else:
        form = Order()

    return render(request, 'newapp/order.html', {'form': form, 'text': text, 'sent': sent})