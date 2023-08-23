This is a collection of tools used for parsing film transcription draft pages at Wikisource. These tools were made on behalf of Wikisource's WikiProject Film, of which I am the founder.

## Explanation ##

The normal method of proofreading works at Wikisource is to use the page-by-page proofreading process through the ProofreadPage MediaWiki extension. However, due to some technical difficulties, using ProofreadPage to proofread a film, rather than a scan of a book, is absolute **hell** to do.

So, the film draft system is the workaround I invented to resolve this issue. Much like my QuickTranscribe workflow (which I actually developed several years later than these tools), the film draft system takes a single-page approach to film proofreading rather than a multi-page approach.

Film drafts are produced and processed here: https://en.wikisource.org/wiki/Wikisource:WikiProject_Film/Drafts

## Dependencies ##
* pywikibot

## films.py ##

The script for parsing film transcription drafts that are completed, to insert all the data into the relevant places.

## dialogue.py ##

For audiovisual films (rather than silent films, which is what is normally worked with), this tool parses an initial text layer of dialogue line by line. It allows you to insert the character names and timestamps, and also make minor changes to the text where there are typos.

## To do in the future ##

* Clean up the code.
* Integrate transcriptions to Wikidata.