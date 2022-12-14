from django.urls import path
from . import views

urlpatterns = [
    # for the class based API Views
    path('', views.ProductListCreateAPIView.as_view()),
    path('create/', views.ProductCreateAPIView.as_view()),
    path('list/', views.ProductListAPIView.as_view(), name=
    'product-list'),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product-edit'),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
    path('search/', views.SearchListAPIView.as_view(), name='search'),
    
    # for the func-based API View product_alt_view
    path('2/create/', views.product_alt_view),
    path('2/list/', views.product_alt_view),
    path('2/<int:pk>/', views.product_alt_view),

    # for mixins
    path('mixins/list/', views.ProductMixinView.as_view()),
    path('mixins/<int:pk>/detail/', views.ProductMixinView.as_view()),
    path('mixins/create/', views.ProductMixinView.as_view()),
    path('mixins/<int:pk>/update/', views.ProductMixinView.as_view()),
    path('mixins/<int:pk>/delete/', views.ProductMixinView.as_view()),
]