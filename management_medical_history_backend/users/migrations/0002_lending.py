# Generated by Django 2.2.17 on 2021-09-21 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lending',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created At')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified At')),
                ('name', models.CharField(max_length=80)),
                ('address', models.CharField(blank=True, max_length=80, null=True)),
                ('telephone', models.CharField(blank=True, max_length=80, null=True)),
                ('cellphone', models.CharField(blank=True, max_length=80, null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Set to true when the lending is active.', verbose_name='Active')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
