# Generated by Django 5.0.4 on 2024-04-22 12:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0010_alter_mywords_word"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="stories",
            new_name="Story",
        ),
        migrations.RenameField(
            model_name="rating",
            old_name="stories",
            new_name="story",
        ),
        migrations.AlterUniqueTogether(
            name="rating",
            unique_together={("user", "story")},
        ),
    ]
