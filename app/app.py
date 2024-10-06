from typing import Annotated
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import httpx
from models import QnAnswers
from helper import get_score
import os

app = FastAPI(title='Analytics')
security = HTTPBearer()


@app.get('/', tags=['home'])
async def home():
    return "Welcome to Analytics service"




@app.get('/analytics/{qna_id}', tags=['analytics'], status_code=status.HTTP_200_OK)
async def analysis_on_qna(qna_id, credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]):

    async with httpx.AsyncClient() as client:
        r = await client.get(f'http://localhost:{os.environ.get("PORT_NO")}/get_qna/{qna_id}', headers={'Authorization': f'{credentials.scheme} {credentials.credentials}'})
        if r.status_code != status.HTTP_200_OK:
            raise HTTPException(status_code=r.status_code)

    res = r.json()
    ques = res.get('ques')
    ans = res.get('ans')    

    score = get_score(ques=ques, ans=ans)
    
    return {score: f"{score}"} 
    

    

@app.get('/help')
async def get_help(help: QnAnswers):
    pass
