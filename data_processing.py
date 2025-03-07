import pandas as pd
import random
import time
from api_client import get_ads_for_state, get_ad_info
from mappings import characteristics_mapping

# Наприклад, перелік допустимих типів нерухомості
obligated_realty_type_ids = [2, 3, 5, 6, 9, 11, 18, 21]

def process_ads(state_ids, pages_per_state, num_random_ads):
    """
    Отримує оголошення для вказаних state_ids, вибирає випадкові оголошення
    та обробляє дані (застосовує мапінг характеристик).
    """
    all_ads = []
    for state_id in state_ids:
        ads = get_ads_for_state(state_id, pages_per_state)
        print(f"State {state_id}: знайдено {len(ads)} оголошень.")
        all_ads.extend(ads)
        time.sleep(0.5)
    print(f"Всього оголошень: {len(all_ads)}")

    if len(all_ads) < num_random_ads:
        print("Недостатньо оголошень для вибору випадкових.")
        return []

    random_ads = random.sample(all_ads, num_random_ads)
    print("Випадково вибрані ID оголошень:", random_ads)

    ad_info_list = []
    for ad in random_ads:
        info = get_ad_info(ad)
        if info.get('realty_type_id') in obligated_realty_type_ids:
            characteristics = dict(info.get('characteristics_values', {}))
            type_id = int(info.get('realty_type_id'))
            if type_id in characteristics_mapping:
                applicable_chars = characteristics_mapping[type_id]
                for characteristic, value in characteristics.items():
                    characteristic_int = int(characteristic)
                    if characteristic_int in applicable_chars:
                        name, mapping = applicable_chars[characteristic_int]
                        if int(value) in mapping:
                            info[name] = mapping[int(value)]
            ad_info_list.append(info)
        time.sleep(0.5)
    return ad_info_list

def create_dataframe(ad_info_list, columns_to_keep):
    """
    Створює pandas DataFrame з отриманих даних, залишаючи лише вказані колонки.
    """
    df = pd.DataFrame(ad_info_list)
    existing_columns = [col for col in columns_to_keep if col in df.columns]
    df = df[existing_columns]
    df = df[sorted(df.columns)]
    return df
