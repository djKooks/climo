# -*- coding: utf-8 -*-


import click


@click.group()
def cli():
    pass


# test command
@cli.command()
def test():
    '''
    
    '''

