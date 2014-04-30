#!/usr/bin/env sh
export PYTHONPATH=$PYTHONPATH:/var/projects/linuxpoetry/code
/var/projects/linuxpoetry/env/bin/gunicorn -w 3 poetry.wsgi:application -b 0.0.0.0:80
