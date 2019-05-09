# Generated by Django 2.2.1 on 2019-05-09 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField()),
                ('data_nascimento', models.DateField()),
                ('eventos', models.ManyToManyField(to='eventos.Evento')),
            ],
        ),
    ]