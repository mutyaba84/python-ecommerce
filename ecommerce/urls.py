from django.conf.urls import url

from . import views

app_name = 'ecommerce' # This will be like this: {% url 'ecommerce:detail' item.id %} on our templates. 
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^products/$', views.products, name='products'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^logout/$', views.logout),
]