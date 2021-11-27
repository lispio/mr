#!/bin/bash

#Script for create venv and install needed package 

create_db() {
  #create data base 'vis' if not exist
  psql -U postgres -tc "SELECT 1 FROM pg_database WHERE datname = 'mr'" | grep -q 1 || psql -U postgres -c "CREATE DATABASE mr OWNER it"
}

restore_form_dump_file()
{
  #restore data base from dump file
  psql mr < ~/mr/mr.sql
}

create_venv(){
    echo create venv
    python3 -m venv /opt/lispio/mr/mrSvr_venv
    echo done
}

install_py_package()
{
  echo insall requirements package
  source /opt/lispio/mr/mrSvr_venv/bin/activate
  pip install wheel
  pip install -r /opt/lispio/mr/requirements.txt
  deactivate
  echo done
}

do_migrations () {
  echo enter venv
  source /opt/lispio/mr/mrSvr_venv/bin/activate
  echo runing migrations
  python3 utility/apply.py
  deactivate
  echo migratios done
}

create_venv
install_py_package
#create_db