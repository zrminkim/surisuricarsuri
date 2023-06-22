from django.shortcuts import render
import pandas as pd
from django.db.models import Avg
from carsuri.models import RepairCost, ExchangeCost
import math

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

def repairFunc(maker_num, model_num, detail_num, damage, part):
    maker_num = maker_num;
    model_num = model_num;
    detail_num = detail_num;
    damage = damage
    part=part

    part=convert_part_name(part)
    print(part)
    data = RepairCost.objects.filter(maker_num=maker_num, model_num=model_num, detail_num=detail_num)
    
    # Django 모델 인스턴스를 리스트로 변환
    data = [(repair_cost.cost, repair_cost.repair) for repair_cost in data]
    
    # Pandas DataFrame 생성
    df = pd.DataFrame(data, columns=['cost','repair'])
    filtered_df = df[df['repair'].str.contains(part)]
    
    if filtered_df.empty:
        data = RepairCost.objects.filter(maker_num=maker_num, model_num=model_num)
        data = [(repair_cost.cost, repair_cost.repair) for repair_cost in data]
    
        # Pandas DataFrame 생성
        df = pd.DataFrame(data, columns=['cost','repair'])
        filtered_df = df[df['repair'].str.contains(part)]
        if filtered_df.empty:
            cost = 0
        else : 
            cost = filtered_df['cost'].mean()
    else : 
        cost = filtered_df['cost'].mean()
    cost = math.ceil(cost / 1000) * 1000
    cost_formatted = "{:,}".format(cost)

    
    return cost_formatted



def exchangeFunc(maker_num, model_num, detail_num, damage, part):
    maker_num = maker_num;
    model_num = model_num;
    detail_num = detail_num;
    damage = damage
    part=part

    part=convert_part_name(part)
    print(part)
    data = ExchangeCost.objects.filter(maker_num=maker_num, model_num=model_num, detail_num=detail_num)
    
    # Django 모델 인스턴스를 리스트로 변환
    data = [(exchange_cost.cost, exchange_cost.exchange) for exchange_cost in data]
    
    # Pandas DataFrame 생성
    df = pd.DataFrame(data, columns=['cost','exchange'])
    filtered_df = df[df['exchange'].str.contains(part)]
    
    if filtered_df.empty:
        data = ExchangeCost.objects.filter(maker_num=maker_num, model_num=model_num)
        data = [(exchange_cost.cost, exchange_cost.repair) for exchange_cost in data]
    
        # Pandas DataFrame 생성
        df = pd.DataFrame(data, columns=['cost','exchange'])
        filtered_df = df[df['exchange'].str.contains(part)]
        if filtered_df.empty:
            cost = 0
        else : cost = filtered_df['cost'].mean()
    else : 
        cost = filtered_df['cost'].mean()
    
    cost = math.ceil(cost / 1000) * 1000
    cost_formatted = "{:,}".format(cost)
    
    return cost_formatted