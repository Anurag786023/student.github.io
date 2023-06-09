# Generated by Django 4.1.7 on 2023-05-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('clas', models.CharField(choices=[('LKG', 'LKG'), ('UKG', 'UKG'), ('NURSERY', 'NURSERY'), ('ONE', 'ONE'), ('TOW', 'TWO'), ('THREE', 'THREE'), ('FOUR', 'FOUR'), ('FIVE', 'FIVE'), ('SIX', 'SIX'), ('SEVEN', 'SEVEN'), ('EIGHT', 'EIGHT'), ('NINE', 'NINE'), ('TEN', 'TEN'), ('ELEVEN', 'ELEVEN'), ('TWELEVE', 'TWELEVE')], default='none', max_length=10)),
                ('role_number', models.IntegerField(max_length=5)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
