# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-02 21:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_pgjson.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunitySponsorship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_data', django_pgjson.fields.JsonField(default={})),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventSponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_data', django_pgjson.fields.JsonField(default={})),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_sponsors', to='events.Event')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_data', django_pgjson.fields.JsonField(default={})),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('logo', models.ImageField(upload_to=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SponsorTier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_data', django_pgjson.fields.JsonField(default={})),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='eventsponsor',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_sponsors', to='sponsorship.Sponsor'),
        ),
        migrations.AddField(
            model_name='communitysponsorship',
            name='sponsor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_sponsorships', to='sponsorship.Sponsor'),
        ),
        migrations.AddField(
            model_name='communitysponsorship',
            name='tier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_sponsorships', to='sponsorship.SponsorTier'),
        ),
    ]
