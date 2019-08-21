"""blog_star URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from post.views import (
    IndexView,
    ArticleCreateView,
    ArticleDetailView,

)
from account.views import ProfileDetailView, SignUp
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    # Post
    path('post/create', ArticleCreateView.as_view(), name='create'),
    path('post/<int:article_id>', ArticleDetailView.as_view(), name='detail'),
    path('post/add_like/<int:article_id>', ArticleDetailView.as_view()),
    path('post/add_unlike/<int:article_id>', ArticleDetailView.as_view()),
    # Account/Profile
    path('account/profile/<int:profile_id>', ProfileDetailView.as_view(), name='profile'),
    path('account/', include('django.contrib.auth.urls')),
    path('signup/', SignUp.as_view(), name='signup'),

    # i18n
    path('i18n/', include('django.conf.urls.i18n')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

