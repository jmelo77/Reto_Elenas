# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsAdminOrOwner


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows task to be viewed,edited or deleted.
    """

    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsAdminOrOwner,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(user=self.request.user, active=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_destroy(self, instance):
        instance.delete()  
