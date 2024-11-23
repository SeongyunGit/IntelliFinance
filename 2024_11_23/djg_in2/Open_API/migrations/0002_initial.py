# Generated by Django 4.2.16 on 2024-11-23 06:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Open_API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='integrationproductoption',
            name='deposit_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='Open_API.integrationproduct'),
        ),
        migrations.AddField(
            model_name='integrationproduct',
            name='like_users',
            field=models.ManyToManyField(related_name='like_product', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='companylistoption',
            name='deposit_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='Open_API.companylist'),
        ),
        migrations.AddField(
            model_name='comments',
            name='bank_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_product', to='Open_API.integrationproduct'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together={('user', 'bank_product')},
        ),
        migrations.AlterUniqueTogether(
            name='comments',
            unique_together={('user', 'bank_product')},
        ),
    ]
