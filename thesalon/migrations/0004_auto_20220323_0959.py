# Generated by Django 3.2.9 on 2022-03-23 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesalon', '0003_auto_20220322_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('Email', models.EmailField(max_length=100)),
                ('Message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='Gender',
            field=models.IntegerField(choices=[(0, 'Male'), (1, 'Female')]),
        ),
    ]
