# Generated by Django 5.0.7 on 2024-07-16 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.SmallIntegerField()),
                ('course_name', models.CharField(max_length=20)),
                ('course_description', models.TextField()),
                ('department', models.CharField(max_length=20)),
                ('course_instructor', models.CharField(max_length=20)),
                ('assessment_requirements', models.TextField()),
                ('course_fee', models.IntegerField()),
            ],
        ),
    ]