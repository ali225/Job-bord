# Generated by Django 3.1.3 on 2020-11-16 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0006_auto_20201115_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
