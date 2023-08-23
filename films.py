#This is gonna be worse'n a sure 'nuff funeral.
pageq = input("Page name: ")
if pageq == "":
    print("You nincompoop! Don't type nothing!")
    exit()
import time
import re
import random
print("Importing pywikibot...")
import pywikibot
print("Imported!")

print("Processing data...")

# Remove item from requests list (see below)

sections = ["Uploaded to Commons", "Not uploaded to Commons", "Lost film"]

def requestremove(film, year):
    find_more_lines = False
    edit_summary = f"Removing [[{film}]] from request lists, as it is already done..."
    print(edit_summary)
    for section in sections:
        pagename = f"Wikisource:WikiProject Film/{section}/{year}"
        site = pywikibot.Site()
        page = pywikibot.Page(site, pagename)
        if page.text != "":
            pageparse = page.text.split("\n")
            new_pageparse = pageparse.copy()
            print(f"Checking {pagename}")
        else:
            continue
        for line in pageparse:
            if line.startswith(f"* [[{film}|") or line.startswith(f"* [[{film}]]"):
                new_pageparse.remove(line)
                find_more_lines = True
            elif find_more_lines == True:
                if line.startswith("* ") or line.startswith("==") or line == "":
                    find_more_lines = False
                    page.text = "\n".join(new_pageparse)
                    page.save(f"{edit_summary}")
                    break
                else:
                    new_pageparse.remove(line)

# Pick a random film

list_to_shuffle = []

def filmpick(section):
    for i in range(100):
        if len(str(i)) == 1:
            pagename = f"Wikisource:WikiProject Film/{section}/190{i}"
        else:
            pagename = f"Wikisource:WikiProject Film/{section}/19{i}"
        # print(pagename)
        site = pywikibot.Site()
        page = pywikibot.Page(site, pagename)
        if page.text != "":
            pageparse = page.text.split("\n")
            print(f"Checking {pagename}")
        else:
            continue
        for line in pageparse:
            if line.startswith("* "):
                list_to_shuffle.append(f"\n\n({pagename})\n\n{line}")

if pageq == "p" or pageq == "pick":
    print("Picking a random film...")
    filmpick("Uploaded to Commons")
    filmpick("Not uploaded to Commons")
    random_max = len(list_to_shuffle)-1
    random = random.randint(0, random_max)
    print(list_to_shuffle[random])
    exit()

#Correction of Motion Pictures, 1912-1939 page

try:
    int(pageq)
    print("Processing correction of Motion Pictures, 1912-1939 page...")
    pagename = f"Page:Motion Pictures 1912 to 1939 (IA Motionpict19121939librrich0010).djvu/{pageq}"
    site = pywikibot.Site()
    page = pywikibot.Page(site, pagename)
    page.text = page.text.replace("”", "\"")
    page.text = page.text.replace(" \n", "\n")
    page.text = page.text.replace("\n**SEE", " SEE")
    page.text = page.text.replace("\n** SEE", " SEE")
    page.text = page.text.replace("SEE\n** ", " SEE ")
    page.text = page.text.replace("SEE\n**", " SEE ")
    page.text = page.text.replace(",\n", ".\n")
    page.text = page.text.replace("\n\n\n", "\n\n")
    page.text = page.text.replace(", ©", ". ©")
    page.text = page.text.replace("..", ".")
    page.text = page.text.replace(",.", ".")
    page.text = page.text.replace("\n** SEE", " SEE")
    page.text = page.text.replace("Bros,", "Bros.")
    page.text = page.text.replace("Co,", "Co.")
    page.text = page.text.replace("Corp,", "Corp.")
    page.text = page.text.replace("Credits;", "Credits:")
    page.text = page.text.replace("descr,", "descr.")
    page.text = page.text.replace("deser,", "descr.")
    page.text = page.text.replace(" deser.", " descr.")
    page.text = page.text.replace("Eclair", "Éclair")
    page.text = page.text.replace("Frangaise", "Française")
    page.text = page.text.replace(", From", ". From")
    page.text = page.text.replace(" ft,", " ft.")
    page.text = page.text.replace("Inc,", "Inc.")
    page.text = page.text.replace("Ju1", "Jul")
    page.text = page.text.replace("Metro-Goldwyn- ", "Metro-Goldwyn-")
    page.text = page.text.replace("Mfg,", "Mfg.")
    page.text = page.text.replace("Mr,", "Mr.")
    page.text = page.text.replace("Mrs,", "Mrs.")
    page.text = page.text.replace("0ct", "Oct")
    page.text = page.text.replace("Players- ", "Players-")
    page.text = page.text.replace("Prod,", "Prod.")
    page.text = page.text.replace("pseud,", "pseud.")
    page.text = page.text.replace("Ltd,", "Ltd.")
    page.text = page.text.replace(" v, ", " v. ")
    page.text = page.text.replace(" no,", " no.")
    page.text = re.sub(r" LP ([0-9])", r" LP \1", page.text)
    page.text = re.sub(r" LU ([0-9])", r" LU \1", page.text)
    page.text = re.sub(r" MP ([0-9])", r" MP \1", page.text)
    page.text = re.sub(r" MU ([0-9])", r" MU \1", page.text)
    page.text = re.sub(r" ([A-Z]), ", r" \1. ", page.text)
    page.text = re.sub(r" \(([A-Z]), ", r" (\1. ", page.text)
    page.text = re.sub(r"([0-9])\n", r"\1.\n", page.text)
    page.text = page.text.replace("  ", " ")
    print("Processed!")
    page.save("Fixed something on the Internet that's from before the Internet existed: autofixed some OCR errors on this page")
    print("All done!")
    exit()
