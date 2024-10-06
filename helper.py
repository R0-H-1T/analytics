import httpx
from typing import List, Dict


def get_score(ques: List[Dict], ans: List[List[Dict]]):
    total_participants = len(ans)
    count = 0

    # print(ans[0][0].get('choice'))
    for j in range(total_participants):        
        sum = 0
        for i in range(len(ques)):
            if ques[i].get('mcq'):
                if ques[i].get('correct') == ans[j][i].get('choice'):
                    print(ques[i].get('correct'), " ", ans[j][i].get('choice'))
                    sum+=1
                else: 
                    sum-=1
            else:
                # @TODO
                # if the answer is text, check using some AI model?
                # for now assuming it correct
                sum+=1
        if sum == len(ques):
            count+=1

    score = f'{count}/{len(ans)}'
    return score