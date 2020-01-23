from flask import Blueprint, request, abort, jsonify

from ..models import GitInfo

search_page = Blueprint('search_page', __name__)
DEFAULT_PAGE = 1
ITEMS_PER_PAGE = 30


def marshal(git_info_instance: GitInfo) -> dict:
    """ Need to use inited of this serializer """
    return {
        "id": git_info_instance.id,
        "full_name": git_info_instance.full_name,
        "html_url": git_info_instance.html_url,
        "description": git_info_instance.description,
        "stargazers_count": git_info_instance.stargazers_count,
        "language": git_info_instance.language,
    }


def is_int(s):
    """ Check to convert in int """
    try:
        return int(s)
    except ValueError:
        abort(400, description=f"Page need to be represent as int")

def get_int_value(value):
    result = is_int(request.args.get(value, ITEMS_PER_PAGE))
    if result < 1:
        abort(400, description=f"{value} to be grater that 0.")
    return result

@search_page.route('/', methods=['GET'])
def show():
    # Sorting
    sort_field = GitInfo.stargazers_count
    sort_order = request.args.get("sort_order", "desc").lower()

    if sort_order not in ["asc", "desc"]:
        abort(400, description=f"Sort order need to be in ['asc', 'desc'], not {sort_order}")
    sort_condition = sort_field.desc() if sort_order == 'desc' else sort_field.asc()

    # Pagination
    page_number = get_int_value("page")
    page_limit = get_int_value("page_limit")

    result = GitInfo.query.order_by(sort_condition)\
        .paginate(page_number, page_limit, error_out=False)

    # Other method to do this with .offset(start).limit(limit)

    return jsonify({
        "count": result.total,
        "result": [marshal(item) for item in result.items]
    })
