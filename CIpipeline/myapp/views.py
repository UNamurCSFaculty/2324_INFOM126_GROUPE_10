from django.shortcuts import render,redirect

from .models import Message
from .forms import MessageForm

def index(request):
    messages = Message.objects.all()
    return render(request, 'index.html', {'messages': messages})
def add_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MessageForm()
    return render(request, 'add_message.html', {'form': form})