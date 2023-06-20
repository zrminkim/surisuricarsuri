from django.shortcuts import render
import pandas as pd
from django.db.models import Avg
from carsuri.models import RepairCost

def estFunc(maker_num, model_num, detail_num, damage):
    
    # maker_num = 1;
    # model_num = 1;
    # detail_num = 55;
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