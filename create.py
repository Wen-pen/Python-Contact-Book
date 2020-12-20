import click
import main
from pascal import Contact

@click.group()
def cli():
    pass

@cli.command()
@click.argument("name")
@click.argument("email")
@click.argument("number")
def create(name, email, number):
    '''Adds contacts to contact book'''
    con = Contact(name, email, number)
    main.add(con)

@cli.command()
@click.argument("name")
def search(**kwargs):
    '''Searches for a contact and returns one based on contact name'''
    click.echo(main.search(kwargs['name']))

@cli.command()
def listContacts(**kwargs):
    '''Lists all the contacts, with name, email and phone number in a table'''
    main.listContacts()
if __name__ == '__main__':
    cli()