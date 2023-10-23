from click.testing import CliRunner
from cli import cli

def test_add_user():
    runner = CliRunner()
    result = runner.invoke(cli, ['add_user', 'John'])
    assert result.exit_code == 0
    assert 'User John added.' in result.output

def test_add_post():
    runner = CliRunner()
    result = runner.invoke(cli, ['add_post', 'Sample Post', '1'])
    assert result.exit_code == 0
    assert 'Post "Sample Post" added for user 1.' in result.output


def test_list_users_and_posts():
       runner = CliRunner()
       result = runner.invoke(cli, ['list_users_and_posts'])
       assert result.exit_code == 0
       assert 'User ID: 1, Name: John' in result.output