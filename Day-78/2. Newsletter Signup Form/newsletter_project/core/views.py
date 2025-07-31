from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SubscriberForm, SubscriberModelForm
from .models import Subscriber

def newsletter_manual(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            Subscriber.objects.create(**form.cleaned_data)
            messages.success(request, "Thank you for subscribing!")
            return redirect('newsletter_manual')
        else:
            messages.error(request, "Check the form for errors.")
    else:
        form = SubscriberForm()
    return render(request, 'core/newsletter_manual.html', {'form': form})

def newsletter_modelform(request):
    if request.method == 'POST':
        form = SubscriberModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You're now subscribed!")
            return redirect('newsletter_modelform')
        else:
            messages.error(request, "Oops! There was a problem.")
    else:
        form = SubscriberModelForm()
    return render(request, 'core/newsletter_modelform.html', {'form': form})