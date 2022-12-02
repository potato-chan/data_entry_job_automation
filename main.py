from data_manager import DataManager

LIMIT = "50"
OTODOM_LINK = "otodom_pl"
GOOGLE_FORM_LINK = "google_form"

ads = DataManager(otodom_link=OTODOM_LINK, google_form_link=GOOGLE_FORM_LINK, limit=LIMIT)
ads.create_list_with_ads()
ads.send_all_ads_to_google_forms()
