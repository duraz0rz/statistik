#!/bin/bash -e

echo Waiting for DB to be available...
while ! nc -z db 5432 2>/dev/null
do
    let elapsed=elapsed+1
    if [ "$elapsed" -gt 90 ]
    then
        echo "TIMED OUT !"
        exit 1
    fi
    sleep 1;
done

pipenv run python manage.py migrate
SONG_COUNT=$(psql -wqt -h db -U postgres -c 'select count(*) from public.statistik_song;')
if [ $SONG_COUNT == 0 ]
then
    echo "Doing one time DB import"
    pipenv run python misc/import_music_csv.py
    pipenv run python misc/import_ddr_json.py
    pipenv run python misc/import_chart_csv.py
    pipenv run python misc/import_clickagain_ratings.py
fi

# Need to run this if Debug = True in docker/settings.py for Javascript to get to static folder
pipenv run python manage.py collectstatic --noinput --ignore *.scss
pipenv run python manage.py runserver 0.0.0.0:8000