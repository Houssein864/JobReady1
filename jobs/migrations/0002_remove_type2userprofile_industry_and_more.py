# Generated by Django 5.0.3 on 2024-03-22 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type2userprofile',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='type1userprofile',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='type1userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='type2userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Industry',
        ),
        migrations.DeleteModel(
            name='Type1UserProfile',
        ),
        migrations.DeleteModel(
            name='Type2UserProfile',
        ),
    ]