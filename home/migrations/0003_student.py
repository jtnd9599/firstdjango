# Generated by Django 2.2.2 on 2019-06-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190619_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name', max_length=100, null=True)),
                ('usn', models.IntegerField(help_text='usn')),
                ('sem', models.IntegerField(help_text='semister')),
            ],
        ),
    ]
