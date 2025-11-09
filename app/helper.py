import httpx
from typing import List, Dict


def get_score(ques: List[Dict], ans: List[List[Dict]]):
    """Get average score of the questionnaire
    
    Logic:
        Total no.of questions right / Total no.of questions
    """
    total_participants = len(ans)
    count = 0

    # print(ans[0][0].get('choice'))
    # getting the average score
    # total 
    for j in range(total_participants):        
        sum = 0
        for i in range(len(ques)):
            if ques[i].get('mcq'):
                if ques[i].get('correct') == ans[j][i].get('choice'):
                    print(ques[i].get('correct'), " ", ans[j][i].get('choice'))
                    sum+=1
                # else: 
                #     sum-=1
            else:
                # @TODO
                # if the answer is text, check using some AI model?
                # for now assuming it correct
                sum+=1
        if sum == len(ques):
            count+=1

    score = f'{count}/{len(ans)}'
    return score



def get_avg_score(questionnaire: List[Dict], answers: List[List[Dict]]):
    """Get average score of the questionnaire
    
    Logic:
        Total no.of questions right / Total no.of questions
    """

    correct_answers = list()
    for question in questionnaire:
        if question.get('mcq'):
            correct_answers.append(question.get('correct'))
        else:
            correct_answers.append(None)
    

    total_correct_ans = 0
    for answer in answers:
        for i in range(len(answer)):
            if correct_answers[i]:
                if answer[i].get('choice') == correct_answers[i]: total_correct_ans += 1

    total_questions = len(answers) * len(answers[0])
    
    return (total_correct_ans/total_questions)*100


if __name__ == "__main__":

    pass