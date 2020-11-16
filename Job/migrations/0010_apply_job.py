# Generated by Django 3.1.3 on 2020-11-16 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0009_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='job',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='apply_job', to='Job.job'),
            preserve_default=False,
        ),
    ]