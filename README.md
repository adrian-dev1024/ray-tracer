# Ray Tracer

In this project I am following the Book [The Ray Tracer Challenge](https://pragprog.com/titles/jbtracer/the-ray-tracer-challenge/). 

## Goal
Using this project as a hands-on way to gain more experience with Python.

Interested in using:
- class
- dataclass
- dunder methods
- inheritance (super/abc)

## Progress

I have made it mostly through chapter 8 **Shadows**.

The examples can be found in [putting-it-together](src/putting-it-together) folder and the outputs are in the [images](images) folder.

## Dev Setup

Install the dev requirements 
```bash
$  pip install -r dev-requirements.txt
```


Use tox to run [Cucumber](https://behave.readthedocs.io/en/latest/) tests
```bash
$ tox
```

and to lint code.

```bash
tox -e linting
```

