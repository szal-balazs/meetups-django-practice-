# Generated by Django 4.2.6 on 2023-12-18 11:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mu_site', '0005_participant_alter_meetup_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meetup',
            name='participant',
            field=models.ManyToManyField(blank=True, to='mu_site.participant'),
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer',
            field=models.ManyToManyField(to='mu_site.organizer'),
        ),
    ]