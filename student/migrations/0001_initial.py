# Generated by Django 5.0.6 on 2024-07-09 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=30)),
                ('s_class', models.CharField(max_length=30)),
                ('s_addr', models.CharField(max_length=30)),
                ('s_school', models.CharField(max_length=30)),
                ('s_email', models.EmailField(max_length=30)),
            ],
        ),
    ]
