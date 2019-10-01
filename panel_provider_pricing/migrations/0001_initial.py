# Generated by Django 2.2.5 on 2019-09-25 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PanelProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TargetGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.IntegerField(default=None)),
                ('name', models.CharField(max_length=100)),
                ('secret_code', models.CharField(max_length=100)),
                ('panel_provider_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel_provider_pricing.PanelProvider')),
                ('parent_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel_provider_pricing.TargetGroup')),
            ],
        ),
        migrations.CreateModel(
            name='LocationGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel_provider_pricing.Country')),
                ('panel_provider_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel_provider_pricing.PanelProvider')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.IntegerField(default=None)),
                ('name', models.CharField(max_length=100)),
                ('secret_code', models.CharField(max_length=100)),
                ('location_groups', models.ManyToManyField(to='panel_provider_pricing.LocationGroup')),
            ],
        ),
        migrations.AddField(
            model_name='country',
            name='panel_provider_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel_provider_pricing.PanelProvider'),
        ),
        migrations.AddField(
            model_name='country',
            name='target_groups',
            field=models.ManyToManyField(to='panel_provider_pricing.TargetGroup'),
        ),
    ]