# Pokémon Name Finder

## Overview
The Pokémon Name Finder allows users to input a sequence of characters, and it identifies all Pokémon names that contain those characters, regardless of their order. This program is useful for searching Pokémon names when you're not sure of the exact spelling or want to find all names that share certain letters.

## How It Works
The program normalizes the user's input by removing specific delimiters and spaces. It then checks each Pokémon name to ensure it contains the required characters in any order but with the correct frequency.

## Features
- **Input Normalization**: Removes undesired characters and standardizes input for processing.
- **Character Frequency Matching**: Uses character counting to ensure all required characters are present in each Pokémon name.
- **Flexible Searching**: Allows for partial and scrambled inputs to be used in searching Pokémon names.

## Usage
1. Run the program.
2. Enter a sequence of characters representing the scrambled or partial name of a Pokémon.
3. The program will display all matching Pokémon names, if any.

## Example
- Input: `_o_edg_`
- Output: Finds and lists Pokémon names that contain 'o', 'e', 'd', and 'g' in any order.

## Code Details
The program utilizes the `collections.Counter` to count character occurrences and compares these counts between the input and each Pokémon name in the database.

This program is designed to be user-friendly and robust, accommodating various user input forms to help Pokémon enthusiasts and gamers find Pokémon names efficiently.

(I didn't write the README, im not that fancy)
