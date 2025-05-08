from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.conf import settings

def shortEnquiryDisplay(request):
    access_token = request.COOKIES.get('access_token')
    refresh_token = request.COOKIES.get('refresh_token')

    if not access_token:
        return HttpResponse("Access token not found", status=401)

    url = settings.API_BASE_URL + 'api/enquiry/'
    headers = {
        'Authorization': f'Bearer {access_token}',
    }

    refresh_url = settings.API_BASE_URL + 'api/token/refresh/'

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 401:
            # Refresh the token
            refresh_response = requests.post(refresh_url, json={'refresh': refresh_token})

            if refresh_response.status_code == 200:
                access_token = refresh_response.json().get('access')
                headers['Authorization'] = f'Bearer {access_token}'
                response = requests.get(url, headers=headers)
            else:
                return HttpResponse("Unauthorized - Failed to refresh token", status=401)

        response.raise_for_status()
        enquiries = response.json()

    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)

    # Set new token in the response cookies (if refreshed)
    resp = render(request, 'dashboard/pages/enquiry/shortEnquiryDisplay.html', {'enquiries': enquiries})
    resp.set_cookie('access_token', access_token, httponly=True)
    return resp
