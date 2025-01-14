# Generated by Django 2.2.17 on 2021-09-22 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_diagnosticaid_externalcause_medicine_presentation_specialist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created At')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified At')),
                ('description', models.CharField(max_length=120)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
