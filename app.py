from typing import Annotated
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import httpx
from models import QnAnswers


app = FastAPI(title='Analytics')
security = HTTPBearer()


@app.get('/', tags=['home'])
async def home():
    return "Welcome to Analytics service"




@app.get('/analytics/{qna_id}', tags=['analytics'])
async def analysis_on_qna(qna_id):
    async with httpx.AsyncClient() as client:
        r = await client.get(f'http://localhost:8081/test_get_qna/{qna_id}')
        if r.status_code != status.HTTP_200_OK:
            raise HTTPException(status_code=r.status_code)

    
    # @TODO
    # Handle None -  if no question, or answer
    
    res = r.json()
    qna = res.get('ques')
    answers = res.get('ans')

    print(answers)

    total_participants = len(answers)
    count = 0

    print(answers[0][0].get('choice'))
    for j in range(total_participants):        
        sum = 0
        for i in range(len(qna)):
            if qna[i].get('mcq'):
                if qna[i].get('correct') == answers[j][i].get('choice'):
                    print(qna[i].get('correct'), " ", answers[j][i].get('choice'))
                    sum+=1
                else: 
                    sum-=1
            else:
                # @TODO
                # if the answer is text, check using some AI model?
                # for now assuming it correct
                sum+=1
        if sum == len(qna):
            count+=1

    score = f'{count}/{len(answers)}'
    print(f'\n\n{score}')

    return score
    

    


@app.get('/anal')
async def test(qna: QnAnswers):
    pass