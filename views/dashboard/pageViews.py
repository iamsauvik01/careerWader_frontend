from django.shortcuts import render
from django.http import HttpResponse
import requests
import traceback
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.conf import settings



def dashboard(request):
    try:
        # Print all session data for debugging
        # print("Session data:", dict(request.session))  

        role = request.session.get('user_role', 'Guest')

        return render(request, 'dashboard/pages/dashboard.html', {'role': role})
    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)

def loginPageDisplay(request):
    try:
        return render(request, 'dashboard/pages/auth/auth-login.html',{'api_base_url': settings.API_BASE_URL})        
    except Exception as e:
        return HttpResponse(f"An error occured {e}",status = 500)
    
def registerDisplay(request,role):
    try:
        return render(request, 'dashboard/pages/auth/auth-register.html', {'role':role,'api_base_url': settings.API_BASE_URL})
    except Exception as e:
        return HttpResponse(f"An error occured {e}",status = 500)
    
def verifyOtp(request):
    try:
        return render(request, 'dashboard/pages/auth/verification-page.html')
    except Exception as e:
        return HttpResponse(f"An error occured {e}",status = 500)
    
