# Generated by Django 5.0.1 on 2024-03-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer_a', models.CharField(max_length=1000)),
                ('answer_b', models.CharField(max_length=1000)),
                ('answer_c', models.CharField(max_length=1000)),
                ('answer_d', models.CharField(max_length=1000)),
                ('selected_answer', models.CharField(max_length=1000)),
                ('correct_answer', models.CharField(max_length=1000)),
            ],
        ),
    ]
