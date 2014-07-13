from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from lists.models import Item

# Create your views here.

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    
    items = Item.objects.all()
    #sends items to the template home.html using the key 'items'
    #the template uses this as {{% for item in items %}}
    return render(request,'home.html',{'items':items})
