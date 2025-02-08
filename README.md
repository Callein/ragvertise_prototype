# RAGvertise Prototype

## 1️⃣ 프로젝트 개요
> 이 프로젝트는 FastAPI 기반으로 Ollama LLM (Mistral, OpenChat 3.5 등) 및 RAG 기반 검색을 활용한 광고사 추천 서비스의 프로토타입입니다.   
DB는 MariaDB를 사용하며, 벡터 검색을 위해 FAISS 또는 Qdrant를 활용할 수 있습니다.

## 2️⃣ 설치 및 초기 설정
### 📌 2.1 필수 요구사항
- Python 3.10 이상 (python --version 확인)  
- pip 및 가상환경 (venv)  
- MySQL 8.0 이상 (또는 MariaDB)  
- Ollama 설치  
- FastAPI & Uvicorn  

### 📌 2.2 프로젝트 클론 및 가상 환경 설정
```shell
# 프로젝트 클론
git clone https://github.com/Callein/ragvertise_prototype.git
cd ragvertise_prototype

# 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)

# 필수 패키지 설치
pip install -r requirements.txt
```

### 📌 2.3 .env 설정 (환경 변수)
> .env 의 구성요소는 아래와 같습니다. 원본 .env 필요시 문의주세요.
```text
DB_HOST=
DB_PORT=
DB_NAME=
DB_USERNAME=
DB_PASSWORD=

# FastAPI 서버 포트
API_PORT=
...
```

### 📌 2.4 Ollama 설치 및 모델 다운로드
```shell
# Ollama 설치 (Mac/Linux)
curl -fsSL https://ollama.com/install.sh | sh

# OpenChat 3.5 모델 다운로드
ollama pull openchat:3.5

# 또는 Mistral 7B 다운로드 (가벼운 모델)
ollama pull mistral
```

## 3️⃣ FastAPI 서버 실행
```shell
# 단순 실행
python main.py
# reload 필요시
uvicorn main:app --reload --port 9000
```
Port는 `9000` 입니다.


## 4️⃣ API 사용 방법
[📜 Swagger UI (Docs)](http://localhost:9000/docs)  
[📃 Redoc (Alternative Docs)](http://localhost:9000/redoc)

### 🔹 4.1 모델 테스트 API (POST /api/test/generate)
- Request
    ```json
    {
        "system_prompt": "persona: 너는 최고의 광고 카피를 만드는 AI야.\n instruction: 모든 답은 한국어로 해.",
        "user_prompt": "헬스케어 제품을 위한 창의적인 광고 문구를 추천해줘."
    }
    ```
    | 필드명         | 타입     | 필수 여부 | 설명               |
    |--------------|--------|---------|------------------|
    | `system_prompt` | `string` | ✅       | 모델의 역할이나 지침을 전달하는 필드 |
    | `user_prompt`   | `string` | ✅       | 실제 요청을 전달하는 필드   |
    

- Response
    ```json
    {
        "response": "1. \"체력을 강화하는 건강한 미래를 만들어라! 다양한 헬스케어 제품으로 건강하신 것처럼!\"\n\n2. \"오늘부터 건강함의 시작, 내일부터 행복한 자신과 함께하는 헬스케어 제품입니다.\"\n\n3. \"건강을 위해 가장 중요한 것은 자신의 삶! 내 삶, 내 체력, 나만의 헬스케어 제품으로 당신이 건강하시어라.\"\n\n4. \"건강함을 선택하세요. 지금부터 겸손한 시작, 건강한 미래를 만들어내세요!\"\n\n5. \"건강에서 삶의 뿌리를 발굴해보세요! 최고의 헬스케어 제품으로 건강하신 것처럼!\"\n\n6. \"행복을 위한 기원은 건강함! 건강한 체력, 건강한 마음, 건강한 삶을 위해 최고의 헬스케어 제품으로 선택해보세요.\"\n\n7. \"건강하신 것처럼 행복하시오! 혁신적인 헬스케어 제품과 함께한 당신의 건강한 삶, 건강한 미래를 만들어내세요.\"\n\n8. \"건강함을 선택하고, 행복을 누리시오! 최고의 헬스케어 제품과 함께하여 당신이 건강하시며 행복해지세요.\"\n\n9. \"건강한 체력으로 삶을 만나보세요! 최고의 헬스케어 제품과 함께, 당신의 건강한 미래를 만들어내세요.\"\n\n10. \"건강하신 것처럼 행복하시오! 최고의 헬스케어 제품과 함께, 당신의 건강한 미래를 만들어내세요.\""
    }
    ```


