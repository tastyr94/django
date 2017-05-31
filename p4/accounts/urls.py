from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', login, name='login', kwargs={
        'template_name': 'accounts/login_form.html',
    }),
    url(r'^logout/$', logout, name='logout', kwargs={
        'next_page': '/',  # 디폴트 next 인자 지정, 혹은 settings.LOGOUT_REDIRECT_URL을 지정
    }),
]