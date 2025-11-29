# `wc` Coding Challenges

This repo is created as a part of the [codingchallenges.fyi](https://codingchallenges.fyi/challenges/intro) challenges.
This repo specifically tackle the [challenge](https://codingchallenges.fyi/challenges/challenge-wc) of replicate the CLI command [`wc`](https://linux.die.net/man/1/wc).

## The Challenge

Replicate these functionality from the Unix command line tool [`wc`](https://linux.die.net/man/1/wc):
```bash
  -c, --bytes
      print the byte counts 
  -l, --lines
      print the newline counts 
  -w, --words
      print the word counts 
  -m, --chars
      print the character counts 
```


As part of the challenge we will be using the provided [test text file](./test.txt).

## Development

To setup this project you will have to have [uv](https://github.com/astral-sh/uv) installed.

To run the commands it is simply running:
```bash
uv run main.py -h
```

To run the testing suite you will call:
```bash
uv run pytest -s -v
```

To run the linter you will call:
```bash
uv run ruff check --fix .
```
