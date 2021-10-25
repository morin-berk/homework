# Generated by Django 3.2.8 on 2021-10-24 18:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('created',
                 models.DateTimeField(default=django.utils.timezone.now)),
                ('deadline', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('task', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('solution', models.TextField()),
                ('homework', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='polls.homework')),
            ],
        ),
        migrations.CreateModel(
            name='HomeworkResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('created', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('author', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='student_author', to='polls.student')),
                ('homework', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='student_homework',
                    to='polls.homework')),
                ('solution', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='student_solution',
                    to='polls.student')),
            ],
        ),
        migrations.AddField(
            model_name='homework',
            name='task',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='polls.teacher'),
        ),
    ]
