from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
						#url(r'^', TemplateView.as_view(template_name='under_maintenance.html')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'', include('core.urls')),
                       )