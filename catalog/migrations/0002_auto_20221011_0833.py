# Generated by Django 3.2.16 on 2022-10-11 08:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placed_at', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('p', 'pendind'), ('c', 'completed'), ('f', 'failed')], default='p', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(null=True)),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('inventory', models.PositiveSmallIntegerField(null=True)),
                ('lastupdated', models.DateTimeField(auto_now_add=True)),
                ('collect', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.collection')),
            ],
        ),
        migrations.CreateModel(
            name='promotions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(null=True)),
                ('discoun', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='MyModelName',
        ),
        migrations.AddField(
            model_name='product',
            name='promotions',
            field=models.ManyToManyField(to='catalog.promotions'),
        ),
    ]