# Generated by Django 4.2.7 on 2023-11-17 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_rename_a_email_applicant_your_contact_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant',
            old_name='Your_Loan',
            new_name='Your_Amount',
        ),
    ]
