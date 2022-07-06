from django.shortcuts import render

# Create your views here.


def main_page(request):
    properties = {
        'title': 'Main Page',
    }
    return render(request, 'Pages/main_page.html', properties)
