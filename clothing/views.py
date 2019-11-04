from django.shortcuts import render
from clothing.models import Cloth

def index_page(request):
    """
    handles all request for index page 
    """
    cloth_list = Cloth.objects.all().order_by('name')[:3]
    return render(request, 'clothing/index_page.html', 
                                    {'cloth_list': cloth_list})


def cloth_list(request):
    """
    handles all request to view all available cloth
    and returns a list of all clothes as a response passed
    to the cloth_list HTML file
    """
    cloth_list = Cloth.objects.all()
    context = {'cloth_list': cloth_list}
    return render(request, 'clothing/cloth_list.html', context)

def handle_cloth_search(request):
    """
    handles all request to search for products
    """
    searched_name = request.POST['cloth_name']
    search_result = Cloth.objects.filter(name__icontains=searched_name)
    return render(request, 'clothing/search_result_list.html', {'search_result': search_result})