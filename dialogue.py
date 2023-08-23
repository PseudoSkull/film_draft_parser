import sys

file_name = "debbie.txt"

# pubyear = 2002
# show = "{{w|Beyblade (season 1)|Beyblade}}"
# episode_name = "Day of the Dragoon"
# episode_number = "2"

file = open(file_name, "r")

list = file.readlines()

listdump = open("listdump.txt", "r")
listdumpr = listdump.read()

if listdumpr == "":
    newlist = []
    print("Got here!")
else:
    newlist = listdumpr.split("          ")

listcount = -1
newlistcount = 0
minute = "0"
ten = "0"
hour = None

while 1:
    try:
        listcount += 1
        # print(listcount)
        # print(len(list))
        # print(newlist)
        if listcount > len(list):
            break
        try:
            item = list[listcount]
        except:
            break
        if item != "\n":
            newlistcount += 1
        if newlistcount <= len(newlist):
            continue
        if item != "\n":
            while 1:                # if timestamp.contains("m"):
                item = item.rstrip()
                print(f"total elements: {int((len(list)-1)/2)}\nlistcount: {listcount}\nnewlistcount: {newlistcount}\n")
                print(item)
                timestamp = input("Timestamp: ")
                character = input("Character: ")
                if character == "b":
                    newlist.pop()
                    newlistcount -= 1
                    listcount -= 2
                    item = list[listcount]
                    print("Went back one!\n\n")
                    # print(newlist)
                    continue
                elif character == "d":
                    newlist.append("")
                    newlistcount += 1
                    listcount += 2
                    item = list[listcount]
                    print(f"Skipped!\n\n")
                    # print(newlist)
                    continue
                elif character == "a":
                    addition = input("Add line at this position: ")
                    if addition == "":
                        print("\n\nNot adding.\n\n")
                    else:
                        list.insert(listcount, "\n")
                        list.insert(listcount, f"{addition}\n")
                        fileadd = open(file_name, "w+")
                        fileadd.write("".join(list))
                        fileadd.close()
                        print("\n\nAdded!\n\n")
                    item = list[listcount]
                    continue
                elif character == "c":
                    quotecharacter = input("Character for citation: ")
                    quote = input("Quote for citation: ")
                    word = input("Word: ")
                    citation = f"""
#* '''{pubyear}''', ''{show}'', "{episode_name}" (episode {episode_number}):
#*: {quotecharacter}: {quote}
"""
                    citation = citation.replace(word, f"'''{word}'''")
                    print(citation)
                elif character == "w-":
                    print(list[listcount-10])
                    print(list[listcount-8])
                    print(list[listcount-6])
                    print(list[listcount-4])
                    print(list[listcount-2])
                    continue
                elif character == "w+":
                    print(list[listcount+2])
                    print(list[listcount+4])
                    print(list[listcount+6])
                    print(list[listcount+8])
                    print(list[listcount+10])
                elif character == "sim":
                    sim = open("sim.txt", "w+")
                    sim.write("".join(newlist))
                    sim.close()
                    print("\n\nSimulated! See sim.txt for simulation of transcription so far.\n\n")
                elif character == "clear":
                    areyousure = input("Are you sure you want to clear? ")
                    if areyousure == "y":
                        print("Okay, clearing...\n\n")
                        listdumpw = open("listdump.txt", "w+")
                        listdumpw.write("")
                        print("Goodbye!")
                        sys.exit()
                    else:
                        print("Not clearing...\n\n")
                        continue
                elif character == "":
                    print("\nERROR: Please enter something here!\n")
                else:
                    break
            edit = input("Edit: ")
            if edit != "":
                if edit == "!":
                    edit = f"{item[:len(item)-1]}!"
                elif edit == ".":
                    edit = f"{item[:len(item)-1]}."
                elif edit == "?":
                    edit = f"{item[:len(item)-1]}?"
                elif edit == "...":
                    edit = f"{item[:len(item)-1]}..."
                elif edit == "3.":
                    edit = f"{item[:len(item)-2]}"
                elif edit == "3!":
                    edit = f"{item[:len(item)-3]}!"
                elif edit == "3?":
                    edit = f"{item[:len(item)-3]}?"
                elif ">" in edit:
                    item_to_change = edit[:edit.index(">")]
                    item_to_replace_with = edit[edit.index(">")+1:]
                    item = item.replace(item_to_change, item_to_replace_with)
                    edit = item
                item = edit
            if character == "s":
                item = f"{{{{ft/s|\n{{{{c|{item}}}}}\n}}}}\n\n----\n\n"
            elif character == "i":
                item = f"{{{{ft/i|\n{{{{c|{item}}}}}\n}}}}\n\n----\n\n"
            else:
                item = f"{{{{ft/d|\n{{{{ft|{character}|{item}}}}}\n}}}}\n\n----\n\n"
            if character != "s" and character != "i" and "–" in item:
                print("I GOT HERE!")
                item = item.replace("–", "—")
            item = timestamp + "\n\n" + item
            print("\n")
            print(item)
            newlist.append(item)
    except (IndexError, KeyboardInterrupt):
        print(f"\n\nI'M SORRY, YOU'LL HAVE TO TRY AGAIN.")
        listdumpw = open("listdump.txt", "w+")
        listdumpw.write("          ".join(newlist))
        sys.exit()

listdumpw = open("listdump.txt", "w+")
listdumpw.write("          ".join(newlist))
newlist = "".join(newlist)

file = open(file_name, "w+")
file.write(newlist)

print("Congratulations! You're done!")
