# Generated by Django 2.2.17 on 2021-04-07 17:42

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created At')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified At')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('second_name', models.CharField(max_length=50, null=True)),
                ('surname', models.CharField(max_length=80, null=True)),
                ('second_surname', models.CharField(max_length=80, null=True)),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exist.'}, max_length=254, unique=True, verbose_name='Email address')),
                ('is_verified', models.BooleanField(default=True, help_text='Set to true when the user have verified email address.', verbose_name='Verified')),
                ('role', models.CharField(choices=[('ROLE_ADMIN', 'Admin role'), ('ROLE_PATIENT', 'Patient role'), ('ROLE_AUXILIAR', 'Auxiliar role'), ('ROLE_PROFESSIONAL', 'Professional role')], default='ROLE_ADMIN', max_length=30)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created At')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified At')),
                ('phone_number', models.CharField(blank=True, max_length=80)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='users/pictures/', verbose_name='Profile picture')),
                ('surname', models.CharField(blank=True, max_length=80, null=True)),
                ('second_surname', models.CharField(blank=True, max_length=80, null=True)),
                ('first_name', models.CharField(blank=True, max_length=80, null=True)),
                ('second_name', models.CharField(blank=True, max_length=80, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=80, null=True)),
                ('nuip', models.CharField(blank=True, max_length=80, null=True)),
                ('address', models.CharField(blank=True, max_length=80, null=True)),
                ('neighborhood', models.CharField(blank=True, max_length=120, null=True)),
                ('telephone', models.CharField(blank=True, max_length=80, null=True)),
                ('cellphone', models.CharField(blank=True, max_length=80, null=True)),
                ('usual_occupation', models.CharField(blank=True, max_length=120, null=True)),
                ('special_population', models.CharField(blank=True, max_length=80, null=True)),
                ('sexual_orientation', models.CharField(blank=True, max_length=80, null=True)),
                ('social_security_scheme', models.CharField(blank=True, max_length=80, null=True)),
                ('eps', models.CharField(blank=True, max_length=120, null=True)),
                ('eps_level', models.CharField(blank=True, max_length=20, null=True)),
                ('affiliation_number', models.CharField(blank=True, max_length=100, null=True)),
                ('civil_status', models.CharField(blank=True, max_length=80, null=True)),
                ('scholarship', models.CharField(blank=True, max_length=100, null=True)),
                ('ethnic_group', models.CharField(blank=True, max_length=120, null=True)),
                ('type_degree_disability', models.CharField(blank=True, max_length=80, null=True)),
                ('work_address', models.CharField(blank=True, max_length=20, null=True)),
                ('work_phone_one', models.CharField(blank=True, max_length=20, null=True)),
                ('work_phone_two', models.CharField(blank=True, max_length=20, null=True)),
                ('last_name_mom', models.CharField(blank=True, max_length=80, null=True)),
                ('first_name_mom', models.CharField(blank=True, max_length=80, null=True)),
                ('responsable', models.CharField(blank=True, max_length=120, null=True)),
                ('relationship_person_in_charge', models.CharField(blank=True, max_length=100, null=True)),
                ('address_person_in_charge', models.CharField(blank=True, max_length=80, null=True)),
                ('telephone_person_in_charge', models.CharField(blank=True, max_length=80, null=True)),
                ('hc_open_place', models.CharField(blank=True, max_length=120, null=True)),
                ('user_create_hc', models.CharField(blank=True, max_length=80, null=True)),
                ('hc_transfer_to', models.CharField(blank=True, max_length=120, null=True)),
                ('transfer_date', models.DateField(blank=True, null=True)),
                ('date_last_attention', models.DateField(blank=True, null=True)),
                ('user_alert', models.CharField(blank=True, max_length=120, null=True)),
                ('user_message_hc', models.CharField(blank=True, max_length=120, null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.City')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.Country')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.Department')),
                ('nationality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='services.Nacionality')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='Created At')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='Modified At')),
                ('type', models.CharField(choices=[('ACCOUNT_CONFIRMATION', 'Account confirmation'), ('RESET_PASSWORD', 'Reset password')], max_length=100)),
                ('key', models.CharField(max_length=254)),
                ('valid_from', models.DateTimeField(auto_now_add=True)),
                ('valid_until', models.DateTimeField()),
                ('is_available', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
                'unique_together': {('type', 'key')},
            },
        ),
    ]
