from django.urls import include, path

urlpatterns = [
    path("", include("hello.urls")),
    path("api/", include("praia.urls")),
]
