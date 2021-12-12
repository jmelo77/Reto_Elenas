from rest_framework import routers

from elenas_apps.base.views import UserViewSet
from elenas_apps.tasks.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'users')
router.register(r'tasks', TaskViewSet, 'tasks')
