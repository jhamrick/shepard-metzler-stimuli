#!/bin/bash -e

export VENV=blender
export PYTHON=$(which python3)
export BLENDER_SITE_PACKAGES=/Applications/blender.app/Contents/Resources/2.75/python/lib/python3.4/site-packages
export VENV_SITE_PACKAGES=${WORKON_HOME}/${VENV}/lib/python3.4/site-packages

# create the virtualenvironment
echo "Creating '${VENV}' virtual environment"
mkvirtualenv -q ${VENV} -p $(which python3) --no-pip --no-setuptools

# replace site-packages with blender's site-packages
echo "Replacing '${VENV_SITE_PACKAGES}' with '${BLENDER_SITE_PACKAGES}'"
rm -r "${VENV_SITE_PACKAGES}"
ln -s "${BLENDER_SITE_PACKAGES}" "${VENV_SITE_PACKAGES}"

# activate the virtualenv
workon ${VENV}

# install setuptools
wget -q https://bootstrap.pypa.io/ez_setup.py -O - | python > /dev/null

# install pip
echo "Installing pip"
easy_install -q pip

# install requirements
echo "Installing requirements"
pip install -q -r requirements.txt
