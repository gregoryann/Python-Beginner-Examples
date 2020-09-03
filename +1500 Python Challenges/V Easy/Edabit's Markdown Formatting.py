"""
Edabit's Markdown Formatting
Edabit allows for markdown formatting, meaning that it's possible to format words by surrounding text with special characters. For example, to get bold text, you surround the text with double asterisks, like this **bold**.

Here is a list of the possible formatting options in Edabit and how to apply them:

**bold**
_italics_
`inline code`
~~strikethrough~~
Challenge
Given a string and a style character, return the newly formatted string. Style characters are single letters that represent the different types of formatting.

For the purposes of this challenge, the style characters are as follows:

"b" is for bold
"i" is for italics
"c" is for inline code
"s" is for strikethrough
Examples
md_format("Bold", "b") ➞ "**Bold**"

md_format("leaning text", "i") ➞ "_leaning text_"

md_format("Edabit", "c") ➞ "`Edabit`"

md_format("That's a strike!", "s") ➞ "~~That's a strike!~~"
Notes
Remember to format your comments!

"""


"""
Solution 1
"""

def md_format(word, style):
	markdown = {'b':'**', 'i':'_', 'c':'`', 's':'~~'}
	return '{0}{1}{0}'.format(markdown[style], word)

"""
Solution 2
"""

def md_format(word, style):
	styles = {"b":"**", "i":"_","c":"`","s":"~~"}
	return styles[style] + word + styles[style]

"""
Solution 3
"""

style_code = {"b":"**" , "i":"_" , "c":"`" , "s":"~~"}
def md_format(word, style):
    m = style_code[style]
    return m+word+m

"""
Solution 4
"""

def md_format(word, style):
	fmt = {
		'b':'**',
		'i':'_',
		'c':'`',
		's':'~~'
	}
	return '{0}{1}{0}'.format(fmt[style],word)



