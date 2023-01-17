# Generated by Django 4.1.5 on 2023-01-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("divulgar", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Racas",
            new_name="Raca",
        ),
        migrations.AlterField(
            model_name="pet",
            name="status",
            field=models.CharField(
                choices=[("P", "Para adoção"), ("A", "Adotado")],
                default="P",
                max_length=1,
            ),
        ),
        migrations.AlterField(
            model_name="pet",
            name="telefone",
            field=models.CharField(max_length=50),
        ),
    ]