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

## What is Tidying?

Tidying :broom: is a development activity where we change the structure (not the behaviour!) of existing code to improve
its readability.

## What is Refactoring?

Refactoring :hammer: is a development and testing activity to improve the design (readability, maintainability, reducing
complexity) of existing code by **changing its behaviour** while preserving its functionality.
By continuously improving the design of code, we make it easier and easier to work with it.

## Gilded Rose Requirements Specification

The specification of the Gilded Rose shop
is [here](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.md).

## Tasks

1. From the start position (main branch), create a new branch
2. Study the (vague) requirements and think about how you could cover them in the current code with tests.
3. Fix the existing Test and add some new ones which reflect the current behavior (spec) of the production code
4. Tidy (structure) the code in order to improve readability
5. Refactor (change the behaviour) of the production code to improve its design
6. Tidy (structure) more as needed
7. Add a test for the new feature "Conjured items"
8. Implement the new feature "Conjured items" (which degrade in Quality twice as fast as normal items)
9. Reflect on the exercise and document your learnings

## Do's and Don'ts

- Do not re-write the production code from scratch
- Write Unit Tests

## Tips

- As you go on, ask the following: are we tidying (changing the structure of) the code or are we refactoring (
  changing the behaviour of) the code?
- While tidying and refactoring try to take small steps, don't rush ahead and run your Tests after each change

## History of the Kata

See [here](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/README.md#history-of-the-exercise) for
infos about from where this exercise originates.

## Credits and resources

- [Why Developers LOVE The Gilded Rose Kata](https://www.youtube.com/watch?v=Mt4XpGxigT4)
- [Fun Refactoring! - Gilded Rose Kata, Hands-on with Approval Testing](https://www.youtube.com/watch?v=OdnV8hc9L7I&t)
- [Best Tests for Gilded Rose Kata | Kent Beck’s Desiderata](https://www.youtube.com/watch?v=vMww6pV6P7s)
- [The Test Desiderata Map](https://kentbeck.github.io/TestDesiderata/)

## Python hints

### pytest

Install/Upgrade the following things as dependencies in the projects .venv (virtual environment):

- `pip install -U pytest` (see [here](https://docs.pytest.org/en/8.2.x/getting-started.html#install-pytest))
- `pip install -U pytest-watch` (see [here](https://pypi.org/project/pytest-watch/))