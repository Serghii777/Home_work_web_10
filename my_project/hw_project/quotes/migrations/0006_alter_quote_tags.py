# Generated by Django 5.0.3 on 2024-04-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0005_remove_tag_tag_of_username_alter_author_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='tags',
            field=models.ManyToManyField(related_name='quotes', to='quotes.tag'),
        ),
    ]
