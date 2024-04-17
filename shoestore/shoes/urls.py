from django.urls import path

from . import views

app_name = "shoes"

urlpatterns = [
    path("actors/", views.ActorListView.as_view(), name="actor_list"),
    path("actors/<int:pk>", views.ActorDetailView.as_view(), name="actor_detail"),
    path("actors/new", views.ActorCreateView.as_view(), name="actor_create"),
    path("actors/update/<int:pk>", views.ActorUpdateView.as_view(),
         name="actor_update"),
    path("actors/delete/<int:pk>", views.ActorDeleteView.as_view(),
         name="actor_delete"),
    path("shoes/", views.MovieListView.as_view(), name="movie_list"),
    path("shoes/new", views.MovieCreateView.as_view(), name="movie_create"),
    path("shoes/<int:pk>", views.MovieDetailView.as_view(),
         name="movie_detail"),
    path("shoes/update/<int:pk>", views.MovieUpdateView.as_view(),
         name="movie_update"),
    path("shoes/delete/<int:pk>", views.MovieDeleteView.as_view(),
         name="movie_delete"),
     path("shoes/update_bis/<int:pk>",views.MovieUpdatebisView.as_view(),name="movie_update_bis"),
     path("shoes/bis/<int:pk>",views.MovieDetailbisView.as_view(),name="movie_detail_bis",),
     path("shoes/js/<int:pk>",views.MovieDetailJsView.as_view(),name="movie_detail_js",),
]