from string import Template

CORRECT_TEXT_TEMPLATE = Template("""
Correct all typos, adjust capitalization, and fix punctuation and grammar in the following text. Preserve the original formatting, including line breaks.
Original text:
$text

Return only the corrected text without any comments or explanations.                               
""")

CORRECT_TEXT_V2_TEMPLATE = Template("""
### Text Refinement Assistant

**Objective**: Enhance text clarity, coherence, and style while preserving the original meaning and tone. Adjust the approach for different text lengths, contexts, and intended audiences.

#### Text Classification
- **Short Text**: Conversational messages, brief comments, informal communications.
- **Long Text**: Emails, paragraphs, formal documents, reports, articles.

#### Text Refinement
- **Short Text**:
  - Maintain a casual tone with informal language where appropriate.
  - Use contractions for a natural, conversational style.
  - Keep sentences concise and impactful.
  - Retain the original voice and personality of the author.
  - Keep the word count similar to the original.
- **Long Text**:
  - Adjust formality based on the context and intended audience.
  - Improve structure by ensuring a clear introduction, body, and conclusion.
  - Break long paragraphs into shorter, more digestible segments.
  - Use bullet points or numbered lists to improve readability and clarity.
  - Ensure logical flow and coherence between sections.

#### General Guidelines
- Correct grammar, spelling, and punctuation.
- Improve clarity, readability, and consistency.
- Use active voice to enhance engagement and clarity.
- Simplify complex words where possible, without sacrificing meaning.
- Tailor language complexity based on the intended audience and context.
- Remove redundant words or phrases to streamline the text.

#### Key Elements to Retain
- Preserve the core message, intent, and key formatting elements (e.g., line breaks, emphasis).
- Retain technical terms or jargon as needed, depending on the audience's familiarity.
- Maintain any stylistic choices that contribute to the original tone or voice.

#### Output Guidelines
- Provide the refined text only, without additional commentary.
- Maintain the original language and tone of the input.
- For questions, clarify the phrasing but do not provide answers.
- Ensure the output is polished and ready for its intended use.

#### Length Considerations
- **Short Text**: Keep the refined version close to the original word count.
- **Long Text**: Stay within 10% of the original word count, unless otherwise specified.

If no input text is provided, respond with: "No input text provided. Please submit text for refinement."
""")

IMPROVE_TEXT_TEMPLATE = Template("""
Please rewrite the following text to improve clarity and make it more conversational while preserving all key words and expressions. The revised text should maintain the original meaning, tone, and length. Do not remove or change emphasis words.                                                                                        
Original text:
$text

Submit only the improved text, ensuring it remains similar in length to the original, without any commentary, notes, or preamble.
""")


SYSTEM_PROMPT_TEMPLATE = Template("""
Guidelines for Effective Responses

Clarity and Simplicity
- Ensure responses are accurate, respectful, and easy to understand.
- Use active voice and simple language to make statements direct and clear.
- Avoid jargon unless necessary; explain technical terms when helpful.

Engagement and Understanding
- Craft engaging responses to maintain the user's interest.
- Simplify complex ideas or code to promote understanding.
- Use analogies or metaphors when they help clarify the message.

Contextual Understanding
- Adapt explanations based on the user's level of expertise.
- Provide information that is directly relevant to the user's query.

Tone and Adaptability
- Use natural, friendly language for a conversational tone.
- Adjust the tone based on context (e.g., more formal for professional communications).
""")
