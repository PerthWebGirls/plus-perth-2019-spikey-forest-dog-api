# Generated by Django 2.2.4 on 2019-12-05 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('adoption_fee', models.CharField(max_length=50)),
                ('breeds_display', models.CharField(max_length=50)),
                ('coat', models.CharField(max_length=50)),
                ('contact_number', models.CharField(max_length=50)),
                ('created_at', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=2)),
                ('status', models.CharField(max_length=50)),
                ('desexed', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('group', models.CharField(max_length=50)),
                ('heart_worm_treated', models.CharField(max_length=50)),
                ('medical_notes', models.CharField(max_length=50)),
                ('personality', models.CharField(max_length=250)),
                ('senior', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('photos', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('vaccinate', models.CharField(max_length=50)),
                ('wormed', models.CharField(max_length=50)),
                ('postcode', models.CharField(max_length=4)),
                ('postcode_range', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AddField(
            model_name='profile',
            name='pet_preference',
            field=models.CharField(choices=[('any', 'Any'), ('cat', 'Cat'), ('dog', 'Dog'), ('rabbit', 'Rabbit'), ('bird', 'Bird')], default='any', max_length=6),
        ),
    ]
