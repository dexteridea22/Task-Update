from rest_framework.generics import  ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from django.views.generic import ListView, DetailView
from django.shortcuts import render,redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import Tasks
from .serializers import SongsSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
# import logging
import json
class SongsPagination(LimitOffsetPagination):
	default_limit   =   10
	max_limit   =   200         


class ListTasksView(ListAPIView):
	 """
	 Provides a get method handler.
	 """
	 queryset = Tasks.objects.all()
	 serializer_class = SongsSerializer
	 filter_backends    =   (DjangoFilterBackend,SearchFilter)
	 # filter_fields    =   ('title',)
	 # search_fields    =   ('title','artist')
	 pagination_class   =   SongsPagination 


	 
class TaskCreate(CreateAPIView):
	
	serializer_class    =   SongsSerializer
	
	def create(self,request,*args,**kwargs):
		try:
			task_name   =   request.data.get('task_name')
			if task_name is not None and task_name=='':
				raise ValidationError({'task name cannot be empty'})

		except ValueError:
			raise ValidationError({'task name will be string'})

		return super().create(request,*args,**kwargs)
class TaskRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
	queryset            =   Tasks.objects.all()
	lookup_field        =   'task_id'
	serializer_class    =   SongsSerializer

	def delete(self,request,*args,**kwargs):
		task_id =   request.data.get('task_id')
		response    =   super().delete(request,*args,**kwargs)
		if response.status_code ==  204:
			from django.core.cache import cache
			cache.delete('task_data{}'.format(task_id))
		return response 
	def update(self,request,*args,**kwargs):
		response    =   super().update(request,*args,**kwargs)
		task_id =   request.data.get('task_id')
		if response.status_code == 200:
			from django.core.cache import cache
			task =  response.data
			cache.set('task_Data{}'.format(task_id),{
			'robot_id':task['robot_id'],    
			'task name':task['task_name'],
			'issued_time':task['issued_time'],
			'scheduled_time':task['scheduled_time'],
			'status':task['status'],
			})
		# logger = logging.getLogger(__name__)	
		# logger.info('Information incoming!')	
		if response.data['status'] =='Completed':
			# print(response.data)
			with open('log_completed_tasks.json', 'a') as outfile:
				json.dump(response.data, outfile,indent=2)	
			outfile.close()
		return response 

def ListTableTasksView(request):
	 """
	 Provides a get method handler.
	 """
	 queryset = Tasks.objects.all()
	 context = {
	 'object_list' : queryset
	 }
	 # template_name = "tasks/index.html"
	 return render(request,'tasks/index.html',context) 


	 


 
