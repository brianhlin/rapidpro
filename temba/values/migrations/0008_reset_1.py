# Generated by Django 1.10.5 on 2017-01-06 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0006_reset_1'),
        ('flows', '0079_reset_1'),
        ('contacts', '0046_reset_1'),
        ('orgs', '0029_reset_1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_uuid', models.CharField(db_index=True, help_text='The rule that matched, only appropriate for RuleSet values', max_length=255, null=True)),
                ('category', models.CharField(help_text='The name of the category this value matched in the RuleSet', max_length=128, null=True)),
                ('string_value', models.TextField(help_text='The string value or string representation of this value', max_length=640)),
                ('decimal_value', models.DecimalField(decimal_places=8, help_text='The decimal value of this value if any.', max_digits=36, null=True)),
                ('datetime_value', models.DateTimeField(help_text='The datetime value of this value if any.', null=True)),
                ('media_value', models.TextField(help_text='The media value if any.', max_length=640, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='values', to='contacts.Contact')),
                ('contact_field', models.ForeignKey(help_text='The ContactField this value is for, if any', null=True, on_delete=django.db.models.deletion.SET_NULL, to='contacts.ContactField')),
                ('location_value', models.ForeignKey(help_text='The location value of this value if any.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='locations.AdminBoundary')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgs.Org')),
                ('ruleset', models.ForeignKey(help_text='The RuleSet this value is for, if any', null=True, on_delete=django.db.models.deletion.SET_NULL, to='flows.RuleSet')),
                ('run', models.ForeignKey(help_text='The FlowRun this value is for, if any', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='values', to='flows.FlowRun')),
            ],
        ),
    ]
