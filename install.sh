#!/bin/bash

#Script for create venv and install needed package 

create_db() {
  #create data base 'vis' if not exist
  psql -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = 'fgr'" | grep -q 1 || psql -U postgres -c "CREATE DATABASE vis OWNER it"
}

restore_form_dump_file()
{
  #restore data base from dump file
  psql fgr < ~/fgr/fgr.sql
}

create_venv(){
    echo create venv
    python3 -m venv /opt/lispio/fgr/fgr_venv
    echo done
}

install_py_package()
{
  echo insall requirements package
  source /opt/lispio/fgr/fgr_venv/bin/activate
  pip install wheel
  pip install -r /opt/lispio/fgr/requirements.txt
  deactivate
  echo done
}

do_migrations () {
  echo enter venv
  source /opt/lispio/visSvr/visSvr_venv/bin/activate
  echo runing migrations
  python3 utility/apply.py
  deactivate
  echo migratios done
}

create_venv
install_py_package