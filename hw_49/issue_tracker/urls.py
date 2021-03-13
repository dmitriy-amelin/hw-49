from django.urls import path

from issue_tracker.views import (
    IndexView,
    TaskView,
    TaskUpdate,
    TaskAdd,
    TaskDelete,

)

urlpatterns = [
    path('', IndexView.as_view(), name='task-list'),
    path('task/<int:pk>/', TaskView.as_view(), name='task-view'),
    path('task/add/', TaskAdd.as_view(), name='task-add'),
    path('<int:pk>/update/', TaskUpdate.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDelete.as_view(), name='task-delete'),
]