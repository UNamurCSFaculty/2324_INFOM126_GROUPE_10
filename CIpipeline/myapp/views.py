from django.shortcuts import render,redirect,get_object_or_404

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
def update_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MessageForm(instance=message)
    return render(request, 'update.html', {'form': form, 'message': message})
def delete_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    message.delete()
    return redirect('index')
