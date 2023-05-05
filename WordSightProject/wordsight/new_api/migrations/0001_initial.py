from django.db import migrations, models
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
            name='Tag',
            fields=[
                ('tag_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('class1', models.CharField(max_length=20, null=True)),
                ('class2', models.CharField(max_length=20, null=True)),
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
                ('tag_list', models.TextField(null=True)),
                ('news_contents', models.TextField()),
                ('image_link', models.URLField()),
                ('keyword_list', models.TextField(null=True)),
                ('keyword', models.ManyToManyField(to='new_api.keyword')),
                ('tag', models.ManyToManyField(related_name='related_tag', to='new_api.tag')),
            ],
        ),
    ]
