# Generated by Django 3.0.3 on 2020-06-13 18:12

from django.db import migrations, models
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=150)),
                ('items', jsonfield.fields.JSONField()),
                ('prices', jsonfield.fields.JSONField()),
                ('types', jsonfield.fields.JSONField()),
                ('links', models.TextField()),
                ('total', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
