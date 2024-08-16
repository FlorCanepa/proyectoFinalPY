# Generated by Django 4.2.15 on 2024-08-15 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_author_autor_rename_publisher_editorial_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
        migrations.AddField(
            model_name='libro',
            name='editorial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.editorial'),
        ),
    ]
