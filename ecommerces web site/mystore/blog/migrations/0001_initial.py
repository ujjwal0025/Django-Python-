# Generated by Django 5.0.2 on 2024-04-10 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogger',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('heading1', models.CharField(max_length=500)),
                ('cont_heading1', models.CharField(max_length=500)),
                ('heading2', models.CharField(max_length=500)),
                ('cont_heading2', models.CharField(max_length=500)),
                ('thumnail', models.ImageField(default='', upload_to='shop/images')),
            ],
        ),
    ]
