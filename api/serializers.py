from rest_framework import serializers

from orderbox.models import Order


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('author', 'textDep', 'textDest','created_date')

    # author = models.ForeignKey('auth.User')
    # textDep = models.TextField()
    # textDest = models.TextField()
    # created_date = models.DateTimeField(