except ValueError:
    pagename = f"Wikisource:WikiProject Film/Drafts/{pageq}"
# pagename = f"{pageq}"
site = pywikibot.Site()

page = pywikibot.Page(site, pagename)

if page.text == "" and pageq != "r":
    print(f"Page {pagename} does not exist. Please check the name and try again.")
    exit()

# Correct GeoCities transcript

if page.text.startswith("g\n"):
    print("Fixing GeoCities transcript...")
    geocities_list = []
    geocities_lines = page.text.split("\n")
    for line in geocities_lines: #initial conversion from everything
        line = line.lstrip()
        try:
            int(line)
            geocities_list.append("}}\n}}\n\n----\n\n\n\n")
        except ValueError:
            if line != "" and not line.startswith("["):
                geocities_list.append(line)
    geocities_list = " ".join(geocities_list)
    geocities_list = geocities_list.replace("  ", " ")
    geocities_list = geocities_list.replace("\n ", "\n")
    geocities_list = geocities_list.replace(" }", "}")
    geocities_list = geocities_list.replace("----\n\n\n\n\"", "----\n\n\n\n{{ft/d|\n{{c|\"")
    geocities_list = re.sub(r"----\n\n\n\n([A-Z])", r"----\n\n\n\n{{ft/s|\n{{c|\1", geocities_list)
    geocities_list = geocities_list.split("----\n")
    geocities_final = []
    for line in geocities_list:
        if "--" in line:
            twodash = line.replace("---", "—")
            twodash = line.replace("--", "—")
        else:
            twodash = line
        line = line.replace("-", "-")
        line = line.replace("---", "—")
        line = line.replace("--", "—")
        line = line.replace(" - ", "—")
        line = line.replace("\n- ", "—")
        line = line.replace(" -", "—")
        line = line.replace("- ", "")
        line = line.replace("-—", "——")
        line = line.replace("—-", "——")
        geocities_final.append(line)
    geocities_final = "----\n".join(geocities_final)
    geocities_final = geocities_final[8:]
    geocities_final += "}}\n}}"
    geocities_final = geocities_final.replace("\"'", "{{\" '}}")
    geocities_final = geocities_final.replace("'\"", "{{' \"}}")
    geocities_final = geocities_final.replace(" — ", "—")
    geocities_final = geocities_final.replace("— ", "—")
    geocities_final = geocities_final.replace(" —", "—")
    geocities_final = geocities_final.replace("\n—", "\n{{ft/s|\n{{c|—")
    page.text = f"{geocities_final}"
    print("Done. Saving...")
    page.save(f"Fixed something on the Internet that's from before the Internet existed")
    print("All done! Please remember to use me again when this is all proofread.")
    exit()

titles_q = input("Did you make sure to add the titles? ")

