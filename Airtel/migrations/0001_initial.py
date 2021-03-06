# Generated by Django 4.0.2 on 2022-02-06 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('expire', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('type', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10)),
                ('previousPlan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Airtel.plans')),
            ],
        ),
        migrations.CreateModel(
            name='Plans_Offers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Airtel.offers')),
                ('plan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Airtel.plans')),
            ],
        ),
    ]
