# Generated by Django 4.2.4 on 2023-08-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datainput', '0005_alter_patientdata_eradicated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdata',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]