if pageq == "r":
    print("Processing correction of a copyright renewal page...")
    pagename = f"{titles_q}"
    site = pywikibot.Site()

    page = pywikibot.Page(site, pagename)
    page.text = page.text.replace("  ", " ")
    page.text = page.text.replace("\n*", "\n\n*")
    page.text = page.text.replace("\n\n*#", "\n*#")
    page.text = page.text.replace("\n=", "\n\n=")
    page.text = page.text.replace("®", "©")
    page.text = page.text.replace(", ©", ". ©")
    page.text = page.text.replace("Bros,", "Bros.")
    page.text = page.text.replace("Co,", "Co.")
    page.text = page.text.replace("Corp,", "Corp.")
    page.text = page.text.replace("Inc.", "inc.")
    page.text = page.text.replace("Inc,", "inc.")
    page.text = page.text.replace("0ct", "Oct")
    print(page.text)
    page.save("Fixed something on the Internet that's from before the Internet existed: autofixed some OCR errors on this page")
    exit()

page.text = page.text.replace("\n\n\n", "\n\n")
page.text = page.text.replace("}}\n----", "}}\n\n----")
page.text = re.sub(r"----\n([0-9])", r"----\n\n\1", page.text)
page.text = page.text.replace("<br>", "<br />")

parse = page.text.split("\n\n")
dashesbool = False

for item in parse:
    if item == "----" and dashesbool == False:
        dashesbool = True
    if not item.endswith("}}") and item != "----" and item != "----" and not item.startswith("0") and not item.startswith("1") and not item.startswith("2") and not item.startswith("3")  and not item.startswith("4") and not item.startswith("5") and dashesbool == True:
        print(f"ERROR: The following item ({parse.index(item)}) does not end with }}:\n\n{item}")
        exit()
data = []
single_line_data = []
time_bool = False
line_bool = False
title = pageq
if "(" in title:
    realtitle = title[:title.find("(")-1]
    realtitlewithsymbol = f"{title}|{realtitle}"
    disambig_to_check = realtitle
    disambig_page = pywikibot.Page(site, disambig_to_check)
    if disambig_page.text == "":
        similar = f"<!-- {{{{similar|{realtitle}}}}} -->\n"
    else:
        similar = f"{{{{similar|{realtitle}}}}}\n"
else:
    realtitle = title
    realtitlewithsymbol = title
    similar = ""
# print("Title: " + title)
file = ""
author = ""
author_proper = ""
author_override = ""
publisher = ""
year = ""
pd = ""
note = ""
if title.startswith("A "):
    defaultsort = f"{{{{DEFAULTSORT:{realtitle[2:]}}}}}"
    if title.startswith("An "):
        defaultsort = f"{{{{DEFAULTSORT:{realtitle[3:]}}}}}"
elif title.startswith("The "):
    defaultsort = f"{{{{DEFAULTSORT:{realtitle[4:]}}}}}"
else:
    defaultsort = ""
categories = ""
portals = ""
section = ""
next = ""
user = ""
problematic = False
problematic_list = []
time_num = 0

## remove page from Uploaded or Not uploaded list

def CartoonOrNot(medium):
    global categories
    if "Cartoons" in categories:
        categories = categories + f", {medium} cartoons"
    else:
        categories = categories + f", {medium} film"

