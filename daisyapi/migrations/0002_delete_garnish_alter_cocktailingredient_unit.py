# Generated by Django 4.1 on 2022-08-29 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('daisyapi', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Garnish',
        ),
        migrations.AlterField(
            model_name='cocktailingredient',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daisyapi.unit'),
        ),
    ]
