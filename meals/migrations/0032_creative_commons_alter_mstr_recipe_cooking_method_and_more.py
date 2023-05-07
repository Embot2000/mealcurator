# Generated by Django 4.0.1 on 2023-01-08 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0031_mstr_search_trg'),
    ]

    operations = [
        migrations.CreateModel(
            name='creative_commons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('internal', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('link_text', models.CharField(max_length=256)),
                ('link', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='mstr_recipe',
            name='cooking_method',
            field=models.CharField(choices=[('st', 'Stove Top'), ('mi', 'Microwave'), ('bl', 'Blender'), ('gr', 'Grill'), ('ov', 'Oven'), ('pr', 'Pressure Cooker'), ('sc', 'Slow Cooker'), ('af', 'Air Fryer'), ('ra', 'Raw/Uncooked'), ('ot', 'Other')], max_length=2, verbose_name='Cooking Method'),
        ),
        migrations.AlterField(
            model_name='mstr_recipe',
            name='dish_type',
            field=models.CharField(choices=[('sp', 'Soup'), ('bk', 'Baked Dishes'), ('pa', 'Pasta Dishes'), ('cu', 'Curry Dishes'), ('ca', 'Casserole Dishes'), ('st', 'Stews'), ('sa', 'Salad'), ('lt', 'Light Dishes'), ('sm', 'Smoothie'), ('na', 'None of those')], max_length=2, verbose_name='Dish Type'),
        ),
        migrations.AlterField(
            model_name='mstr_recipe_list',
            name='uom',
            field=models.CharField(choices=[('qt', ''), ('ts', 'Tsp'), ('tb', 'Tbsp'), ('cu', 'Cup'), ('oz', 'Ounces'), ('lb', 'Pounds'), ('ml', 'Milliliter'), ('ll', 'Liter'), ('ea', 'Each'), ('dz', 'Dozen'), ('bu', 'Bunch'), ('st', 'Stalks'), ('cl', 'Cloves')], default='qt', max_length=2, verbose_name='Unit of Measure'),
        ),
        migrations.AlterField(
            model_name='raw_recipe',
            name='cooking_method',
            field=models.CharField(choices=[('st', 'Stove Top'), ('mi', 'Microwave'), ('bl', 'Blender'), ('gr', 'Grill'), ('ov', 'Oven'), ('pr', 'Pressure Cooker'), ('sc', 'Slow Cooker'), ('af', 'Air Fryer'), ('ra', 'Raw/Uncooked'), ('ot', 'Other')], max_length=2, verbose_name='Cooking Method'),
        ),
        migrations.AlterField(
            model_name='raw_recipe',
            name='dish_type',
            field=models.CharField(choices=[('sp', 'Soup'), ('bk', 'Baked Dishes'), ('pa', 'Pasta Dishes'), ('cu', 'Curry Dishes'), ('ca', 'Casserole Dishes'), ('st', 'Stews'), ('sa', 'Salad'), ('lt', 'Light Dishes'), ('sm', 'Smoothie'), ('na', 'None of those')], max_length=2, verbose_name='Dish Type'),
        ),
    ]
