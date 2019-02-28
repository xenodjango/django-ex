from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from welcome.views import index, health

from rest_framework.routers import DefaultRouter

from todo_app.todo.views import TaskViewSet

router = DefaultRouter()
router.register(r"todo", TaskViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^api/", include((router.urls, "todo"))),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
