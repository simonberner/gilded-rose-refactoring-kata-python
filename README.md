# Gilded Rose Refactoring Kata in Python

- Taken from [here](https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main/python)
- We use [pytest](https://docs.pytest.org)

## What is the Gilded Rose?

The [Gilded Rose](https://wowpedia.fandom.com/wiki/Gilded_Rose) is an [Inn](https://wowpedia.fandom.com/wiki/Inn) in the
Game [World of Warcraft](https://en.wikipedia.org/wiki/World_of_Warcraft).
It is basically a shop where one can buy items, food, and drinks.

## Purpose of the Kata

The idea of the exercise is to do some deliberate practice of designing tests and refactoring.
The idea is not to re-write the code from scratch, but rather to practice taking small steps,
running the tests often, and incrementally improving the design.

You will see that without any Tests in place, you will be lost while refactoring.

## What is Code Refactoring?

Refactoring is a development and testing activity to improve the design (readability, maintainability, reducing
complexity) of existing code while preserving its functionality.
By continuously improving the design of code, we make it easier and easier to work with it.

## Gilded Rose Requirements Specification

The specification of the Gilded Rose shop
is [here](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.md).

## Tasks

1. From the start position (main branch), create a new branch
2. Fix the existing Test and add some new ones which reflect the current behavior (spec) of the production code 
3. Tidy the code first in order to make it more readable (to you)
4. Refactor the "production" code (gilded_rose.py) to improve its design (readability, maintainability)
5. Update the "system" with the new feature: "Conjured" items degrade in Quality twice as fast as normal items 
6. Reflect on the exercise and document your learnings in this README

## Do's and Don'ts

- Do not re-write the production code from scratch
- Write Unit Tests

## Tips

- While refactoring try to take small steps, don't rush ahead and run your Tests after each change

## History of the Kata

See [here](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/README.md#history-of-the-exercise) for
infos about from where this exercise originates.