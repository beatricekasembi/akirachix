# Generated by Django 2.2.1 on 2019-10-15 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20190924_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Courses',
            field=models.ManyToManyField(blank=True, null=True, related_name='students', to='course.Course'),
        ),
    ]
