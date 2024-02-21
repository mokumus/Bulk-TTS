## Text-to-Speech Conversion from JSON Data

This Python script utilizes the Google Text-to-Speech (gTTS) module to convert text data extracted from a JSON file into speech files. The JSON file contains data in the format of word pairs, with one word in a source language and its corresponding translation in another language.

### Requirements

- Python 3.x
- `gtts` library
- `json` library

### Usage

1. Ensure you have installed the required libraries (`gtts`).
   
2. Prepare your JSON file with word pairs.

3. Update the file name in the script to point to your JSON file.

4. Run the script. It will generate speech files in the specified output directory, with each word having its own subdirectory containing the corresponding translations as speech files.

### Code Explanation

- The script first imports necessary modules for text-to-speech conversion (`gtts`) and handling JSON data (`json`).
  
- It defines functions to extract data from the JSON file and to save text-to-speech output.

- The `get_keys_json` function reads the JSON file, extracts words and their translations, and returns them.

- The `save_tts` function converts text to speech using `gTTS` and saves the output to a specified directory with a given file name and format.

- Finally, the script iterates over the words and their translations, converting each translation to speech and saving it in the respective word's directory within the specified output directory.

### Example

Assuming you have a JSON file named `eslestirme.json` with word pairs and translations, running the script will generate speech files for each translation, organized in directories corresponding to the words.

### Note

- You can modify the script to customize the language, output format, or directory structure as needed.