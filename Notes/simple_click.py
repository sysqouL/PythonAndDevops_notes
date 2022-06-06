#-----------------------------------------------------------------------------------------------------------------------
""""""

"""
    Пример использования библиотеки Click
"""
"""
import click

@click.command()
@click.option("--firstname", default="Petya", help="Default name")
@click.option("--surname", default="Pupkin", help="Second name")
def test(firstname, surname):
   click.echo(f"{firstname} {surname}")

if __name__ == '__main__':
    test()

input()

"""
import click

@click.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    for _ in range(count):
        click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    hello()
