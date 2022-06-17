# Generated by Django 4.0.5 on 2022-06-17 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0004_neighborhood'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('population', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='profilepics')),
                ('description', models.TextField()),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hood', to='area.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='NeighborHood',
        ),
    ]