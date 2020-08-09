from rest_framework import serializers
from api.models import ToDo

class apiSerializer(serializers.ModelSerializer):
	class Meta:
		model = ToDo
		fields = ('id', 'todo', 'comment', 'reply', 'status', 'end')