from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
    try:
        return render(request, 'home/pages/index.html')
    except Exception as e:
        return HttpResponse(f"An error occured {e}", status = 500)
    
def about(request):
    try:
        return render(request, 'home/pages/about.html')
    except Exception as e:
        return HttpResponse(f"An error occured {e}", status = 500)
    
def contact(request):
    try:
      return render(request, 'home/pages/contact.html')  
    except Exception as e:
        return HttpResponse(f"An error occured {e}", status = 500)
    
def franchise(request):
    try:
        return render(request, 'home/pages/franchise.html')
    except Exception as e:
        return HttpResponse(f"An error occured {e}", status = 500)
    
def counsellor(request):
    try:
        return render(request, 'home/pages/counsellor.html')
    except Exception as e:
        return HttpResponse(f"An error occured {e}", status = 500)
    
def franchiseLanding(request):
    try:
        print(settings.API_BASE_URL)
        return render(request, 'home/pages/franchiseLanding.html')
    except Exception as e:
        return HttpResponse(f"An error occured {e}", status = 500)
    
def faqFranchise(request):
    try:
        return render(request, 'home/pages/faqFranchise.html')
    except Exception as e:
        return HttpResponse(f"An error occured {e}", status = 500)
    
# def test(request):
#     try:
#         return render(request, 'home/pages/test.html')
#     except Exception as e:
#          return HttpResponse(f"An error occured {e}", status = 500)