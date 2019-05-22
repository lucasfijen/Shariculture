# Generated by Django 2.0.4 on 2019-05-22 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_development', '0003_auto_20190522_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='audio_file',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='service_development.SpokenUserInput', verbose_name='Recorded audio'),
        ),
        migrations.AddField(
            model_name='offer',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.Language', verbose_name='Offer_language'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='product_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.Product', verbose_name='Product type'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.Region', verbose_name='Region'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='service_development.KasaDakaUser', verbose_name='Caller id'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='voice_label',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.VoiceLabel', verbose_name='Voice label'),
        ),
    ]