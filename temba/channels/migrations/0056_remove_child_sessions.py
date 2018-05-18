# Generated by Django 1.10.5 on 2017-01-25 02:25

from django.db import migrations


def remove_child_sessions(apps, schema_editor):
    ChannelSession = apps.get_model('channels', 'ChannelSession')
    FlowRun = apps.get_model('flows', 'FlowRun')

    child_sessions = ChannelSession.objects.all().exclude(parent=None)

    for child in child_sessions:
        FlowRun.objects.filter(session=child).update(session=child.parent)

    child_sessions.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0055_install_indexes'),
    ]

    operations = [
        migrations.RunPython(remove_child_sessions)
    ]
