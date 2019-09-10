# Generated by Django 2.2.5 on 2019-09-10 17:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mailinglist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriberMessage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('sent', models.DateTimeField(default=None, null=True)),
                ('last_attempt', models.DateTimeField(default=None, null=True)),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailinglist.Message')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailinglist.Subscriber')),
            ],
        ),
    ]
