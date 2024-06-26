# Generated by Django 4.1.7 on 2024-05-17 18:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('Id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=13)),
                ('Username', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('Id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=50)),
                ('Author', models.CharField(max_length=50)),
                ('Category', models.CharField(max_length=50, null=True)),
                ('Description', models.TextField()),
                ('Available', models.BooleanField(default=False)),
                ('Cover', models.ImageField(upload_to='static/Covers-%y-%m-%d')),
                ('BorrowingNumber', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('Id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=13)),
                ('Username', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(default='user', max_length=30, unique=True)),
                ('Rule', models.BooleanField(default=True)),
                ('Password', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('Id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('BorrowDate', models.DateField(default=django.utils.timezone.now)),
                ('ReturnDate', models.DateField(default=django.utils.timezone.now)),
                ('BookId', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Controlling.book')),
                ('ClientId', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Controlling.client')),
            ],
        ),
    ]
