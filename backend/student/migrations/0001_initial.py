# Generated by Django 4.2.7 on 2023-12-03 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('semesters', models.IntegerField(choices=[{1, ' 2 semesters'}, {2, ' 4 semesters'}, {' 6 semesters', 3}])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('semester', models.IntegerField(choices=[{' semester 1', 1}, {2, ' semester 2'}, {3, ' semester 3'}, {' semester 4', 4}, {5, ' semester 5'}, {' semester 6', 6}])),
                ('grade', models.FloatField(default=0, null=True)),
                ('result', models.TextField(default='fail')),
                ('speciality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.speciality')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
