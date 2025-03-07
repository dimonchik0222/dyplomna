import requests
from config import API_KEY, BASE_URL

def get_ads_for_state(state_id, pages):
    """
    Отримує список оголошень для заданого state_id.
    """
    result = []
    for page in range(pages):
        url = f"{BASE_URL}/search?api_key={API_KEY}&state_id={state_id}&operation_type=1&page={page}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            result.extend(data.get("items", []))
        except Exception as e:
            print(f"Помилка при отриманні даних для state_id={state_id}: {e}")
            return []
    return result

def get_ad_info(ad_id):
    """
    Отримує детальну інформацію по оголошенню за його ID.
    """
    url = f"{BASE_URL}/info/{ad_id}?api_key={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Помилка при отриманні інформації для ad_id={ad_id}: {e}")
        return {}
