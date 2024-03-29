# Generated by Django 2.2.2 on 2019-06-27 01:07

from django.db import migrations, models
import django.db.models.deletion
import portfolio.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_item', models.CharField(max_length=100)),
                ('order', models.PositiveSmallIntegerField(default=0, verbose_name='Menu item order')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('titles_before_name', models.CharField(blank=True, max_length=30)),
                ('titles_after_name', models.CharField(blank=True, max_length=30)),
                ('about_me', models.TextField()),
                ('default_email', models.EmailField(max_length=254)),
                ('default_website', models.URLField(blank=True, verbose_name='My website')),
                ('default_phone', models.CharField(blank=True, max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
                ('job_description', models.CharField(max_length=500)),
                ('start_date', models.DateField(verbose_name='Job start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Job end date')),
                ('website', models.URLField(blank=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('skill_category', models.CharField(max_length=100)),
                ('skill_level', models.PositiveSmallIntegerField(validators=[portfolio.validators.validate_skill_level])),
                ('website', models.URLField(blank=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Publication title')),
                ('description', models.CharField(max_length=500, verbose_name='Publication summary')),
                ('release_date', models.DateField(verbose_name='Publication date')),
                ('website', models.URLField(blank=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('project_description', models.CharField(max_length=500)),
                ('website', models.URLField(blank=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Portrait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('upload', models.ImageField(height_field='height', upload_to='portrait/', width_field='width')),
                ('height', models.PositiveIntegerField(blank=True, default='100', editable=False, null=True)),
                ('width', models.PositiveIntegerField(blank=True, default='100', editable=False, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('upload', models.ImageField(height_field='height', upload_to='gallery/%Y/', width_field='width')),
                ('height', models.PositiveIntegerField(blank=True, default='100', editable=False, null=True)),
                ('width', models.PositiveIntegerField(blank=True, default='100', editable=False, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=60)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=100)),
                ('institute_type', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('start_date', models.DateField(verbose_name='Education starting date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Education ending date')),
                ('website', models.URLField(blank=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_content', models.TextField()),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.Menu')),
            ],
        ),
    ]
