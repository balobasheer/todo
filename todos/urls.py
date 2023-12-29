from django.urls import path

from .views import TodoList, DetailTodo


urlpatterns = [
    path("<int:pk>/", DetailTodo.as_view(), name="todo_detail"),
    path("", TodoList.as_view(), name="todo_list"),
]
