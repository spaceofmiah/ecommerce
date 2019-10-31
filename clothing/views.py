from django.shortcuts import render
from clothing.models import Cloth

def index_page(request):
    """
    handles all request for index page 
    """
    return render(request, 'clothing/index_page.html')


def cloth_list(request):
    """
    handles all request to view all available cloth
    and returns a list of all clothes as a response passed
    to the cloth_list HTML file
    """
    cloth_list = Cloth.objects.all()
    context = {'cloth_list': cloth_list}
    return render(request, 'clothing/cloth_list.html', context)