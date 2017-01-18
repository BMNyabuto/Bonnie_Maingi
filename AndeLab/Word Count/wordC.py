def words(Text_String):
	Text_StringList = Text_String.split()
	
	for i in Text_StringList:
		if i == '0':
			j = Text_StringList.index(i)
            Text_StringList.remove('0')
            Text_StringList.insert(j, 0)
                  
        elif i == '1':
            j = Text_StringList.index(i)
            Text_StringList.remove('1')
            Text_StringList.insert(j, 1)

        elif i == '2':
            j = Text_StringList.index(i)
            Text_StringList.remove('2')
            Text_StringList.insert(j, 2)

        elif i == '3':
            j = Text_StringList.index(i)
            Text_StringList.remove('3')
            Text_StringList.insert(j, 3)

        elif i == '4':
            j = Text_StringList.index(i)
            Text_StringList.remove('4')
            Text_StringList.insert(j, 4)

        elif i == '5':
            j = Text_StringList.index(i)
            Text_StringList.remove('5')
            Text_StringList.insert(j, 5)
        elif i == '6':
            j = Text_StringList.index(i)
            Text_StringList.remove('6')
            Text_StringList.insert(j, 6)

        elif i == '7':
            j = Text_StringList.index(i)
            Text_StringList.remove('7')
            Text_StringList.insert(j, 7)

        elif i == '8':
            j = Text_StringList.index(i)
            Text_StringList.remove('8')
            Text_StringList.insert(j, 8)

        elif i == '9':
            j = Text_StringList.index(i)
            Text_StringList.remove('9')
            Text_StringList.insert(j, 9)
                  
    Count_Word_Occurence = [Text_StringList.count(x) for x in Text_StringList]

    result = dict(zip(Text_StringList, Count_Word_Occurence))

    return result
