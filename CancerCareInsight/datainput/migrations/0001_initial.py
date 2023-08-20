# Generated by Django 4.2.4 on 2023-08-20 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('cancer_type', models.CharField(choices=[('Breast', 'Breast Cancer'), ('Lung', 'Lung Cancer')], max_length=50)),
                ('stage', models.PositiveIntegerField()),
                ('diagnosis_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_type', models.CharField(choices=[('Surgery', 'Surgery'), ('Chemotherapy', 'Chemotherapy'), ('Radiation', 'Radiation')], max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('medication_names', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datainput.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eradicated', models.BooleanField()),
                ('recurrence', models.BooleanField()),
                ('side_effects', models.TextField()),
                ('quality_of_life_post_treatment', models.PositiveIntegerField()),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='datainput.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direct_costs', models.DecimalField(decimal_places=2, max_digits=10)),
                ('indirect_costs', models.DecimalField(decimal_places=2, max_digits=10)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='datainput.patient')),
            ],
        ),
    ]
