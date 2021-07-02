# Generated by Django 2.2.10 on 2021-06-29 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalTag',
            fields=[
                ('id', models.BigIntegerField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True, db_column='created')),
            ],
            options={
                'db_table': 'GlobalTag',
            },
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
