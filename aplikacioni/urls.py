from django.urls import path
from . import views


urlpatterns= [

    path("", views.home, name="HomePage"),   #thonjzat jane boshe sepse home esht faqja e pare qe hapet
    path("about/", views.about, name="aboutPage"),
    # path("product/", views.product, name="productPage"),
    path("login/", views.login, name="loginPage"),  #kte emrin e shkruajme tek navbari file, aty ku kemi futur me href linkun e login page 
]

# pas view.py, vijme ktu dhe shenojme serish url-t

