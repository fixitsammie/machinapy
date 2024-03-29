# Generated by Django 3.0.3 on 2020-08-10 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('manager_email', models.EmailField(max_length=100)),
                ('foundation_date', models.DateField(blank=True)),
                ('participant_type', models.CharField(choices=[('Band', 'Band'), ('Carriage', 'Carriage')], max_length=10)),
                ('order_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
