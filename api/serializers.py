from rest_framework import serializers
from api.models import ToDo, Signup

class apiSerializer(serializers.ModelSerializer):
	class Meta:
		model = ToDo
		fields = ('id', 'todo', 'comment', 'reply', 'status', 'end')
        
class signupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ('id', 'username', 'email', 'password', 'phone')