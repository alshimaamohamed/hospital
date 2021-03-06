# Generated by Django 3.1.2 on 2021-02-06 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Places.building')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Scan_lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Places.floor')),
                ('main_anchor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Items.anchor')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('type', models.CharField(choices=[('single', 'single'), ('double', 'double'), ('triple', 'triple')], max_length=32)),
                ('avilibility', models.BooleanField(default=True)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Places.floor')),
                ('main_anchor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Items.anchor')),
            ],
        ),
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Places.floor')),
            ],
        ),
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Places.floor')),
                ('main_anchor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Items.anchor')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Places.floor')),
                ('main_anchor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Items.anchor')),
            ],
        ),
        migrations.CreateModel(
            name='Kitchen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Places.floor')),
                ('main_anchor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Items.meal')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Places.floor')),
            ],
        ),
        migrations.CreateModel(
            name='Charging_station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Places.floor')),
                ('main_anchor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Items.anchor')),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Places.hospital'),
        ),
        migrations.CreateModel(
            name='Bio_labs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Places.floor')),
            ],
        ),
    ]
