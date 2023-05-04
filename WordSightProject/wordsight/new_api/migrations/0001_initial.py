# Generated by Django 4.2.1 on 2023-05-04 08:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('keyword_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('count', models.IntegerField()),
                ('in_date', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('origin_address', models.URLField()),
                ('title', models.CharField(max_length=200)),
                ('created_date', models.DateField()),
                ('news_agency', models.CharField(max_length=10)),
                ('reporter', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=200, null=True)),
                ('people', models.CharField(max_length=200, null=True)),
                ('company', models.CharField(max_length=200, null=True)),
                ('tag', models.CharField(max_length=200)),
                ('news_contents', models.TextField()),
                ('image_link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='News_Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('keyword_id', models.OneToOneField(db_column='keyword_id', on_delete=django.db.models.deletion.CASCADE, to='new_api.keyword')),
                ('news_id', models.ForeignKey(db_column='news_id', on_delete=django.db.models.deletion.CASCADE, to='new_api.news')),
            ],
        ),
    ]
