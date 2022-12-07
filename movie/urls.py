from django.urls import path
from .views import moveListView,moveDetailView,MoveCreateView,MovieUpdateView,MoveDeleteView

urlpatterns=[
    path('movie_list/',moveListView.as_view(), name='movie_list'),
    path('movie_list/<int:pk>/',moveDetailView.as_view(),name='movie_detail'),
    path('create/', MoveCreateView.as_view(), name='create_movie'),
    path('<int:pk>/update_movie',MovieUpdateView.as_view(),name='update_movie'),
    path('<int:pk>/delete_movie',MoveDeleteView.as_view(), name='delete_movie')
    
]