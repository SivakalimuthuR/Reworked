# Generated by Django 5.0.6 on 2024-07-02 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('starting_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('closing_time', models.DateTimeField()),
            ],
        ),
    ]
