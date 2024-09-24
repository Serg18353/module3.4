def single_root_words(root_woordd, *other_woords):
    root_woord_l = root_woordd.lower()
    same_words = []
    for i in other_woords:
        other_woords_l = i.lower()
        if root_woord_l in other_woords_l or other_woords_l in root_woord_l:
            same_words.append(i)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)
