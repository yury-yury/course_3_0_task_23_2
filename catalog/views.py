from django.shortcuts import render

# Create your views here.

def main(request):
    if request.method == 'GET':
        return render(request, 'catalog/home.html')


def contact(request):
    if request.method == 'POST':
        visiter = dict()
        visiter['name'] = request.POST.get('name', None)
        visiter['phone'] = request.POST.get('phone', None)
        visiter['message'] = request.POST.get('message', None)
        print(visiter)
    return render(request, 'catalog/contact.html', )
