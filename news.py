from newsdb import get_most_popular_three_articles_of_all_time
from newsdb import get_most_popular_article_authors_of_all_time
from newsdb import get_day_on_which_more_than_1_percent_req_errors


def underlined(text):
    return "\033[4m%s\033[0m" % text


def header(text):
    return "\033[104m%s\033[49m" % text


def print_line(title, data, format):
    print(underlined("\n%s :\n" % title))
    print("".join(format % (35, title, views)
                  for title, views in data))


def show_report():
    print_line('Most popular three articles of all time',
               get_most_popular_three_articles_of_all_time(), "%-*s -- %s views\n")
    print_line('Most popular article authors of all time',
               get_most_popular_article_authors_of_all_time(), "%-*s -- %s views\n")
    print_line('Days on which more than 1% of requests lead to errors',
               get_day_on_which_more_than_1_percent_req_errors(), "%-*s -- %s errors\n")

if __name__ == '__main__':
    show_report()
