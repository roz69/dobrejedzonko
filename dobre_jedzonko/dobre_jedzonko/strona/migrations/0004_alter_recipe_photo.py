# Generated by Django 4.1.4 on 2022-12-27 18:59

from django.db import migrations, models
import strona.pathandrename


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0003_alter_recipe_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(blank=True, upload_to=strona.pathandrename.PathAndRename.wrapper),
        ),
    ]