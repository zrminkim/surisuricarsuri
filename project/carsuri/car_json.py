from carsuri.estimate import estFunc

def process_results(results, folder_name, maker_num, model_num, detail_num):
    class_mapping = {
        'Front bumper_c': {'part': '앞 범퍼', 'exchange': '교환'},
        'Front bumper_s': {'part': '앞 범퍼', 'repair': '수리'},
        'Side mirror_c': {'part': '사이드 미러', 'exchange': '교환'},
        'Side mirror_s': {'part': '사이드 미러', 'repair': '수리'},
        'Wheel_c': {'part': '휠', 'exchange': '교환'},
        'Wheel_s': {'part': '휠', 'repair': '수리'},
        'Rear bumper_c': {'part': '뒷 범퍼', 'exchange': '교환'},
        'Rear bumper_s': {'part': '뒷 범퍼', 'repair': '수리'}
    }

    processed_results = []

    for imgname, prediction in results.items():
        part_repair = class_mapping.get(prediction, {})
        part = part_repair.get('part', '')
        repair = part_repair.get('repair', '')
        cost = estFunc(maker_num, model_num, detail_num, repair)


        processed_results.append({
            'folder_name' : folder_name,
            'imgname': imgname, 
            'part': part,
            'repair': repair,
            'cost': cost
        })

    return processed_results