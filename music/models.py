from django.db import models
STATUS_CHOICES = (
    ('Scheduled','SCHEDULED'),
    ('Active','ACTIVE' ),
    ('Completed','COMPLETED' ),
    ('Preempted','PREEMPTED' ),
    ('Rejected','REJECTED' )
)

class Tasks(models.Model):
    # song title
    task_id 		= models.AutoField(primary_key=True)
    robot_id 		= models.IntegerField(null=False,unique=True)
    # name of artist or group/band
    task_name 		= models.CharField(max_length=255, null=False)
    issued_time 	= models.DateTimeField(auto_now_add=True)
    scheduled_time 	= models.DateTimeField(auto_now_add=False)
    status         	= models.CharField(max_length=15, choices=STATUS_CHOICES, default='Scheduled')
    def __str__(self):
        return "{} - {}".format(self.task_id,self.robot_id,self.task_name, self.issued_time,self.scheduled_time,self.status)
