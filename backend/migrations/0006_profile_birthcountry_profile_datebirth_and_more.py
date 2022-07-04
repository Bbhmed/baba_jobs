# Generated by Django 4.0.4 on 2022-06-10 04:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='birthcountry',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='datebirth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='deactive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='emailcontact',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='livecountry',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='numbercontact',
            field=models.BigIntegerField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.DeleteModel(
            name='Lead',
        ),
    ]
