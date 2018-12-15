from django.shortcuts import render, redirect
from .models import Message
# Create your views here.


def index(request):
    context = {}
    messages = Message.objects.all()
    context['messages'] = messages
    return render(request, 'index.html', context)


# def form_commit(request):
#     if request.method == "POST":
#         name = request.POST.get('name')
#         message = request.POST.get('message')
#         mess = Message(name=name,message=message)
#         mess.save()
#     return redirect()
