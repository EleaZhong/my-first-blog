# Generated by Django 2.0.7 on 2019-03-14 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190314_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='haha', max_length=50),
            preserve_default=False,
        ),
    ]
