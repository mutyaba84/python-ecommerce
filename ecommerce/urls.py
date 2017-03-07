from django.conf.urls import include, url

from . import views

app_name = 'ecommerce' # This will be like this: {% url 'ecommerce:detail' item.id %} on our templates. 
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^products/$', views.products, name='products'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contact/$', views.contact, name='contact'),
	
	url(r'^user/', include([
        url(r'^login/$', views.user_login, name='user_login'),
		url(r'^register/$', views.user_register, name='user_register'),
		url(r'^account/$', views.user_account, name='user_account'),
		url(r'^products/$', views.user_products, name='user_products'),
		url(r'^logout/$', views.logout),
    ])),
]