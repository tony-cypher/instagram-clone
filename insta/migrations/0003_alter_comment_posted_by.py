# Generated by Django 4.1 on 2024-09-15 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("insta", "0002_comment_post_delete_profile_comment_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="posted_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
