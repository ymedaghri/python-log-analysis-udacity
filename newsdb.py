import psycopg2
import datetime

DBNAME = "news"


def get_most_popular_three_articles_of_all_time():
    """Return the most popular three articles of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select a.title, count(*) from articles a inner join log l on l.path='/article/'||a.slug " +
              "group by a.title order by 2 desc limit 3")
    return c.fetchall()
    db.close()


def get_most_popular_article_authors_of_all_time():
    """Return the most popular three articles of all time."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select aut.name, count(*) from articles art inner join authors aut on art.author=aut.id " +
              " inner join log l on l.path='/article/'||art.slug group by aut.name order by 2 desc")
    return c.fetchall()
    db.close()


def get_day_on_which_more_than_1_percent_req_errors():
    """Return the days on which more than 1% of requests lead to errors."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select to_char(le.time, 'Month DD, YYYY'), trunc(le.requests*100.0/ls.requests,2) from log_errors le inner join log_success ls on ls.time=le.time where le.requests*100.0/ls.requests>=1")
    return c.fetchall()
    db.close()
