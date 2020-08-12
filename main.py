import datetime
import requests
import utils

QUIT = 'q'


def press_enter_to_continue():
    input("\nPress Enter to continue...")


def print_posts(posts):
    if not posts:
        print('No posts!')
    else:
        for post in posts:
            print('\n')
            print(f'Title: {post["title"]}')
            print(f'Link: {post["link"]}')
            print(f'Date: {post["date"]}')


def is_date_correct(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def get_news_by_date():
    while True:
        utils.cls()
        print("Enter date in the following format: YYYY-MM-DD \n"
              "(q - for quiet or cancel)")
        date = input("->")
        if date == QUIT:
            return
        else:
            if is_date_correct(date):
                posts = requests.get(
                    f'http://0.0.0.0:8023/news/?date={date}').json()
                print_posts(posts)
                return
            else:
                print('Incorrect date format, should be YYYY-MM-DD')
                press_enter_to_continue()


def main_menu():
    while True:
        utils.cls()
        print('-------------------------------------')
        print("Choose action\n"
              "    1 Get all news\n"
              "    2 Get news by date")
        choice = input("->")
        if choice.isdigit() and int(choice) == 1:
            print_posts(requests.get('http://0.0.0.0:8023/news').json())
            press_enter_to_continue()
        elif choice.isdigit() and int(choice) == 2:
            get_news_by_date()
            press_enter_to_continue()
        elif choice == QUIT:
            raise SystemExit


if __name__ == '__main__':
    main_menu()
