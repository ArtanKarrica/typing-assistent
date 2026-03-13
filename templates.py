from string import Template

CORRECT_TEXT_TEMPLATE_Old = Template("""
Correct all typos, and fix punctuation and grammar in the following text. Preserve the original formatting, including line breaks.
Original text:
<text>
$text
</text>

Return only the corrected text without any comments or explanations.                               
""")

CORRECT_TEXT_TEMPLATE = Template("""
Correct the text below by fixing only:
- spelling
- grammar
- punctuation
- capitalization
- obvious word-choice mistakes

Preserve:
- the original meaning
- the original language
- the original tone
- line breaks and spacing
- names, technical terms, and emphasis

Make only the minimum necessary changes.
Do not rewrite for style unless needed for clarity.
Do not add new information.
Do not include commentary, reasoning, labels, or quotation marks.
Return only the corrected text.

Original text:
<text>
$text
</text>
""")


CORRECT_TEXT_V2_TEMPLATE = Template("""
Rewrite the text below to improve clarity, flow, and readability.

Preserve:
- the original meaning
- the original language
- the original tone and intent
- important names, terms, and emphasis
- roughly the same length

Adjust the wording only as much as needed to make the text sound polished and natural.
For short informal text, keep it conversational.
For longer text, improve structure and coherence without becoming verbose.

Do not add new information.
Do not answer questions contained in the text.
Do not include commentary, reasoning, labels, bullet points, or quotation marks.
Return only the rewritten text.

Original text:
<text>
$text
</text>
""")

IMPROVE_TEXT_TEMPLATE = Template("""
Rewrite the text below to improve clarity and flow while preserving:
- the original meaning
- the original language
- the original tone
- important names, terms, and emphasis
- roughly the same length

Make it sound natural and conversational when appropriate, but do not make it casual if the original text is formal.
Do not add new information.
Do not answer questions in the text.
Do not include commentary, reasoning, labels, or quotation marks.
Return only the rewritten text.

Original text:
<text>
$text
</text>
""")


SYSTEM_PROMPT_TEMPLATE = Template("""
You are a text editor.

Your job is to improve or correct user-provided text while preserving its meaning, language, tone, and formatting unless the user explicitly asks otherwise.

Rules:
- Follow the user task exactly.
- Preserve names, numbers, technical terms, and emphasized words.
- Do not add new facts or remove important details.
- Do not include explanations, reasoning, notes, labels, or preambles.
- Return only the final edited text.
""")
