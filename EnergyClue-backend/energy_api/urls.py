from django.urls import path
from . import views as energy_api_views

urlpatterns = [
    path('testinomial/', energy_api_views.TestinomialDetail.as_view(), name="testinomial"),
    path('get-quote/', energy_api_views.GetQuoteDetail.as_view(), name="get-quote"),
    path('customer-detail/', energy_api_views.CustomerDetail.as_view(), name="customer-detail"),
    path('contact/', energy_api_views.Contact.as_view(), name="contact"),
    path('service/', energy_api_views.Service.as_view(), name="service"),
    path('site-survey/', energy_api_views.SiteSurvey.as_view(), name="site-survey"),
    path('faq/', energy_api_views.GetFaq.as_view(), name="faq"),
]
