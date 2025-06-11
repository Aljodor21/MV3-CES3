from django.contrib import admin
from django.urls import path,include
from strawberry.django.views import GraphQLView
from notes.schema import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('notes.urls')),
    path("graphql/", GraphQLView.as_view(schema=schema)),
]
