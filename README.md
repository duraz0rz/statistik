# STATISTIK

## Description

Review tracker for [beatmania IIDX](https://en.wikipedia.org/wiki/Beatmania_IIDX) chart difficulties. Supports traditional [ClickAgain-style reviews](http://clickagain.sakura.ne.jp/cgi-bin/sort11/data.cgi?level12=1) as well as Elo-based, [Textage-style reviews](http://textage.cc/banner/sortrank.html?3).

Deployed to my DO droplet at http://statistik.benhgreen.com.
Elo reviews can be found at http://statistik.benhgreen.com/elo?level=12.

## Setup

You can use Docker for the quick and easy setup. `run-app.sh` automatically runs all the migrations and populates the DB before starting the web service.

After following the setup, create some users via the `/register`
endpoint and you should be good to go.

Note that a user's `UserProfile` must be modified to 'enable' reviewing on their account.

To populate the song database, run the included `import_music_csv.py` and
`import_chart_csv.py` scripts from the root directory.

## Docker setup
* Install Docker from https://www.docker.com/community-edition
* If you're on Linux or OS X, this should be enough
* If you're on Windows and on Docker Edge, you have more steps to follow:
  * Install LCOW:  https://github.com/linuxkit/lcow
  * Switch Docker to use Linux containers
  * Add a .env file with the following setting: `COMPOSE_CONVERT_WINDOWS_PATHS=1`
  * Restart Docker

* Build the image for the app to run in: `docker-compose build`
  * You only need to do this if you modify any dependencies in `Pipfile`.

## Run the app
* `docker-compose up -d`

## Run unit tests
* Start the db: `docker-compose up -d db`
* Add the following values to your `.env` file:
  ```
  DJANGO_SETTINGS_MODULE=docker.settings
  DATABASE_URL=postgres://postgres:postgres@localhost:5432/postgres
  ```
* Run unit tests: `pipenv run python manage.py test`

## Bring down app and/or db
* `docker-compose down`

## Primary TODOs
- cleanup code (especially frontend)
- better navigation via links in page titles
- indexes for elo rankings
