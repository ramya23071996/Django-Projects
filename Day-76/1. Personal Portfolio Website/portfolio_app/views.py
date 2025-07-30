from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    skills = ['Flask', 'Django', 'JavaScript']
    return render(request, 'about.html', {'skills': skills})

def projects(request):
    project_list = [
        {'name': 'Bug Tracker', 'desc': 'Issue reporting and management'},
        {'name': 'Stock Visualizer', 'desc': 'Real-time market insights'},
        {'name': 'Password Manager', 'desc': 'Encrypted password storage'}
    ]
    return render(request, 'projects.html', {'projects': project_list})

def contact(request):
    return render(request, 'contact.html')