# put all the data from the page into list and variables
for line in parse:
    if line.startswith("User: "):
        user = line[6:]
    if line.startswith("File: "):
        if line.startswith("File: File:"):
            print("ERROR: Filename began with \"File:\"! PLEASE don't do this, it's bad form!")
            file = line[11:]
        else:
            file = line[6:]
        if file.endswith("webm"):
            source = "webm"
        elif file.endswith("ogv"):
            source = "ogv"
        elif file.endswith("ogg"):
            source = "ogg"
    if line.startswith("Section: "):
        section = line[9:]
    if line.startswith("Next: "):
        next = f"[[{line[6:]}]]"
    if line.startswith("Author: "):
        author = line[8:]
        if ", " not in line and author.startswith("p "):
            author = author[2:]
            author_proper = f"[[Portal:{author}|]]"
            author_override = f"|override_author = [[Portal:{author}|]]"
        elif author == "Anonymous":
            author_proper = f"[[Portal:Anonymous texts|Anonymous]]"
            author_override = f"|override_author = [[Portal:Anonymous texts|Anonymous]]"
        elif ", " in line and not line.startswith("p "):
            author_proper = author.split(", ")
            if len(author_proper) == 2:
                author_proper = f"[[Author:{author_proper[0]}|]] and [[Author:{author_proper[1]}|]]"
            else:
                for auth in author_proper:
                    author_proper[author_proper.index(auth)] = f"[[Author:{auth}|]]"
                author_proper_last = author_proper.pop()
                author_proper = f"{', '.join(author_proper)}, and {author_proper_last}"
            author_override = f"|override_author = {author_proper}"
        else:
            author_proper = f"[[Author:{author}|]]"
            author_override = author
        print(author_proper)
        print(author_override)
    if line.startswith("Publisher: "):
        publisher = line[11:]
    if line.startswith("Year: "):
        year = line[6:]
    if line.startswith("PD: "):
        pd = line[4:]
    if line.startswith("Note: "):
        note = line[6:]
    if line.startswith("Cat: "):
        categories = line[5:]
        # Silent vs. Sound categorizing
        if "Silent film" not in categories and "Sound film" not in categories and "Silent cartoons" not in categories and "Sound cartoons" not in categories:
            if int(year) < 1927:
                CartoonOrNot("Silent")
            else:
                while 1:
                    silentorsound = input("Silent or sound? ")
                    if silentorsound == "si" or silentorsound == "silent":
                        CartoonOrNot("Silent")
                        break
                    elif silentorsound == "so" or silentorsound == "sound":
                        CartoonOrNot("Sound")
                        break
                    else:
                        print("Sorry, I didn't understand that. Type \"si\" for silent and \"so\" for sound.")
        # Romance subset of drama
        if "Romance film" in categories and "Drama film" not in categories:
            categories += ", Drama film"
        if ", " in categories:
            categories = categories.split(", ")
            categories.sort()
            portals = "/".join(categories)
            newcats = []
            for category in categories:
                newcats.append(f"[[Category:{category}]]")
            categories = "\n".join(newcats)
        else:
            portals = categories
            categories = f"[[Category:{categories}]]"
    if line_bool == True:
        single_line_data.append(line)
        if "{{" in single_line_data[0]:
            print(f"\nERROR: The following timestamp is incorrectly entered:\n\n{single_line_data[0]}")
            exit()
        if len(single_line_data[0]) <= 3:
            print(f"\nERROR: Looks like you forgot to fill in this timestamp:\n\n{single_line_data[0]}\n\n{single_line_data[1]}")
            exit()
        data.append({
            "time": single_line_data[0],
            "line": single_line_data[1]
        })
        single_line_data.clear()
        line_bool = False
    if time_bool == True:
        time_num += 1
        if line.endswith("p") or line.endswith("P"):
            linesplit = line.split(" ")
            single_line_data.append(linesplit[0])
            problematic = True
            problematic_list.append(time_num)
        else:
            single_line_data.append(line)
        time_bool = False
        line_bool = True
    if line == "----" or line == "-----":
        time_bool = True

# print(data[5])
# print(file)

edit_summary = f"Entering transcription of a film that's generations older than the Internet, on the Internet itself (proofread by {user} from [[Wikisource:WikiProject Film/Drafts/{title}]])"""

# edit_summary = f"It's sad that this film even exists, but I'm entering it because somebody's gotta do it... (proofread by {user} from [[Wikisource:WikiProject Film/Drafts/{title}]])"

# check if any important data missing
if user == "":
    print("\nERROR: User not specified!")
if pd == "":
    print("\nERROR: PD tag not specified!")
    exit()
if year == "":
    print("\nERROR: Year of publication not specified!")
    exit()
if publisher == "":
    print("\nERROR: Publisher not specified!")
    check_publisher = input("Are you sure you want to continue? ")
if author == "":
    print("\nERROR: Author not specified!")
    exit()
if file == "":
    print("\nERROR: Filename not specified!")
    exit()
if categories == "":
    catcontinue = input("No categories/portals were specified. Are you sure you want to continue? If not just CTRL+C or CTRL+Z to exit out. ")
