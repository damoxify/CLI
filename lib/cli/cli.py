import click
from models import User, Post, Comment
from database import Session

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
@click.argument('content')
@click.option('--user', type=click.INT, help='User ID to associate with the comment')
def add_comment(content, user):
    session = Session()
    comment = Comment(content=content, user_id=user)
    session.add(comment)
    session.commit()
    session.close()
    print(f'Comment "{content}" added.')

@cli.command()
def list_users_and_posts():
    session = Session()
    users = session.query(User).all()
    for user in users:
        print(f'User ID: {user.id}, Name: {user.name}')
        for post in user.posts:
            print(f'- Post ID: {post.id}, Title: {post.title}')
    session.close()


# ALGORITHMS USED
class Node:
    def __init__(self, user):
        self.user = user
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, user):
        new_node = Node(user)
        new_node.next = self.head
        self.head = new_node

    def sort_by_name(self):
        if self.head is None:
            return 
        current = self.head
        while current:
            min_node = current
            runner = current
            while runner:
                if runner.user.name < min_node.user.name:
                    min_node = runner
                runner = runner.next

            temp = min_node.user
            min_node.user = current.user
            current.user = temp

            current = current.next
class Node:
    def __init__(self, user):
        self.user = user
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, user):
        new_node = Node(user)
        new_node.next = self.head
        self.head = new_node

    def sort_by_name(self):
        if self.head is None:
            return

        current = self.head
        while current:
            min_node = current
            runner = current
            while runner:
                if runner.user.name < min_node.user.name:
                    min_node = runner
                runner = runner.next

            temp = min_node.user
            min_node.user = current.user
            current.user = temp

            current = current.next

@cli.command()
def sort_users():
    session = Session()
    users = session.query(User).all()
    session.close()

    linked_list = LinkedList()
    for user in users:
        linked_list.insert(user)

    linked_list.sort_by_name()

    print('Users sorted by name:')
    current = linked_list.head
    while current:
        print(f'ID: {current.user.id}, Name: {current.user.name}')
        current = current.next



