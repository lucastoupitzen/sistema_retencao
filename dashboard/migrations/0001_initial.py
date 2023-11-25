# Generated by Django 4.0.10 on 2023-11-02 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('nro_usp', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=80)),
                ('ano_ingresso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('codigo', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('semestre_ideal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Demanda_por_disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cursando', models.BooleanField(default=False)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.aluno')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='dashboard.disciplina')),
            ],
        ),
    ]
