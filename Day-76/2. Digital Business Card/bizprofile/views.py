from django.shortcuts import render

def index(request):
    context = {
        'name': 'Ramya',
        'title': 'Web Developer',
        'email': 'ramya@example.com',
        'linkedin': 'https://linkedin.com/in/ramya',
        'github': 'https://github.com/ramya',
        'image': 'images/profile.jpg'
    }
    return render(request, 'bizprofile/index.html', context)