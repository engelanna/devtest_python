# Generated by Django 2.2.6 on 2019-10-02 22:24

from django.db import migrations, models
import django.db.models.deletion
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='PanelProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('price_calculation_strategy', models.CharField(default='CharacterCount', max_length=255)),
            ],
            options={
                'db_table': 'panel_providers',
            },
        ),
        migrations.CreateModel(
            name='TargetGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.IntegerField(default=None)),
                ('name', models.CharField(max_length=100)),
                ('secret_code', encrypted_model_fields.fields.EncryptedCharField()),
                ('panel_provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel_provider_pricing.PanelProvider')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel_provider_pricing.TargetGroup')),
            ],
            options={
                'db_table': 'target_groups',
            },
        ),
        migrations.CreateModel(
            name='LocationGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel_provider_pricing.Country')),
                ('panel_provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel_provider_pricing.PanelProvider')),
            ],
            options={
                'db_table': 'location_groups',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panel_size', models.IntegerField(default=0)),
                ('external_id', models.IntegerField(default=None)),
                ('name', models.CharField(max_length=255)),
                ('secret_code', encrypted_model_fields.fields.EncryptedCharField()),
                ('location_groups', models.ManyToManyField(to='panel_provider_pricing.LocationGroup')),
            ],
            options={
                'db_table': 'locations',
            },
        ),
        migrations.AddField(
            model_name='country',
            name='panel_provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='panel_provider_pricing.PanelProvider'),
        ),
        migrations.AddField(
            model_name='country',
            name='target_groups',
            field=models.ManyToManyField(to='panel_provider_pricing.TargetGroup'),
        ),
    ]
