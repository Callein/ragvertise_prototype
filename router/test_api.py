from pyexpat.errors import messages

import ollama
from fastapi import APIRouter, HTTPException, Depends

from model.test_model import GenerateTestRequest
from util.database import get_db
from sqlalchemy.orm import Session

test_api_router = APIRouter()

@test_api_router.get("/db_connection")
def test_db_connection(db: Session = Depends(get_db)):
    """
    DB 에 간단한 쿼리를 보내 DB 연결상태 확인
    :param db:
    :return:
    """
    try:
        db.execute("SELECT 1")  # 간단한 쿼리 실행
        return {"message": "Database connected successfully!"}
    except Exception as e:
        return {"error": str(e)}



@test_api_router.post("/generate")
async def generate_text(request: GenerateTestRequest):
    """
    모델을 사용한 텍스트 생성 테스트
    """
    try:
        messages = [
            {"role": "system", "content": request.system_prompt},
            {"role": "user", "content": request.user_prompt}
        ]
        response = ollama.chat(model="mistral", messages=messages)
        return {"response": response["message"]["content"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))