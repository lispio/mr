#!/bin/bash

#Script for create venv and install needed package fog sysconfig


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

create_venv
install_py_package