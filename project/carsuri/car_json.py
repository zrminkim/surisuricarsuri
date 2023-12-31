from carsuri.estimate import repairFunc, exchangeFunc

def process_results(results, folder_name, maker_num, model_num, detail_num):
    class_mapping = {
        'Front_bumper_c': {'part': '앞 범퍼', 'repair': '교환'},
        'Front_bumper_s': {'part': '앞 범퍼', 'repair': '수리'},
        'Rear_bumper_c': {'part': '뒷 범퍼', 'repair': '교환'},
        'Rear_bumper_s': {'part': '뒷 범퍼', 'repair': '수리'},
        'Side_mirror_c': {'part': '사이드 미러', 'repair': '교환'},
        'Side_mirror_s': {'part': '사이드 미러', 'repair': '수리'},
        'Wheel_c': {'part': '휠', 'repair': '교환'},
        'Wheel_s': {'part': '휠', 'repair': '수리'},
    }

    processed_results = []

    for imgname, prediction in results.items():
        part_repair = class_mapping.get(prediction, {})
        part = part_repair.get('part', '')
        repair = part_repair.get('repair', '')

        if repair == '교환':
            cost = exchangeFunc(maker_num, model_num, detail_num, repair, part)
        else:
            cost = repairFunc(maker_num, model_num, detail_num, repair, part)

        print(repair,'1111111111')
        print(part_repair,'222222222222')
        print(prediction,'333333333333')

        processed_results.append({
            'folder_name' : folder_name,
            'imgname': imgname, 
            'part': part,
            'repair': repair,
            'cost': cost
        })

    return processed_results