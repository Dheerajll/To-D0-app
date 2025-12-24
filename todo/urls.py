from django.urls import path
from . import views

urlpatterns = [
    path('addtask/',views.addTask,name="addtask"),
    path('task_completed/<int:id>',views.taskCompleted,name="task-completed"),
    path('delete_task/<int:id>',views.delete_task,name="delete-task"),
    path('unmark_task/<int:id>',views.unmark,name="unmark"),
    path('edit_page/<int:id>',views.editpage,name="edit-page")
]
