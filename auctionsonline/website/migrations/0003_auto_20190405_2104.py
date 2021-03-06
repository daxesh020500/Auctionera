# Generated by Django 2.1.5 on 2019-04-05 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20190402_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='base_price',
            field=models.IntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('LAP', 'Laptop'), ('HH', 'household'), ('GAD', 'Gadget'), ('TEL', 'TV')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='website.User'),
        ),
    ]
