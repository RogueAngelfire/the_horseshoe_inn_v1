# Generated by Django 3.1.1 on 2020-11-05 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20201105_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.product'),
        ),
    ]
