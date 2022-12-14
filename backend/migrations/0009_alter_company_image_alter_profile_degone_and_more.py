# Generated by Django 4.0.4 on 2022-06-14 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_rename_name_company_companyname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, default='default-logo.png', null=True, upload_to='photos%d%y%m'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='degone',
            field=models.ImageField(blank=True, default='def-profile.png', null=True, upload_to='photos%d%y%m'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='degthree',
            field=models.ImageField(blank=True, default='def-profile.png', null=True, upload_to='photos%d%y%m'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='degtwo',
            field=models.ImageField(blank=True, default='def-profile.png', null=True, upload_to='photos%d%y%m'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(blank=True, default='def-profile.png', null=True, upload_to='photos%d%y%m'),
        ),
    ]
