def main():
    sentence = input("Enter a sentence: ")

    flip_sentence =''

    for ch in sentence:
    
        if ch.isalpha():
        
            if ch.islower():
            
                flip_sentence = flip_sentence + ch.upper()
            
            else:
                flip_sentence = flip_sentence + ch.lower()
            
        else:
            flip_sentence = flip_sentence + ch
        
    print("\nGiven Sentence: ",sentence)

    print("\nNew Sentence: ",flip_sentence)

main()
