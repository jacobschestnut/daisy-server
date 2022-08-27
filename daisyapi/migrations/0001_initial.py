# Generated by Django 4.1 on 2022-08-27 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cocktail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('description', models.CharField(max_length=255)),
                ('instructions', models.CharField(max_length=255)),
                ('img_url', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Garnish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Glass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Ice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='IngredientType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Preparation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Mixologist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient_type', to='daisyapi.ingredienttype')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cocktail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daisyapi.cocktail')),
                ('mixologist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daisyapi.mixologist')),
            ],
        ),
        migrations.CreateModel(
            name='CocktailIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=3)),
                ('cocktail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daisyapi.cocktail')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daisyapi.ingredient')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daisyapi.unit')),
            ],
        ),
        migrations.AddField(
            model_name='cocktail',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daisyapi.mixologist'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='glass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daisyapi.glass'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='ice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daisyapi.ice'),
        ),
        migrations.AddField(
            model_name='cocktail',
            name='preparation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daisyapi.preparation'),
        ),
    ]
