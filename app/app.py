from typing import Annotated
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import httpx
from . models import QnAnswers
from . helper import get_score
import os
from dotenv import load_dotenv



app = FastAPI(title='Analytics')
security = HTTPBearer()

load_dotenv()


url = f"http://{os.environ.get('QNA_DNS')}" or f"http://localhost:{os.getenv('PORT_NO')}"



@app.get('/', tags=['home'])
async def home():
    return "Welcome to Analytics service"




@app.get('/analytics/{qna_id}', tags=['analytics'], status_code=status.HTTP_200_OK)
async def analysis_on_qna(qna_id, credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]):

    async with httpx.AsyncClient() as client:
        r = await client.get(f'{url}/get_qna/{qna_id}', headers={'Authorization': f'{credentials.scheme} {credentials.credentials}'})
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
