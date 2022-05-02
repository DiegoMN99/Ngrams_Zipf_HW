# Ngrams_Zipf_HW
Assignment for "ML in Linguistics" course at Universidad de Costa Rica's Master's in Linguistics program

This code is intended to:
  1. Format internet-gathered text into a more-easily-manipulable text file through the "formatted_text_generator"
  2. Normalize the now-formatted text through NLTK's list of stopwords through "normalizer.py"
  3. After using another script (constantedelaleydezipf-B, provided by Dr. Antonio Leoni), "excel_data_analyzer" will use pandas to handle the csv files and provide a quick summary of the unigrams in common between two texts, unigrams unique to each text, and the percentage of similarity of the lists, all in a text file created at the end
