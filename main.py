# main.py
from data_processing import process_ads, create_dataframe


def main():
    # Налаштування параметрів
    state_ids = range(1, 3)  # Наприклад, state_id від 1 до 2
    pages_per_state = 1
    num_random_ads = 10

    # Список колонок, які необхідно зберегти в DataFrame
    columns_to_keep = {
        "state_id", "price_total", "realty_type_id", "city_name_uk", "street_name_uk",
        "realty_type_name_uk", "secondaryUtp", "city_id", "photos", "realty_type_parent_id",
        "latitude", "longitude", "publishing_date_ts", "currency_type_id", "description_uk",
        "price_type", "district_id", "quality", "price", "priceArr", "priceItemArr", "ares_count",
        "currency_type", "realtorVerified", "characteristics_values", "floor", "realty_id",
        "state_name_uk", "agencyVerified", "is_commercial", "agency", "newbuildUtp", "wall_type",
        "total_square_meters", "rooms_count", "district_name_uk", "district_type_name", "newbuildId",
        "user_newbuild_name_uk", "newbuild", "building_number_for_map", "floors_count",
        "district_type_id", "living_square_meters", "kitchen_square_meters",
        "admin_district_name_uk", "admin_district_id"
    }

    # Отримання та обробка даних
    ad_info_list = process_ads(state_ids, pages_per_state, num_random_ads)
    if not ad_info_list:
        return

    df = create_dataframe(ad_info_list, columns_to_keep)
    print("Перші рядки DataFrame:")
    print(df.head())

    # Збереження даних у CSV
    df.to_csv('database.csv', index=False)


if __name__ == "__main__":
    main()
