from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'ecommerce' # This will be like this: {% url 'ecommerce:detail' item.id %} on our templates. 
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^products/$', views.products, name='products'),
	url(r'^product/(?P<product_id>[0-9]+)/$', views.single_product, name='single_product'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contact/$', views.contact, name='contact'),
	
	url(r'^user/', include([
        url(r'^login/$', views.user_login, name='user_login'),
		url(r'^register/$', views.user_register, name='user_register'),
		url(r'^account/$', views.user_account, name='user_account'),
		url(r'^products/$', views.user_products, name='user_products'),
		url(r'^product/create/$', views.user_product_create, name='user_product_create'),
		url(r'^product/update/(?P<product_id>[0-9]+)/$', views.user_product_update, name='user_product_update'),
		url(r'^product/update/set-featured-image/$', views.set_featured_image),
		url(r'^product/update/unset-image/$', views.unset_image),
		url(r'^product/unset-product/$', views.unset_product),
		url(r'^logout/$', views.logout),
    ])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)