# Generated by Django 3.2.8 on 2021-12-03 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DigitalSociety_APP', '0004_society_member'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='society_member',
            table='society_member',
        ),
        migrations.CreateModel(
            name='Society_secretary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(default='', max_length=20)),
                ('Mobile', models.CharField(default='', max_length=10)),
                ('Master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DigitalSociety_APP.master')),
            ],
            options={
                'db_table': 'society_secretary',
            },
        ),
    ]
