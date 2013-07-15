from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qrproject.views.home', name='home'),
    # url(r'^qrproject/', include('qrproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register_company/$','register.views.insert_data_company'),
    url(r'^register_product/$','register.views.insert_data_product'),
    url(r'^register_compaign/$','register.views.insert_data_compaign'),
    url(r'^login/$', 'register.views.companyLogIn'),
    ##################### Retrieve Data #######################
    url(r'^companyProfile/$', 'register.views.companyProfile'),  
    url(r'^listallcompanies/$', 'register.views.listAllCompanies'),
    url(r'^productprofile/$', 'register.views.productProfile'),
    url(r'^listallproducts/$', 'register.views.listAllProducts'),
    url(r'^compaignprofile/$', 'register.views.compaignProfile'),
    url(r'^listallcompaignes/$', 'register.views.listallCompaignes'),
)
