from django.shortcuts import render

# Create your views here.


def get_homepage(request):
    """ renders the homepage """
    return render(request, 'homepage.html')


def get_404(request, exception):
    """ renders the custom 404 page """
    return render(request, '404.html', status=404)
