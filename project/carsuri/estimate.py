from django.shortcuts import render
import pandas as pd
from django.db.models import Avg
from carsuri.models import RepairCost

def convert_part_name(part):
    if part == '사이드 미러':
        return 'Side mirror'
    elif part == '앞 범퍼':
        return 'Front bumper'
    elif part == '휠':
        return 'Wheel'
    elif part == '뒷 범퍼':
        return 'Rear bumper'
    else:
        return None

def estFunc(maker_num, model_num, detail_num, damage, part):
    
    # maker_num = 1;
    # model_num = 1;
    # detail_num = 55;

    # 예시 사용
    part = convert_part_name(part)
    print(part)

    damage = 'repair' # repair or exchange
    data = RepairCost.objects.filter(maker_num=maker_num, model_num=model_num, detail_num=detail_num)
    df = pd.DataFrame(list(data.values()))
    
    if damage == 'repair':
        cost = data.exclude(repair__isnull=True).aggregate(avg_cost=Avg('cost'))['avg_cost']
    elif damage == 'exchange':
        cost = data.exclude(exchange__isnull=False).aggregate(avg_cost=Avg('cost'))['avg_cost']
    
    if cost == None:
        data = RepairCost.objects.filter(maker_num=maker_num, model_num=model_num)
        if damage == 'repair':
            cost = data.exclude(repair__isnull=True).aggregate(avg_cost=Avg('cost'))['avg_cost']
        elif damage == 'exchange':
            cost = data.exclude(exchange__isnull=False).aggregate(avg_cost=Avg('cost'))['avg_cost']

    if cost == None:
        data = RepairCost.objects.filter(maker_num=maker_num)
        if damage == 'repair':
            cost = data.exclude(repair__isnull=True).aggregate(avg_cost=Avg('cost'))['avg_cost']
        elif damage == 'exchange':
            cost = data.exclude(exchange__isnull=False).aggregate(avg_cost=Avg('cost'))['avg_cost']
    
    return cost