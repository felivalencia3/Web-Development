from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', include("ImageUploader.urls")),
    path('analyze/', include("Analysis.urls"))
]
