# Generated by Django 3.1.4 on 2021-01-06 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Login',
            },
        ),
        migrations.CreateModel(
            name='NewsType',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('tName', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'NewsType',
            },
        ),
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('nTitle', models.CharField(max_length=200)),
                ('nAuthor', models.CharField(max_length=20)),
                ('nContent', models.CharField(max_length=1000)),
                ('nPubDateTime', models.DateTimeField(auto_now_add=True)),
                ('NStatus', models.BooleanField()),
                ('tid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.newstype')),
            ],
            options={
                'db_table': 'NewsInfo',
            },
        ),
    ]
