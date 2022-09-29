# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class StudentapiStudentinfo(models.Model):
    studentname = models.CharField(db_column='StudentName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    studentrollno = models.IntegerField(db_column='StudentRollNo', primary_key=True)  # Field name made lowercase.
    studentbranch = models.CharField(db_column='StudentBranch', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    studentgpa = models.FloatField(db_column='StudentGPA')  # Field name made lowercase.
    studentsection = models.CharField(db_column='StudentSection', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StudentApi_studentinfo'
    