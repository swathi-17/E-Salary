# Generated by Django 4.0 on 2021-12-24 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
        ('salary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deduction',
            name='dedid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='deduction',
            name='eid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.employee'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='conveyance_allowance',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='salary',
            name='eid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.employee'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='hra',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='salary',
            name='medical_allowance',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='salary',
            name='others',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='salary',
            name='performance_bonus',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='salary',
            name='slipno',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]