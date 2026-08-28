# Mastermind

A command-line implementation of the Mastermind code-breaking game. The program reads a code and player mode from an input file, writes game feedback to an output file, and can either use guesses supplied by a human player or generate random guesses for the computer.

## Requirements

- Python 3
- A writable output file that already exists

## Usage

```text
python mastermind.py INPUT_FILE OUTPUT_FILE [CODE_LENGTH] [MAX_GUESSES] [COLOUR ...]
```

Arguments:

- `INPUT_FILE`: path to the input file.
- `OUTPUT_FILE`: path to an existing file that will be overwritten with the result.
- `CODE_LENGTH`: optional number of colours in the code. The default is `5`.
- `MAX_GUESSES`: optional maximum number of guesses. The default is `12`.
- `COLOUR ...`: optional list of valid colour names. The default colours are `red blue yellow green orange`.

For the example files in this repository, the code length is three:

```text
python mastermind.py inputexample1.txt outputexample1.txt 3
```

## Input File Format

The first line defines the secret code. The word `code` must be followed by exactly `CODE_LENGTH` valid colours.

The second line defines the player mode:

```text
code red blue yellow
player human
```

### Human mode

Add one guess per line after the player declaration:

```text
code red blue yellow
player human
red green blue
red red red
red blue yellow
```

Guesses with the wrong number of colours or an unknown colour are reported as ill-formed. Once the code is solved, any remaining input lines are ignored.

### Computer mode

Use the following player declaration and no guesses are required:

```text
code red blue yellow
player computer
```

The computer generates random guesses. These guesses are written to `computerGame.txt`.

## Feedback

Each valid guess produces colour pegs:

- `black`: correct colour in the correct position.
- `white`: correct colour in the wrong position.

Feedback is written in the output file in this format:

```text
Guess 1: black white
Guess 2: black
```

The game ends with either a win message or:

```text
You lost. Please try again.
```

## Exit Codes

The program prints an exit code and description when it finishes:

| Code | Meaning |
| ---: | --- |
| `0` | The program ran successfully. |
| `1` | Not enough program arguments were provided. |
| `2` | There was an issue with the input or output file. |
| `3` | Defined by the error table, but not currently returned by the program. |
| `4` | No or ill-formed code was provided. |
| `5` | No or ill-formed player was provided. |

For codes `4` and `5`, the error description is also written to the output file.

## Repository Examples

- `inputexample1.txt` through `inputexample8.txt` contain sample game inputs and validation cases.
- `outputexample1.txt` through `outputexample8.txt` show the corresponding expected output.
- `computerGame.txt` contains generated computer guesses after a computer-mode game.
