# Generated by Django 5.0.3 on 2024-04-01 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0006_alter_quote_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='tags',
            field=models.ManyToManyField(to='quotes.tag'),
        ),
    ]