if note == "TBA":
    print("\nERROR: Note is TBA!")
    exit()




# Create index page

progress = ""

if problematic:
    progress = "C"
else:
    progress = "V"

print("Processed!")
print("----")

pagename = f"Index:{file}"
page = pywikibot.Page(site, pagename)

indexpagescreate = []

for datum in data:
    time_for_index = datum["time"]
    indexpagescreate.append(f"{{{{time|{data.index(datum)+1}|t={time_for_index}}}}}")

index_pages = "\n".join(indexpagescreate)

page.text = f"""{{{{:MediaWiki:Proofreadpage_index_template
|Type=book
|Title=''[[{realtitlewithsymbol}]]''
|Language=en
|Volume=
|Author={author_proper}
|Translator=
|Editor=
|Illustrator=
|School=
|Publisher=[[Portal:{publisher}|{publisher}]]
|Address=
|Year={year}
|Key=
|ISBN=
|OCLC=
|LCCN=
|BNF_ARK=
|ARC=
|Source={source}
|Image=1
|Progress={progress}
|Pages={index_pages}
|Volumes=
|Remarks=
|Width=
|Css=
|Header=
|Footer=
|Transclusion=yes
}}}}
"""
print("Creating Index page...")
print(edit_summary)
page.save(f"{edit_summary}")
print("----")

# print(pagename)
# print(page.text)




# Create Pages

if titles_q == "":
    count = 0
else:
    try:
        count = int(titles_q)
    except TypeError:
        pass

def timedisplay(sec):
    time_elapsed_m = int(sec / 60)
    time_elapsed_h = int(time_elapsed_m / 60)
    time_elapsed_s_rem = int(sec % 60)
    time_elapsed_m_rem = int(time_elapsed_m % 60)
    if time_elapsed_m >= 1 and time_elapsed_m < 60:
        return f"{time_elapsed_h} hours, {time_elapsed_m} minutes, {time_elapsed_s_rem} seconds"
    elif time_elapsed_m >= 60:
        return f"{time_elapsed_h} hours, {time_elapsed_m_rem} minutes, {time_elapsed_s_rem} seconds"
    else:
        return f"{time_elapsed_h} hours, {time_elapsed_m} minutes, {sec} seconds"

while 1:
    count +=1
    percent = int(((count-1)/len(data)) * 100)
    eta = ((len(data) - count) * 12) + 112
    if count > len(data):
        break
    line_now = data[count-1]["line"]
    pagename = f"Page:{file}/{count}"
    page = pywikibot.Page(site, pagename)
    if count in problematic_list:
        page.text = f"""<noinclude><pagequality level="2" user="{user}" /></noinclude>{line_now}<noinclude></noinclude>"""
    else:
        page.text = f"""<noinclude><pagequality level="3" user="{user}" /></noinclude>{line_now}<noinclude></noinclude>"""
    page.text = page.text.replace(">/b", "")
    print("Doing: " + pagename)
    print(f"{percent}% done (page {count} of {len(data)}).")
    print(f"Estimated time remaining: {timedisplay(eta)}")
    print("Sleeping...")
    time.sleep(10)
    page.save(edit_summary)
    print("----")




# Generate final transclusion

transclusionpagescreate = []

pagename = title
page = pywikibot.Page(site, pagename)

for datum2 in data:
    time_for_transclusion = datum2["time"]
    transclusionpagescreate.append(f"{{{{page|{file}/{data.index(datum2)+1}|num={time_for_transclusion}}}}}")

transclusion_pages = "\n".join(transclusionpagescreate)

transcluded_content = f"""{similar}{{{{header
 | title       = {realtitle}
 | author      = {author_override}
 | translator  =
 | section     = {section}
 | previous    =
 | next        = {next}
 | year        = {year}
 | portal      = {portals}
 | notes       = {note}
{{{{Film|{file}|thumbtime=2|size=400px}}}}
}}}}{defaultsort}

<div style="margin-left: 3em; margin-right: 3em;">
{transclusion_pages}
</div>


{{{{{pd}}}}}

{categories}"""

print(transcluded_content)

page.text = f"{transcluded_content}"

print("All pages done! Transcluding...")
page.save(edit_summary)
print("----")





