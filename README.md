# STATISTIK

##Description

Review tracker for beatmania IIDX chart difficulties. Supports traditional
[ClickAgain-style reviews](http://clickagain.sakura.ne.jp/cgi-bin/sort11/data.cgi?level12=1) as well as Elo-based, [Textage-style reviews](http://textage.cc/banner/sortrank.html?3).


## Setup
Uses Python 3.5, Django 1.8, Postgres, as well as whatever else is in `requirements.txt`.
(Postgres is absolutely required unless you modify certain models to not use ArrayFields.)

Install everything, setup database/migrations, create some users via the `/register`
endpoint and you should be good to go.

Note that a user's `UserProfile` must be modified to 'enable' reviewing on their account.

To populate the song database, run the included `import_music_csv.py` and
`import_chart_csv.py` scripts from the root directory.

## Primary TODOs
- cleanup code (especially frontend)
- better navigation via links in page titles
- indexes for elo rankings