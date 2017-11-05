"""gupunkotha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from allauth.account.views import SignupView
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views

from messaging.views import MessageListView, MessageCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', MessageListView.as_view(), name='message-list'),
    url(r'^u/(?P<username>[a-zA-Z0-9]+)/$', MessageCreateView.as_view(), name='message-create'),

    url(r'^login/$', views.LoginView.as_view(), name='account_login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),

    url(r'^password_change/$', views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^password_change/done/$', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    url(r'^password_reset/$', views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^accounts/signup/$', SignupView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
