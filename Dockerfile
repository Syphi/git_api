FROM python:3.7

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /app

# # Run migrations
# RUN alembic -c /app/src/alembic.ini upgrade head
#
# # Run startup scripts
# RUN python3 -m src.src.scripts.upload_script
