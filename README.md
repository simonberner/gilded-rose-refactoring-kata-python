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
complexity) of existing code by **changing its internal behaviour** while preserving its functionality.
By continuously improving the design of code, we make it easier and easier to work with it.

## Gilded Rose Requirements Specification

The specification of the Gilded Rose shop
is [here](https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/main/GildedRoseRequirements.md).

## Tasks

1. From the start position (main branch), create a new branch
2. Study the (vague) requirements and think about how you could cover them in the current code with tests.
3. Fix the existing Test and add some new ones which reflect the current (external) behavior (spec) of the production code
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

### Steps for ApprovalTests

1. `pip install -U approvaltests` (
   see [here](https://github.com/approvals/ApprovalTests.Python?tab=readme-ov-file#adding-to-existing-projects))
2. `pip install -U pytest-approvaltests`
   see [here](https://github.com/approvals/ApprovalTests.Python?tab=readme-ov-file#example-using-pytest)
3. `pytest --approvaltests-use-reporter='PythonNative'`
   see [here](https://github.com/approvals/ApprovalTests.Python.PytestPlugin?tab=readme-ov-file#usage) -> (other diff tools: FileMerge, DiffMerge)

## Learnings

### Code smells

- The current design of the code is not composable at all. The existing code is a tangled mess of business
  rules.
- The item has its members accessed all over the place. This means the code actually belongs into the Item class.

### Test coverage

- We would need to write a lot of test combinations
- to cover all the possible business rules -> Could we cover them
  by using [ApprovalTest](https://github.com/approvals/ApprovalTests.Python?
- How about picking out just the most relevant combinations and cover them with UnitTests?
    - It would take quite some time to figure these out
- It is very hard to write composable tests if your software design is not composable.

### Code reading techniques

- Slow scroll
- Code folding

### Writing Tests

- Test Desiderata is a fundamental collection of valuable properties, which
  help us to optimize the value of automated tests.
- [Programmer tests are an oracle providing feedback coding-decision-by-coding-decision.](https://medium.com/@kentbeck_7670/programmer-test-principles-d01c064d7934)
- If the code is not composable, its best to give up on writing normal Unit Tests with the composable Test
  Desiderata in mind. Instead use Approval Test with combination approval. You will get a lot of coverage with very
  little Test code.
- When writing composable Tests, we can test one aspect (of the underlying code) at a time and don't need to write a
  test for every single combination.

### Nice to know

- [Here](https://github.com/d215steinberg/GildedRose-Java/blob/startPoint/Table%20of%20Contents.md) is a very
  comprehensive possible solution in Java

### Composable code

When we say "code has to be composable," we mean that the code should be designed in a way that allows different parts
of it to be combined and reused easily in various configurations. Composability is a key principle in software design
that enables modularity and flexibility. Here are some aspects of composable code:

1. **Modularity**: The code is broken down into small, self-contained modules or components, each responsible for a
   specific functionality. These modules can be developed, tested, and maintained independently.

2. **Interoperability**: The components can interact with each other through well-defined interfaces or APIs. This
   ensures that modules can be plugged into different contexts without modification.

3. **Reusability**: Composable code is designed to be reused across different parts of the application or even across
   different projects. This reduces duplication and enhances consistency.

4. **Separation of Concerns**: Each module focuses on a single aspect of the functionality, adhering to the principle of
   separation of concerns. This makes the code easier to understand and manage.

5. **Flexibility**: Composable code can be easily adapted and extended. New functionality can be added by creating new
   modules or by composing existing ones in new ways.

6. **Decoupling**: Components are loosely coupled, meaning changes in one part of the system have minimal impact on
   others. This improves maintainability and reduces the risk of introducing bugs when making changes.

7. **Ease of Testing**: Each module can be tested in isolation, which simplifies the testing process and enhances test
   coverage.

8. **Scalability**: Composable code can be scaled more effectively, as components can be distributed across different
   systems or scaled independently based on demand.

In essence, composable code enhances the overall robustness, maintainability, and scalability of software systems by
promoting the use of modular, interoperable, and reusable components. This approach is particularly beneficial in modern
software development practices such as microservices architecture, functional programming, and object-oriented design.