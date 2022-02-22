"""
dashboardcrypto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from crypto.urls import cryptos_urls
from exchange.urls import exchange_urls
from wallet.urls import wallet_urls
from finance.urls import negotiation_urls
from coinmarketcap.urls import cmc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/crypto/', include(cryptos_urls)),
    path('api/exchange/', include(exchange_urls)),
    path('api/wallet/', include(wallet_urls)),
    path('api/finance/', include(negotiation_urls)),
    path('api/coinmarketcap/', include(cmc_urls)),
    re_path('index/', TemplateView.as_view(template_name='index.html'))
]

#urlpatterns +=[re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]