# Generated by Django 4.2.7 on 2023-11-16 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_farmer_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('ID_Number', models.IntegerField()),
                ('phone_number', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('date_applied', models.DateTimeField(auto_now=True)),
                ('date_to_pay', models.DateTimeField(auto_now=True)),
                ('percentage_interest', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
