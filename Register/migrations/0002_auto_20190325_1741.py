# Generated by Django 2.1.7 on 2019-03-25 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Slot', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('Course_Code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Course_Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('Lect_No', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('CellPhone_No', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='Course_Code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register.Courses'),
        ),
        migrations.AddField(
            model_name='class',
            name='Lect_No',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register.Lecturer'),
        ),
        migrations.AddField(
            model_name='class',
            name='Student_No',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register.StudentsRegister'),
        ),
        migrations.AddField(
            model_name='announcements',
            name='Course_Code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register.Courses'),
        ),
        migrations.AddField(
            model_name='announcements',
            name='Lect_No',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register.Lecturer'),
        ),
    ]
