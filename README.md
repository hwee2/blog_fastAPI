[FastAPI Blog API]

(26. 6. 16)
       
- FastAPI를 사용하여 개발한 블로그 게시글 관리 RESTful API 서버
- SQLAlchemy ORM을 활용하여 데이터베이스 연동 및 블로그 CRUD 기능 구현



🛠️ 기술 스택 (Tech Stack)

- Framework: FastAPI
- Database ORM: SQLAlchemy
- Database: MySQL
- Data Validation: Pydantic
- Language: Python 3.14
  


📂 프로젝트 구조 (Project Structure)

```text
└── blog/                          
    ├── database/                  # 데이터베이스 관련 설정 폴더
    │   ├── db_connection.py       # 데이터베이스 연결 및 세션 관리
    │   └── orm.py                 # SQLAlchemy 기본 클래스(Base) 정의
    ├── scheme/                    
    │   ├── request.py             # API 요청(Request) 바디 스키마 정의
    │   └── response.py            # API 응답(Response) 바디 스키마 정의
    ├── .env                       # 환경 변수 관리 파일
    ├── .gitignore                
    ├── main.py                    # 애플리케이션 진입점 및 FastAPI 라우터 설정
    └── models.py                  # SQLAlchemy DB 테이블 모델 정의         
```
