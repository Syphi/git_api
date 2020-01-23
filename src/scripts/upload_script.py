import requests

from sqlalchemy import inspect

from ..app import db
from ..models import *


def get_raw_data(lang: str = "python", stars_limit: int = 500):
    """ Load data from github api """
    session = requests.Session()
    page = 1
    while True:
        q = f"language:{lang}+stars:>{stars_limit}"
        params = {
            "sort": "stars",
            "order": "desc",
            "page": page
        }
        url = f"https://api.github.com/search/repositories?q={q}"

        response = session.get(url, params=params)
        data = response.json().get('items')
        if not data:
            break
        yield data
        page += 1


def upload_startup_data():
    """
    Load data to db
    Do commit ones in page
    """
    for page_info in get_raw_data():
        for repo_info in page_info:

            new_git_repo = GitInfo()
            inst_obj = inspect(GitInfo)

            for field_name in inst_obj.mapper.column_attrs:
                setattr(new_git_repo, field_name.key, repo_info.get(field_name.key))

            db.session.add(new_git_repo)
        db.session.commit()


if __name__ == '__main__':
    try:
        upload_startup_data()
    except Exception as err:
        print(err)