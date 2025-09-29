# LionInvestment

Django 기반 투자 펀드 관리 시스템입니다.

## 프로젝트 개요

LionInvestment는 투자 상품을 등록하고 관리할 수 있는 웹 애플리케이션입니다. Django 프레임워크를 사용하여 CRUD(Create, Read, Update, Delete) 기능을 제공합니다.

## 주요 기능

- **투자 상품 목록 조회**: 등록된 모든 투자 상품을 확인할 수 있습니다
- **투자 상품 등록**: 새로운 투자 상품을 데이터베이스에 추가할 수 있습니다
- **투자 상품 상세 조회**: 개별 투자 상품의 상세 정보를 확인할 수 있습니다
- **투자 상품 수정**: 기존 투자 상품 정보를 업데이트할 수 있습니다
- **투자 상품 삭제**: 불필요한 투자 상품을 삭제할 수 있습니다

## 기술 스택

- **Framework**: Django
- **Database**: SQLite3
- **Language**: Python

## 프로젝트 구조

```
LionInvestment/
├── config/              # Django 프로젝트 설정
│   ├── settings.py      # 프로젝트 설정 파일
│   ├── urls.py          # 메인 URL 라우팅
│   ├── wsgi.py          # WSGI 설정
│   └── asgi.py          # ASGI 설정
├── fund/                # 펀드 관리 앱
│   ├── models.py        # Item 모델 정의
│   ├── views.py         # 뷰 함수들
│   ├── urls.py          # URL 라우팅
│   ├── forms.py         # ModelForm 정의
│   ├── admin.py         # Admin 설정
│   ├── templates/       # HTML 템플릿
│   └── migrations/      # 데이터베이스 마이그레이션
├── db.sqlite3           # SQLite 데이터베이스
└── manage.py            # Django 관리 명령어 도구
```

## 데이터 모델

### Item 모델
- `name`: 투자 상품명 (CharField, max_length=100)
- `description`: 상품 설명 (TextField)
- `create_at`: 생성일시 (TimeField, auto_now=True)

## 설치 및 실행

### 1. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. Django 설치
```bash
pip install django
```

### 3. 데이터베이스 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 개발 서버 실행
```bash
python manage.py runserver
```

서버가 실행되면 브라우저에서 `http://127.0.0.1:8000/` 으로 접속할 수 있습니다.

## URL 구조

- `/`: 메인 페이지
- `/fund/list/`: 투자 상품 목록
- `/fund/create/`: 투자 상품 등록
- `/fund/<int:pk>/`: 투자 상품 상세 조회
- `/fund/<int:pk>/update/`: 투자 상품 수정
- `/fund/<int:pk>/delete/`: 투자 상품 삭제

## 관리자 페이지

Django Admin을 통해 데이터를 관리할 수 있습니다.

### 관리자 계정 생성
```bash
python manage.py createsuperuser
```

관리자 페이지는 `http://127.0.0.1:8000/admin/` 에서 접속 가능합니다.

## 개발 환경

- Python 3.x
- Django (최신 버전 권장)

## 라이선스

이 프로젝트는 교육 목적으로 개발되었습니다.
