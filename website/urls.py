"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from views.home import mainPageViews
from views.dashboard import pageViews,enquiryViews,usersViews,otpViews



urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    # Home Page Routes
    path('', mainPageViews.franchiseLanding, name = 'franchiseLanding'),
    path('index/', mainPageViews.index, name = 'index'),
    path('contact/', mainPageViews.contact, name="contact"),
    path('franchise/', mainPageViews.franchise, name="franchise"),
    path('about-us/', mainPageViews.about, name='about-us'),
    path('counsellor/',mainPageViews.counsellor, name='counsellor'),
    # path('franchise-landing/',mainPageViews.franchiseLanding, name = "franchiseLanding"),
    path('faq-franchise/',mainPageViews.faqFranchise, name = "faqFranchise"),
    
    # path('test/', mainPageViews.test),
    
    # Login Register Route
    path('login/', pageViews.loginPageDisplay, name = 'login'),
    path('register/<str:role>/',pageViews.registerDisplay, name = 'register'),
    path('verify-otp/',pageViews.verifyOtp, name = 'verifyOtp'),
    
    #OTP Views
    path('submit-otp/',otpViews.submitOtp, name="submitOtp"),
    path('resend-otp/',otpViews.resendOtp, name="resendOtp"),
        
    # Admin Page Routes
    path('dashboard/', pageViews.dashboard, name='dashboard'),
    
    
    
    # Admin Form Display Routes
    path('short-enquiry-display/',enquiryViews.shortEnquiryDisplay, name = 'shortEnquiryDisplay'),
    path('student-display/',usersViews.studentDisplay, name = 'studentDisplay'),
    path('franchise-display/',usersViews.franchiseDisplay, name = 'franchiseDisplay'),
]
