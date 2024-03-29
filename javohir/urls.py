from django.urls import path

from .views import HomePageView, UserRegisterView, UserLoginView, UserLogoutView, UserHomeView, UserAboutView, \
    UserPostDetailView, UserPostConfirmDeleteView, UserPostsView, UserPostsFormView

app_name = 'javohir'
urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('about/', UserAboutView.as_view(), name='about'),
    path('home/', UserHomeView.as_view(), name='home'),
    path('post_detail/', UserPostDetailView.as_view(), name='post_detail'),
    path('post_confirm_delete/', UserPostConfirmDeleteView.as_view(), name='post_confirm_delete'),
    path('user_posts/', UserPostsView.as_view(), name='user_posts'),
    path('post_form/', UserPostsFormView.as_view(), name='post_form'),
]
