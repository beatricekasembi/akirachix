# Generated by Django 2.2.1 on 2019-10-15 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_auto_20191015_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Courses',
            field=models.ManyToManyField(blank=True, related_name='students', to='course.Course'),
        ),
    ]
