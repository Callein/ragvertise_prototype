from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router.healthcheck import healthcheck_router
from constants.env_variables import EnvVariables
from dotenv import load_dotenv

from router.test_api import test_api_router

# .env 로드
load_dotenv()

# FastAPI 앱 생성
app = FastAPI()

# CORS 설정 (필요한 도메인만 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(healthcheck_router, prefix="/healthcheck")
app.include_router(test_api_router, prefix="/test")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(EnvVariables.API_PORT))