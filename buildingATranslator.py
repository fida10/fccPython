def elephantTranslator(wordToTranslate):
    listOfVowels = ['a', 'e', 'i', 'o', 'u'];
    translation = "";
    for indivChar in wordToTranslate:
        if(indivChar.lower() in listOfVowels): # "in" works just like contains, only it works on lists too
            if(indivChar.isupper()):
                translation += 'H';  # append 'H' to translation string if vowel. Above and below if/else accounts for uppercase/lowercase letters
            else:
                translation += 'h';

        else:
            translation += indivChar; # append regular char to translation if not vowel
    return translation;


wordToTranslate = input("Enter the word you'd like translated: ");
print(elephantTranslator(wordToTranslate));


