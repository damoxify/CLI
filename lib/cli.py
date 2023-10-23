import click
from cli import User, Post
from cli import Session
from algorithms import bubble_sort

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def add_user(name):
    session = Session()
    user = User(name=name)
    session.add(user)
    session.commit()
    session.close()
    print(f'User {name} added.')

@cli.command()
@click.argument('title')
@click.argument('user_id', type=int)
def add_post(title, user_id):
    session = Session()
    post = Post(title=title, user_id=user_id)
    session.add(post)
    session.commit()
    session.close()
    print(f'Post "{title}" added for user {user_id}.')



@cli.command()
def list_users_and_posts():
    session = Session()
    users = session.query(User).all()
    for user in users:
        print(f'User ID: {user.id}, Name: {user.name}')
        for post in user.posts:
            print(f'- Post ID: {post.id}, Title: {post.title}')
    session.close()



@cli.command()
@click.argument('numbers', nargs=-1, type=int)
def sort_numbers(numbers):
    bubble_sort(numbers)
    print(f'Sorted Numbers: {numbers}')