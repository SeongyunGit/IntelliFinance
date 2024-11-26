# Generated by Django 4.2.16 on 2024-11-26 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='companyList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(blank=True, max_length=6, null=True)),
                ('fin_co_no', models.CharField(blank=True, max_length=7, null=True)),
                ('kor_co_nm', models.CharField(blank=True, max_length=100, null=True)),
                ('dcls_chrg_man', models.TextField(blank=True, null=True)),
                ('homp_url', models.URLField(blank=True, null=True)),
                ('cal_tel', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='companyListOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(blank=True, max_length=6, null=True)),
                ('fin_co_no', models.CharField(blank=True, max_length=7, null=True)),
                ('area_cd', models.CharField(blank=True, max_length=2, null=True)),
                ('area_nm', models.CharField(blank=True, max_length=20, null=True)),
                ('exis_yn', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IntegrationProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField(blank=True, null=True)),
                ('fin_co_no', models.TextField(blank=True, null=True)),
                ('fin_prdt_cd', models.TextField(blank=True, null=True)),
                ('kor_co_nm', models.TextField(blank=True, null=True)),
                ('fin_prdt_nm', models.TextField(blank=True, null=True)),
                ('join_way', models.TextField(blank=True, null=True)),
                ('dcls_strt_day', models.TextField(blank=True, null=True)),
                ('dcls_end_day', models.TextField(blank=True, null=True)),
                ('fin_co_subm_day', models.TextField(blank=True, null=True)),
                ('mtrt_int', models.TextField(blank=True, null=True)),
                ('spcl_cnd', models.TextField(blank=True, null=True)),
                ('join_deny', models.TextField(blank=True, null=True)),
                ('join_member', models.TextField(blank=True, null=True)),
                ('etc_note', models.TextField(blank=True, null=True)),
                ('max_limit', models.TextField(blank=True, null=True)),
                ('loan_inci_expn', models.TextField(blank=True, null=True)),
                ('erly_rpay_fee', models.TextField(blank=True, null=True)),
                ('dly_rate', models.TextField(blank=True, null=True)),
                ('loan_lmt', models.TextField(blank=True, null=True)),
                ('type_a', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IntegrationProductOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.CharField(blank=True, max_length=6, null=True)),
                ('fin_co_no', models.CharField(blank=True, max_length=7, null=True)),
                ('fin_prdt_cd', models.CharField(blank=True, max_length=20, null=True)),
                ('intr_rate_type', models.CharField(blank=True, max_length=1, null=True)),
                ('intr_rate_type_nm', models.CharField(blank=True, max_length=10, null=True)),
                ('save_trm', models.CharField(blank=True, max_length=4, null=True)),
                ('intr_rate', models.FloatField(blank=True, null=True)),
                ('intr_rate2', models.FloatField(blank=True, null=True)),
                ('rsrv_type', models.CharField(blank=True, max_length=1, null=True)),
                ('rsrv_type_nm', models.CharField(blank=True, max_length=20, null=True)),
                ('rpay_type', models.CharField(blank=True, max_length=1, null=True)),
                ('rpay_type_nm', models.CharField(blank=True, max_length=50, null=True)),
                ('lend_rate_type', models.CharField(blank=True, max_length=1, null=True)),
                ('lend_rate_type_nm', models.CharField(blank=True, max_length=50, null=True)),
                ('lend_rate_min', models.FloatField(blank=True, null=True)),
                ('lend_rate_max', models.FloatField(blank=True, null=True)),
                ('lend_rate_avg', models.FloatField(blank=True, null=True)),
                ('mrtg_type', models.CharField(blank=True, max_length=2, null=True)),
                ('mrtg_type_nm', models.CharField(blank=True, max_length=50, null=True)),
                ('deposit_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='Open_API.integrationproduct')),
            ],
        ),
    ]
