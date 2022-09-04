"""Math URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from Matematika.views import prva
from Matematika.views import registracija
from Matematika.views import logiranje
from Matematika.views import prva_register
from Matematika.views import prva_logiranje
from Matematika.views import logiranje_prva
from Matematika.views import registracija_prva, test,pocetna,testiranje, test_testiranje, test_pocetna, logiranje_pocetna,registracija_pocetna,rez_testiranje,rez_kviz,sodrzina,kviz,testiranje_pocetna
from django.conf import settings
from django.conf.urls.static import static
from Matematika.views import testiranje_rezultati,kviz_rezultati,sodrzina_pocetna,rezultatik_pocetna,rezultatit_pocetna
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', prva ,name="home"),
    path('registration/', registracija ,name="registration"),
    path('home/registration/', prva_register ,name="home/registration"),
    path('login/', logiranje ,name="login"),
    path('home/login/', prva_logiranje ,name="home/login"),
    path('login/home/', logiranje_prva, name="login/home"),
    path('login/pocetna/', logiranje_pocetna, name="login/pocetna"),
    path('registration/home/', registracija_prva, name="registration/home"),
    path('registration/pocetna/', registracija_pocetna, name="registration/pocetna"),
    path('pocetna', pocetna, name="pocetna"),
    path('test/', test, name="test"),
    path('testiranje/', testiranje, name="testiranje"),
    path('test/testiranje/', test_testiranje, name="test/testiranje"),
    path('test/pocetna/', test_pocetna,  name="test/pocetna"),
    path('rezt',rez_testiranje,name="rezt"),
    path('rezk',rez_kviz,name="rezk"),
    path('sodrzina',sodrzina,name="sodrzina"),
    path('kviz',kviz,name="kviz"),
    path('testiranje/pocetna/', testiranje_pocetna,  name="testiranje/pocetna"),
path('testiranje/rezultati/', testiranje_rezultati,  name="testiranje/rezultati"),
path('kviz/rezultati/', kviz_rezultati,  name="kviz/rezultati"),
path('sodrzina/pocetna/', sodrzina_pocetna,  name="sodrzina/pocetna"),
path('rezultatik/pocetna/', rezultatik_pocetna,  name="rezultatik/pocetna"),
path('rezultatit/pocetna/', rezultatit_pocetna,  name="rezultatit/pocetna")

url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),




              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
