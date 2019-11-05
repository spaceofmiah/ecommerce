from django.shortcuts import render, reverse
from clothing.models import Cloth
from clothing.forms import ClothCreationForm
from django.http import HttpResponseRedirect

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

def handle_cloth_creation(request):
    """
    handles all request for creating a cloth, for a GET
    request, the cloth creation form is rendered, for a POST
    request, the submitted data are used to create a cloth object
    """
    if request.method == "POST":
        # for POST request only
        form = ClothCreationForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('clothing:index'))

    # for GET request only
    form = ClothCreationForm()
    context = {'cloth_form': form}
    return render(request, 'clothing/create_cloth.html', context) 