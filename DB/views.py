from django.shortcuts import render
import pandas as pd
from django.db.models import Avg
from myapp.models import RepairCost
# Create your views here.

def mainFunc(request):
    
    maker_num = 1;
    model_num = 1;
    detail_num = 55;
    damage = 'repair' # repair or exchange
    data = RepairCost.objects.filter(maker_num=maker_num, model_num=model_num, detail_num=detail_num)
    df = pd.DataFrame(list(data.values()))
    print(df)
    if damage == 'repair':
        cost = data.exclude(repair__isnull=True).aggregate(avg_cost=Avg('cost'))['avg_cost']
    elif damage == 'exchange':
        cost = data.exclude(exchange__isnull=False).aggregate(avg_cost=Avg('cost'))['avg_cost']
    print('cost',cost)    
    
    if cost == None:
        data = RepairCost.objects.filter(maker_num=maker_num, model_num=model_num)
        if damage == 'repair':
            cost = data.exclude(repair__isnull=True).aggregate(avg_cost=Avg('cost'))['avg_cost']
        elif damage == 'exchange':
            cost = data.exclude(exchange__isnull=False).aggregate(avg_cost=Avg('cost'))['avg_cost']
    print('cost',cost)    

    if cost == None:
        data = RepairCost.objects.filter(maker_num=maker_num)
        if damage == 'repair':
            cost = data.exclude(repair__isnull=True).aggregate(avg_cost=Avg('cost'))['avg_cost']
        elif damage == 'exchange':
            cost = data.exclude(exchange__isnull=False).aggregate(avg_cost=Avg('cost'))['avg_cost']
    print('cost',cost)   
    
    return render(request, 'main.html')
 
'''
해당 차종은 수리정보 없음(둘다 없거나 repair가 없거나)
없는 경우 상위 그룹의 평균으로.
170 차종중 39종...
기아    카렌스    뉴카렌스(06)
기아    프라이드    뉴프라이드4DR(05)
기아    프라이드    뉴프라이드5DR(05)
기아    모닝    모닝
기아    쏘렌토    쏘렌토R
기아    쏘울    쏘울
기아    쏘울    쏘울(16)
기아    프라이드    프라이드(4Dr)
기아    프라이드    프라이드(5Dr)
기아    프라이드    프라이드5DR(15)
르노삼성    QM5    QM5
르노삼성    QM5    QM5(11)
르노삼성    SM3    SM3 (09)
르노삼성    SM3    SM3 (2.0)
르노삼성    SM5    SM5 (2.5)
르노삼성    SM5    SM5 TCE(13)
르노삼성    SM3    XM3(20)-LJL
르노삼성    SM3    뉴 SM3
르노삼성    SM5    뉴 SM5
쌍용    렉스턴    뉴렉스턴
쌍용    렉스턴    렉스턴
쌍용    체어맨    체어맨W
한국GM    아베오    아베오(세단)
한국GM    윈스톰    윈스톰맥스
현대    G70    GV70(20)-JK1
현대    i40    i40 살룬
현대    i40    i40 살룬(15)
현대    엑센트    뉴엑센트(4Dr)
현대    엑센트    뉴엑센트(5Dr)
현대    스타리아    스타리아 투어러(21)
현대    스타렉스    신형 스타렉스6밴
현대    스타렉스    신형 스타렉스점보
현대    싼타페    싼타페
현대    싼타페    싼타페(2012)
현대    아반떼    아반떼 하이브리드 LPi
현대    아이오닉    아이오닉5(21)-NE
현대    아반떼    올뉴아반떼
현대    코나    코나
현대    투싼    투싼(14)
'''