from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Translation template
translation_template = """
Translate the following sentence into {language}, return ONLY the translation, nothing else.

Sentence: {sentence}
"""

# Output parser
output_parser = StrOutputParser()

# Initialize the LLM with the correct model name
llm = ChatOpenAI(api_key='api', temperature=0.0, model="gpt-4o-mini")

# Create the translation prompt
translation_prompt = ChatPromptTemplate.from_template(translation_template)

# Define the translation chain
translation_chain = (
    {"language": RunnablePassthrough(), "sentence": RunnablePassthrough()} 
    | translation_prompt
    | llm
    | output_parser
)

# Function to perform translation
def translate(sentence, language="French"):
    data_input = {"language": language, "sentence": sentence}
    translation = translation_chain.invoke(data_input)
    return translation

