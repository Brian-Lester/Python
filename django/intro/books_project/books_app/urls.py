from django.urls import path     
from . import views

urlpatterns =[
    path('',views.index),
    path('create/book',views.create_book),
    path('view/book/<int:id>',views.view_book),
    path('create/relationship/<int:id>',views.create_realationship),
    path('authors',views.authors),
    path('create/author',views.create_author),
    path('view/author/<int:id>',views.view_author),
    path('create/relationship1/<int:id>',views.create_realationship1)
]