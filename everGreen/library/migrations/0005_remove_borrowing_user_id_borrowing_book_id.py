# Generated by Django 4.2.1 on 2023-05-23 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_rename_date_issued_librarycard_issueddate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowing',
            name='user_id',
        ),
        migrations.AddField(
            model_name='borrowing',
            name='book_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.book'),
        ),
    ]
