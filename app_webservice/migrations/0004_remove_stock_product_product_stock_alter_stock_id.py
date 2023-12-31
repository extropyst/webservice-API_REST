# Generated by Django 4.2.2 on 2023-06-17 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_webservice', '0003_alter_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.OneToOneField(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='app_webservice.stock'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
