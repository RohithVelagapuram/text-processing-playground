# Text Processing Playground

A small collection of lightweight Python utilities for analyzing and working with plain text files.

## Purpose

Built as a learning project to practice file handling, basic data analysis, and writing clean, functional Python scripts.

## Current Tools

### text_stats.py

Analyzes a text file and provides:

* Total word count
* Sentence count
* Most frequent words

### keyword_filter.py

Searches a text file and displays only the lines containing a specified keyword.
Useful for quickly locating relevant information in large text files.

## Example Usage

Run the script and provide a file path:

```
python text_stats.py sample.txt
```

Then enter:

```
python keyword_filter.py sample.txt software
```

## Tech Used

* Python (standard library only)
* File I/O
* Basic data structures (`collections.Counter`)

## Scope

This repository focuses on small, practical utilities rather than large frameworks.
