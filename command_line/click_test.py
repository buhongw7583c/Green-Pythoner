'''
Using click for command line. More easier than argparse. 
'''
# Command
import click
@click.command()
@click.option("--count", default=1, help= "print times", type=int)
#@click.prompt("--name", prompt_suffix= "pleae input the name: ", type= str)
@click.option("--name", prompt= "please input your name ")
def click_hello(count, name):
    for i in range (count):
        click.echo(f'Hello {name}')

if __name__ == '__main__':
    click_hello()

'''
Use the command line to run the codebn
python click_test.py --count 4
'''

