# Myesha Mahazabeen EMPLID: 24005884

language_data =     { 'French' : ('Le monde de la réalité a ses limites; le monde de l\'imagination est sans frontières '
                                    'L\’avenir est entre les mains de ceux qui explorent '
                                    'Le monde est un livre dont chaque pas nous ouvre une page une page '
                                    'Dans la vie on ne fait pas ce que l\’on veut mais on est responsable de ce que l\’on est '),
                  
                    'English' : ('This above all to thine own self be true '
                                    'Did my heart love till now? Forswear it, sight! For I never saw true beauty till this night '
                                    'Another page of this missing book called the happiest moment of life'),

                    'German' : ('Ein jeder kehr’ vor seiner Tür, und rein ist jedes Stadtquartier'
                                    'Zwei Dinge sind unendlich, das Universum und die menschliche Dummheit, '
                                    'aber bei dem Universum bin ich mir noch nicht ganz sicher'
                                    'Was mich nicht umbringt, macht mich stärker'),
                                }

def findLang(str):
    language_words = dict()
    language_count = dict()
    for lang in language_data:
        language_words[lang] = []
        for w in language_data[lang].split(' '):
            w = w.lower()
            s = ''
            for ch in  w:
                if ch not in [';', '\\', ',', '!', '?']:
                    s+=ch
            language_words[lang].append(s)
        language_count[lang] = 0
    
    for w in str.split(' '):
        for lang in language_data:
            for s in language_words[lang]:
                if s==w:
                    language_count[lang]+=1
                    break
    mx_num = 0
    mx_str = 'No language can be determined'
    for lang in language_count:
        if language_count[lang]>mx_num:
            mx_str = lang
            mx_num = language_count[lang]
    return mx_str

str = input("Enter a string: ")
language = findLang(str.lower())
print('predicted language: '+language)
