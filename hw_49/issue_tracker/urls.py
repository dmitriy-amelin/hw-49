from django.urls import path

from issue_tracker.views import (
    IndexView,
    TaskView,
    TaskUpdate,
#     task_update,
#     task_delete,
)

urlpatterns = [
    path('', IndexView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskView.as_view() , name='task-view'),
    # path('task/add/', task_add, name='task-add'),
    path('<int:pk>/update/', TaskUpdate.as_view(), name='task-update'),
    # path('<int:pk>/delete/', task_delete, name='task-delete'),
]