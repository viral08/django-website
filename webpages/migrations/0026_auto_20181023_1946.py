# Generated by Django 2.1 on 2018-10-23 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0025_delete_assignments_by_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='assignment_save',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=200)),
                ('ass_title', models.CharField(max_length=1000)),
                ('content', models.CharField(default='User0', max_length=20000)),
            ],
        ),
        migrations.AddField(
            model_name='assignment_by_student',
            name='ass_title',
            field=models.CharField(default='ass. 0', max_length=1000),
        ),
    ]
