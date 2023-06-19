def process_results(results, folder_name):
    class_mapping = {
        'Front_bumper_c': {'part': '범퍼', 'repair': '교환'},
        'Front bumper_s': {'part': '범퍼', 'repair': '수리'},
        'Side mirror_c': {'part': '사이드 미러', 'repair': '교환'},
        'Side mirror_s': {'part': '사이드 미러', 'repair': '수리'},
        'Wheel_c': {'part': '휠', 'repair': '교환'},
        'Wheel_s': {'part': '휠', 'repair': '수리'}
    }

    processed_results = []

    for imgname, prediction in results.items():
        part_repair = class_mapping.get(prediction, {})
        part = part_repair.get('part', '')
        repair = part_repair.get('repair', '')

        processed_results.append({
            'folder_name' : folder_name,
            'imgname': imgname, 
            'part': part,
            'repair': repair
        })

    return processed_results