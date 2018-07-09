#!/usr/bin/env python
import click
import requests
import json
import random
import time
import console

lives = 4
correct = 0

def doQuiz():
    global lives
    global correct
    r = requests.get('https://opentdb.com/api.php?amount=1&difficulty=easy&&category=27')
    json = r.json()['results'][0]

    click.echo(click.style('Lives: ', bold=True), nl=False)
    click.echo(str(lives), nl=False)
    click.echo(click.style(' Correct answers: ', bold=True), nl=False)
    click.echo(str(correct), nl=True)
    click.echo('')
    click.echo(click.style(json['question'], bold=True))

    options = json['incorrect_answers'];
    options.append(json['correct_answer'])
    random.shuffle(options)

    click.echo('')
    for idx,option in enumerate(options):
        click.echo('[' + str(idx+1) + ']' + option)
    click.echo('')
    choice = click.prompt('Whats your answer ?', type = int)

    if (options.index(json['correct_answer']) + 1) == choice:
        click.echo('correct')
        correct = correct + 1
    else:
        click.echo('Incorrect you loose a life')
        lives = lives - 1

def run(step):
    while lives > 0 and correct < 3:
        click.clear()
        click.echo(click.style(step.title, bold=True))
        click.echo(step.text)
        doQuiz()

    if correct == 3:
        console.doStep(step.choices[0]['link'])
    else:
        console.doStep(step.choices[1]['link'])

if __name__ == '__main__':
    run()
