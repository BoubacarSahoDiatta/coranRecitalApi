from django.urls import path

from . import views

urlpatterns = [
  path('recitals/token=fb9c559be4cd/', views.RecitalView.as_view()),
  path('recitals/invitation=<uuid:id>/', views.RecitalView.as_view()),
  path('users/token=fb9c559be4cd/', views.UserView.as_view()),
  path('compte/<int:id>/', views.UserView.as_view()),
  path('kamil/token=fb9c559be4cd/', views.theHollyCoranView.as_view()),
  path('mesjoukis/user=<int:userid>&recital=<uuid:recitalid>/', views.JukiTakedView.as_view()),
  path('comments/token=fb9c559be4cd/', views.CommentsView.as_view()),
  path('comments/<int:id>/', views.CommentsView.as_view()),
  path('likes/<int:id>/', views.LikesView.as_view()),
]