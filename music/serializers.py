from rest_framework import serializers
from .models import Tasks


class SongsSerializer(serializers.ModelSerializer):
	# is_devoteful	=	serializers.BooleanField(read_only=True)
	# description		=	serializers.CharField(min_length=2,max_length=200)
	class Meta:
		model = Tasks
		fields = ('task_id','robot_id','task_name','issued_time','scheduled_time','status')

