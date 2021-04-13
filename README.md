# Guidelines for setting up and run the repository in local.

    # using https
    git clone https://github.com/RiyaOmar/audio_app.git

# Install `postgresql` and its dependencies locally.

    $ sudo apt update
    $ sudo apt install postgresql postgresql-contrib


# Create the database

    $ sudo su postgres
    $ psql

    postgres=# CREATE DATABASE audio
    WITH
    OWNER = admin
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;
    postgres=# \q
    exit


# create a virtual enviromment and activate your virtual environment using python 3.7.

    python3 -m venv venv
    source venv/bin/activate

Install the development requirements

    pip install -r requirements.txt

# Guidelines for the API:
 There are four API:
  'audios/update_audio/<audios_type>/<audio_id>/' [Update]
  'audios/delete_audio/<audio_type>/<audio_id>/' [Delete]
  'audios/get_audio/<audio_type>/<audio_id>/' [GET]
  'audios/get_audio/<audio_type>/' [GET]
  'audios/create_audio/<audio_type>/' [POST]
