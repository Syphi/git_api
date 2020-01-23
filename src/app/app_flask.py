from . import app
from ..view import *

app.register_blueprint(search_page)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5700)
