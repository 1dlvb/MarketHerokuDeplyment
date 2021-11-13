# Generated by Django 3.2.6 on 2021-11-13 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20211112_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_key', models.CharField(max_length=100, verbose_name='Feature key')),
                ('feature_name', models.CharField(max_length=255, verbose_name='Feature name')),
                ('postfix_for_value', models.CharField(blank=True, help_text='For example, for the characteristic "wheel size", you can add the postfix "inches" to the value. Wheels 29 inches.', max_length=20, null=True, verbose_name='Postfix for the value')),
                ('use_in_filter', models.BooleanField(default=False, verbose_name='Use to filter products in the template')),
                ('filter_type', models.CharField(choices=[('radio', 'Radiobutton'), ('checkbox', 'Checkbox')], default='checkbox', max_length=20, verbose_name='Filter type')),
                ('filter_measure', models.CharField(help_text='For example, "Fork travel (mm)."', max_length=50, verbose_name='The unit of measurement for the filter')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFeaturesValidators',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_value', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Feature value')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.category', verbose_name='Category')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.productfeatures', verbose_name='Features')),
            ],
        ),
    ]