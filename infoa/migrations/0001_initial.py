# Generated by Django 3.0.8 on 2020-08-03 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=40)),
                ('last', models.CharField(max_length=40)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, verbose_name='Gender')),
                ('start_date', models.DateField(blank=True, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End Date')),
                ('phone', models.CharField(blank=True, max_length=12, verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=30, null=True, unique=True, verbose_name='Email')),
                ('emp_type', models.CharField(blank=True, choices=[('P', 'Part Time'), ('F', 'Full TIme')], max_length=1, verbose_name='Employment Type')),
                ('dept', models.CharField(blank=True, max_length=20, verbose_name='Department')),
                ('position', models.CharField(blank=True, max_length=40, verbose_name='Position')),
                ('benefits', models.ManyToManyField(blank=True, to='infoa.Benefit')),
            ],
        ),
    ]
