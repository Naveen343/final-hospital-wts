# Generated by Django 4.1.7 on 2023-08-07 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(choices=[('Cardiology', 'Cardiology'), ('Orthopedics', 'Orthopedics'), ('Gynecology', 'Gynecology'), ('Neurology', 'Neurology')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
    ]