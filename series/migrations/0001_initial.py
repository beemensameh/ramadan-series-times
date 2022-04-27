# Generated by Django 4.0.3 on 2022-04-03 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('channels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ChannelSerie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='channels.channel')),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.serie')),
            ],
        ),
    ]
