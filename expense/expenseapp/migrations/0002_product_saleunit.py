# Generated by Django 4.2.3 on 2023-08-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenseapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='saleunit',
            field=models.IntegerField(null=True),
        ),
    ]
