# Generated by Django 3.1.2 on 2021-02-06 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Tasks', '0001_initial'),
        ('Places', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='acessed_tasks',
            field=models.ManyToManyField(to='Tasks.Task'),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='receptionist',
            name='reception',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Places.reception'),
        ),
        migrations.AddField(
            model_name='patient_mate',
            name='Patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Person.patient'),
        ),
        migrations.AddField(
            model_name='patient',
            name='stay_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Places.room'),
        ),
        migrations.AddField(
            model_name='nurse',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Places.department'),
        ),
        migrations.AddField(
            model_name='mesurements',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Person.patient'),
        ),
        migrations.AddField(
            model_name='hospital_manager',
            name='manager_office',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Places.office'),
        ),
        migrations.AddField(
            model_name='hospital_manager',
            name='manages',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Places.hospital'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Places.department'),
        ),
        migrations.AddField(
            model_name='department_manager',
            name='manages',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Places.department'),
        ),
    ]