import os.path


FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


ALL_BREEDS_JSON = get_path(filename="all_breeds.json")
ALL_USERS_CVS = get_path(filename="users.csv")
PH_DATA = get_path(filename="ph_data.json")
PH_HEADERS = get_path(filename="ph_headers.json")