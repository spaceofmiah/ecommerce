from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from clothing.forms import ClothForm
from clothing.models import Cloth




def index_page(request):
    """
    handles all request for index page 

    : request -> HttpRequest object
    """
    cloth_list = Cloth.objects.all().order_by('name')[:3]
    return render(request, 'clothing/index_page.html', 
                                    {'cloth_list': cloth_list})

def cloth_list(request):
    """
    handles all request to view all available cloth
    and returns a list of all clothes as a response passed
    to the cloth_list HTML file

    : request -> HttpRequest object
    """
    cloth_list = Cloth.objects.all()
    context = {'cloth_list': cloth_list}
    return render(request, 'clothing/cloth_list.html', context)

def handle_cloth_search(request):
    """
    handles all request to search for cloth products

    : request -> HttpRequest object
    """
    searched_name = request.POST['cloth_name']
    search_result = Cloth.objects.filter(name__icontains=searched_name)
    return render(request, 'clothing/search_result_list.html', 
                                        {'search_result': search_result})

def handle_cloth_creation(request):
    """
    handles all request for creating a cloth, for a GET
    request, the cloth creation form is rendered, for a POST
    request, the submitted data are used to create a cloth object

    : request -> HttpRequest object
    """
    if request.user.is_authenticated == False:
        # if the user is not authenticated at all (meaning the user is not logged in)
        # take the user back to the index page
        return HttpResponseRedirect(reverse("clothing:index"))
    else:
        # but if the user is logged in
        if request.user.is_staff == False:
            # but the user is not an admin
            # also take the user to the index page
            return HttpResponseRedirect(reverse('clothin:index'))
    if request.method == "POST":
        # for POST request only
        form = ClothForm(request.POST, request.FILES)
        
        if form.is_valid():
            cloth = form.save()
            return HttpResponseRedirect(cloth.get_absolute_url())

    # for GET request only
    form = ClothForm()
    context = {'cloth_form': form}
    return render(request, 'clothing/create_cloth.html', context)


def cloth_detail(request, cloth_id):
    """
    handles all request to view cloth detail
    and returns detail of clothes as a response passed
    to the cloth_detail HTML file

    : request -> HttpRequest object
    : cloth_id -> Primary key or Identity of the cloth to be updated
    """
    cloth = Cloth.objects.get(pk=cloth_id)
    context = {'cloth': cloth}
    return render(request, 'clothing/cloth_detail.html', context)

def update_cloth(request, id): 
    """
    handles all request to update cloth instance

    : request -> HttpRequest object
    : cloth_id -> Primary key or Identity of the cloth to be updated
    """
    instance = get_object_or_404(Cloth, id=id)
    form = ClothForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request, 'clothing/cloth_update.html', {'form': form})


def delete_handler(request, cloth_id):
    """
    handles all request to delete cloth instance

    : request -> HttpRequest object
    : cloth_id -> Primary key or Identity of the cloth to be updated
    """
    if request.user.is_staff == False:
        return HttpResponseRedirect(reverse('clothing:cloth_list'))
    Cloth.objects.get(pk=cloth_id).delete()
    return HttpResponseRedirect(reverse('clothing:cloth_list'))