# Generated by Django 2.0.2 on 2018-06-24 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_bids', models.IntegerField()),
                ('time_starting', models.DateTimeField()),
                ('time_ending', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_time', models.DateTimeField()),
                ('auction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Auction')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('time_sent', models.DateTimeField()),
                ('auction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Auction')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=500)),
                ('quantity', models.IntegerField()),
                ('category', models.CharField(choices=[('LAP', 'Laptop'), ('CON', 'Console'), ('GAD', 'Gadget'), ('GAM', 'Game'), ('TEL', 'TV')], max_length=2)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=254)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=6)),
                ('firstname', models.CharField(max_length=56)),
                ('lastname', models.CharField(max_length=45)),
                ('cellphone', models.CharField(max_length=14)),
                ('address', models.CharField(max_length=255)),
                ('town', models.CharField(max_length=45)),
                ('post_code', models.CharField(max_length=45)),
                ('country', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Auction')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.User')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.User'),
        ),
        migrations.AddField(
            model_name='bid',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.User'),
        ),
        migrations.AddField(
            model_name='auction',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Product'),
        ),
    ]