##### Remove from request lists

requestremove(pageq, year)



##### Archiving section

archivep1 = "Archiving draft page (part 1, redirect)..."
print(archivep1)

pagename = f"Wikisource:WikiProject Film/Drafts/{pageq}"
# pagename = f"{pageq}"
site = pywikibot.Site()

page = pywikibot.Page(site, pagename)

contents_to_archive = page.text

page.move(f"Wikisource:WikiProject Film/Drafts/Archives/{pageq}", "Archiving draft page...")

# page.text = f"#REDIRECT [[Wikisource:WikiProject Film/Drafts/Archives/{pageq}]]"
# page.save(f"{archivep1}")





# print("----")

# archivep2 = "Archiving draft page (part 2, archive page)..."
# print(archivep2)

# pagename = f"Wikisource:WikiProject Film/Drafts/Archives/{pageq}"
# # pagename = f"{pageq}"
# site = pywikibot.Site()

# page = pywikibot.Page(site, pagename)

# page.text = contents_to_archive
# page.save(f"{archivep2}")




print("----")

archivep3 = "Archiving draft page (part 3, removal from drafts list)..."
print(archivep3)

pagename = f"Wikisource:WikiProject Film/Drafts"

site = pywikibot.Site()

page = pywikibot.Page(site, pagename)

page_just_archived = ""
drafts_page_parse = page.text.split("\n")
for line in drafts_page_parse:
    if line.startswith(f"* [[/{pageq}|"):
        page_just_archived = line
        drafts_page_parse.remove(line)
page.text = "\n".join(drafts_page_parse)

if f"/{pageq}|" not in page_just_archived:
    print("ERROR: Somethin' ain't right on that draft page. Maybe a draft was moved and the draft list not updated? Go check that out.")
    # exit()

page.save(f"{archivep3}")




print("----")

pagename = f"Wikisource:WikiProject Film/Drafts/Archives"

site = pywikibot.Site()

page = pywikibot.Page(site, pagename)

archivep4 = "Archiving draft page (part 4, add entry to archives list)..."
print(archivep4)

page.text = f"{page.text}\n{page_just_archived}"

page.save(f"{archivep4}")

if title.startswith("The ") or title.startswith("A ") or title.startswith("An "):
    redirect_create = "Creating redirect for the title without 'The'/'A'/'An' at the beginning"
    no_beginning_title = title.split(" ")
    no_beginning_title.pop(0)
    no_beginning_title = " ".join(no_beginning_title)
    pagename = no_beginning_title
    page = pywikibot.Page(site, pagename)
    if page.text != "":
        print("COULD NOT CREATE PAGE, something was already there!")
    else:
        page.text = f"#REDIRECT [[{title}]]"
        page.save(f"{redirect_create}")

if title.endswith("!") or title.endswith("?"):
    redirect_create = "Creating redirect for the title without '!'/'?' at the end"
    no_punct_title = title[:-1]
    pagename = no_punct_title
    page = pywikibot.Page(site, pagename)
    if page.text != "":
        print("COULD NOT CREATE PAGE, something was already there!")
    else:
        page.text = f"#REDIRECT [[{title}]]"
        page.save(f"{redirect_create}")

if "&" in title:
    redirect_create = "Creating redirect for the title with 'and' in place of '&'"
    no_symbol_title = title.replace("&", "and")
    pagename = no_symbol_title
    page = pywikibot.Page(site, pagename)
    if page.text != "":
        print("COULD NOT CREATE PAGE, something was already there!")
    else:
        page.text = f"#REDIRECT [[{title}]]"
        page.save(f"{redirect_create}")


# Add page to Template:New texts if proofread fully

# pagename = "Template:New texts"
# page = pywikibot.Page(site, pagename)
#
# newtextparse = page.text.split("\n")
# newtextparse.insert(3, f"{{{{new texts/item|{title}|{author}|{year}}}}}")
# text_to_move = newtextparse[10]
# newtextparse.pop(10)
# newtextparse.insert(15, text_to_move)
# page.text = "\n".join(newtextparse)
#
# print("Adding to Template:New texts...")
# page.save(edit_summary)


#|Progress=X - To be verified
#|Progress=C - To be proofread
#|Progress=V - To be validated
