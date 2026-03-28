from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Kafedra(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT, related_name='kafedras')

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='teachers')
    kafedra = models.ForeignKey(Kafedra, on_delete=models.CASCADE, related_name='teachers')

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='groups')

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name