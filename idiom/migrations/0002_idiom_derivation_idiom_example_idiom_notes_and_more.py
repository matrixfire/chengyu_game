# Generated by Django 5.1.4 on 2024-12-25 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idiom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idiom',
            name='derivation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='idiom',
            name='example',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='idiom',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='idiom',
            name='weight',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Pinyin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pinyin_text', models.CharField(max_length=20)),
                ('tone_marks', models.CharField(blank=True, max_length=20, null=True)),
                ('idiom', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pinyin', to='idiom.idiom')),
            ],
        ),
    ]
