from punch import views
from django.urls import path


urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("contactus",views.contactusx,name="contactus"),
    path("services",views.services,name="services"),
    path("datasave",views.savethis),
    path("updatethis/<int:zxc>",views.updatethisdata),
    path("update-this-data/<int:updateid>",views.nowupdatedata),
    path("delete-record/<int:myid>",views.deletethisdata),
    path("search",views.searchdata,name="searchthis"),
    path("signup",views.signup,name="signup"),
    path("login",views.mylogin,name="login"),
    path("logout",views.mylogout,name="logout")
]