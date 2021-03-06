# Generated by Django 2.2.4 on 2019-10-15 17:04

from decimal import Decimal

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("airtime", "0011_initial")]

    operations = [
        migrations.RemoveField(model_name="airtimetransfer", name="data"),
        migrations.RemoveField(model_name="airtimetransfer", name="message"),
        migrations.RemoveField(model_name="airtimetransfer", name="response"),
        migrations.RemoveField(model_name="airtimetransfer", name="channel"),
        migrations.RemoveField(model_name="airtimetransfer", name="created_by"),
        migrations.RemoveField(model_name="airtimetransfer", name="is_active"),
        migrations.RemoveField(model_name="airtimetransfer", name="modified_by"),
        migrations.RemoveField(model_name="airtimetransfer", name="modified_on"),
        migrations.AlterField(
            model_name="airtimetransfer",
            name="contact",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="contacts.Contact"),
        ),
        migrations.AlterField(
            model_name="airtimetransfer",
            name="org",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="airtime_transfers", to="orgs.Org"
            ),
        ),
        migrations.AlterField(
            model_name="airtimetransfer",
            name="status",
            field=models.CharField(choices=[("S", "Success"), ("F", "Failed")], max_length=1),
        ),
        migrations.AlterField(
            model_name="airtimetransfer",
            name="created_on",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="airtimetransfer", name="sender", field=models.CharField(max_length=64, null=True)
        ),
        migrations.AddField(
            model_name="airtimetransfer", name="currency", field=models.CharField(max_length=32, null=True)
        ),
        migrations.AlterField(
            model_name="airtimetransfer", name="amount", field=models.DecimalField(decimal_places=2, max_digits=10)
        ),
        migrations.RenameField(model_name="airtimetransfer", old_name="amount", new_name="actual_amount"),
        migrations.AlterField(
            model_name="airtimetransfer",
            name="denomination",
            field=models.DecimalField(decimal_places=2, default=Decimal(0), max_digits=10),
            preserve_default=False,
        ),
        migrations.RenameField(model_name="airtimetransfer", old_name="denomination", new_name="desired_amount"),
    ]
