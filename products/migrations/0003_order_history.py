# Generated by Django 4.0.5 on 2022-10-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_cart_prd'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_history',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(blank=True, default='', max_length=100)),
                ('company_name', models.CharField(blank=True, default='', max_length=100)),
                ('country_name', models.CharField(blank=True, default='', max_length=100)),
                ('street', models.CharField(blank=True, default='', max_length=100)),
                ('street_optional', models.CharField(blank=True, default='', max_length=100)),
                ('city', models.CharField(blank=True, default='', max_length=100)),
                ('post_code', models.CharField(blank=True, default='', max_length=100)),
                ('phone_number', models.IntegerField(blank=True, default='')),
                ('email_address', models.CharField(blank=True, default='', max_length=100)),
                ('user_id', models.IntegerField(blank=True, default='')),
            ],
        ),
    ]
