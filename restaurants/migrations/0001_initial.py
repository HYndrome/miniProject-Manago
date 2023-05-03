# Generated by Django 3.2.18 on 2023-05-03 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('views', models.PositiveIntegerField(default=0)),
                ('region', models.CharField(choices=[('서울', '서울'), ('부산', '부산'), ('대구', '대구'), ('인천', '인천'), ('광주', '광주'), ('대전', '대전'), ('울산', '울산'), ('세종', '세종'), ('경기도', '경기도'), ('강원도', '강원도'), ('충청북도', '충청북도'), ('충청남도', '충청남도'), ('전라북도', '전라북도'), ('전라남도', '전라남도'), ('경상북도', '경상북도'), ('경상남도', '경상남도'), ('제주도', '제주도')], max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(choices=[('족발,보쌈', '족발,보쌈'), ('찜,탕,찌개', '찜,탕,찌개'), ('돈까스,회,일식', '돈까스,회,일식'), ('피자', '피자'), ('고기,구이', '고기,구이'), ('야식', '야식'), ('양식', '양식'), ('치킨', '치킨'), ('중식', '중식'), ('아시안', '아시안'), ('백반,죽,국수', '백반,죽,국수'), ('도시락', '도시락'), ('분식', '분식'), ('카페,디저트', '카페,디저트'), ('패스트푸드', '패스트푸드'), ('기타', '기타')], max_length=20)),
                ('pricerange', models.CharField(blank=True, max_length=50, null=True)),
                ('parking', models.CharField(blank=True, max_length=50, null=True)),
                ('business_hours', models.CharField(blank=True, max_length=50, null=True)),
                ('time_lastorder', models.CharField(blank=True, max_length=50, null=True)),
                ('eatdeal', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('rate', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
