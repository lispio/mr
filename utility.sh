#!/bin/bash

do_migrations () {
  echo enter venv
  source /opt/lispio/mr/mrSvr_venv/bin/activate
  echo runing migrations
  python3 utility/apply.py
  deactivate
  echo migratios finisched
}

do_migrations