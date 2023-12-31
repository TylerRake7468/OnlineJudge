# Generated by Django 4.2.5 on 2023-09-23 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ojapp', '0006_problem_constraints_problem_example_explain_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('language', models.CharField(choices=[('C++', 'C++'), ('C', 'C'), ('Python3', 'Python3'), ('Python2', 'Python2'), ('Java', 'Java')], default='c++', max_length=10)),
                ('run_time', models.FloatField(default=0, null=True)),
                ('status', models.CharField(default='Wrong Answer', max_length=100)),
                ('code', models.TextField(default='', max_length=10000)),
                ('error_message', models.TextField(null=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojapp.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ojapp.user')),
            ],
        ),
    ]
