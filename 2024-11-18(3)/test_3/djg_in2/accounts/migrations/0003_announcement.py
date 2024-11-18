# Generated by Django 4.2.16 on 2024-11-18 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement_title', models.CharField(max_length=50)),
                ('announcement_content', models.CharField(max_length=255)),
                ('announcement_important', models.BooleanField()),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
