# Generated by Django 2.1 on 2018-10-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0026_auto_20181023_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment_submitted',
            name='s_class',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
