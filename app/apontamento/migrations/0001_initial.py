# Generated by Django 4.2.3 on 2023-10-05 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ponto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('entrada', models.DateTimeField()),
                ('primeiro', models.BooleanField(default=False)),
                ('segundo', models.BooleanField(default=False)),
                ('atraso', models.BooleanField(default=False)),
                ('saida', models.DateTimeField(blank=True, null=True)),
                ('fechado', models.BooleanField(default=False)),
                ('cliente_id', models.IntegerField(blank=True, null=True)),
                ('tiporeceita_id', models.IntegerField(blank=True, null=True)),
                ('atrasoautorizado', models.BooleanField(default=False)),
                ('usuario', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('entrada',),
            },
        ),
    ]