import uuid
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    deviceId=models.TextField(max_length=255,blank=False)
    fullname=models.TextField(max_length=150,blank=False)
    zone=models.TextField(max_length=150,blank=False)
    class Meta:
        db_table='Users'

class Recital(models.Model):
    STATUSOFRECITAL=[('ENCOURS','ENCOURS'),('SUSPENDU','SUSPENDU'),('TERMINER','TERMINER'),]
    TYPEOFRECITAL=[('PUBLIC','PUBLIC'),('PRIVATE','PRIVATE'),]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator=models.ForeignKey(User,on_delete=models.CASCADE)
    legend=models.TextField(max_length=255,blank=False)
    NumberOfKamil=models.PositiveIntegerField(blank=False)
    NumberOfKamilEnd=models.PositiveIntegerField(blank=False,default=0)
    recitalStatus=models.TextField(max_length=90,blank=False,choices=STATUSOFRECITAL,default='ENCOURS')
    recitalType=models.TextField(max_length=90,blank=False,choices=TYPEOFRECITAL,default='PUBLIC')
    createdAt=models.DateTimeField(auto_now_add=True,blank=False,null=False)
    dateOfEnd=models.DateTimeField(blank=False,null=False)
    updateddAt=models.DateTimeField(auto_now=True,blank=False,null=False)
    class Meta:
        db_table='Recitals'
        ordering = ['createdAt']

class Juki(models.Model):
    STATUSOFREADING=[('ENCOURS','ENCOURS'),('TERMINER','TERMINER'),]
    id = models.AutoField(primary_key=True,editable=False)
    jukiNumber=models.PositiveIntegerField(blank=False,default=0)
    objectifLecture=models.PositiveIntegerField(blank=False,default=1)
    atteint=models.PositiveIntegerField(blank=False,default=0)
    fromRecital=models.ForeignKey(Recital,on_delete=models.CASCADE)
    chosedBy=models.ForeignKey(User,on_delete=models.CASCADE)
    ReadingState=models.TextField(max_length=50,blank=False,choices=STATUSOFREADING,default='ENCOURS')
    chosedAT=models.DateTimeField(auto_now=True,blank=False,null=False)
    updateddAt=models.DateTimeField(auto_now=True,blank=False,null=False)
    class Meta:
        db_table='JukiTaked'
        ordering = ['fromRecital','chosedBy']



class Comment(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    messages=models.TextField(max_length=255,blank=False,)
    commentedBy=models.ForeignKey(User,on_delete=models.CASCADE)
    commentedAt=models.DateTimeField(auto_now_add=True,blank=False,null=False)
    class Meta:
        db_table='Comments'
        ordering = ['commentedBy']

class Like(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    theComment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    likedBy=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        db_table='Likes'
        ordering = ['theComment','likedBy']
    

class kamil(models.Model):
    id = models.AutoField(primary_key=True,editable=False)
    jukiNumber=models.IntegerField(blank=False)
    jukiType=models.TextField(max_length=50,blank=False,default='TEXT CORANIQUE')
    class Meta:
        db_table='juz'
        ordering = ['jukiNumber']
    