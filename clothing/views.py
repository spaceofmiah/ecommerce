from django.shortcuts import render

def index_page(request):
    return render(request, 'clothing/index_page.html')
def cloth_list(request):
    return render(request, 'clothing/list_page.html')