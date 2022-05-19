from rest_framework.authtoken import views
from django.urls import include, path
from rest_framework import routers
from .views import PostViewSet, GroupViewSet, CommentViewSet


router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'groups', GroupViewSet, basename='groups')
router_v1.register(r'^posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename=r'^comments')


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router_v1.urls)),
]
