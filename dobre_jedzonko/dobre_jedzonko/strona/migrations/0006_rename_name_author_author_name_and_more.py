# Generated by Django 4.1.4 on 2022-12-28 17:29

from django.db import migrations, models
import strona.pathandrename


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0005_recipe_linkyt_alter_recipe_photo_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='author_name',
        ),
        migrations.AlterField(
            model_name='author',
            name='author_photo',
            field=models.ImageField(upload_to=strona.pathandrename.PathAndRename.wrapper),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(upload_to=strona.pathandrename.PathAndRename.wrapper),
        ),
    ]