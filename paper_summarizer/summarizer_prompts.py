"""Chain for summarization of input text into correct format"""

from langchain import PromptTemplate
from .output_parser import PaperOutputParser

BASE_SUMMARIZER_PROMPT = """You are summarizing acedemic papers. Focus on extracting important motivation,
methods, results, and conclusions. Be concise, but pay attention to details.
{sections_included}

{format_instructions}

TEXT:
{text}

SUMMARY:"""

def get_prompt_template(output_parser: PaperOutputParser = None, internal: bool = True) -> PromptTemplate:
    """Returns a prompt template for the summarizer, with the correct sections included.
    
    This is different depending on if the prompt is internal or the one that combines everything.
    """
    if output_parser is None:
        return PromptTemplate(
            input_variables=['text'],
            partial_variables={
                "sections_included": "A few paragraphs is acceptable, do not miss any important details",
                "format_instructions": ""},
            template=BASE_SUMMARIZER_PROMPT)
    else:
        if not internal:
            return PromptTemplate(
                input_variables=['text'],
                partial_variables={
                    "sections_included": f"Please organize the summary into the following sections: {', '.join(sections)}. If content does not align with a section, ignore it.",
                    "format_instructions": output_parser.get_format_instructions()},
                template=BASE_SUMMARIZER_PROMPT)
        else:
            return PromptTemplate(
                input_variables=['text'],
                partial_variables={
                    "sections_included": f"Please focus on the following sections: {', '.join(sections)}. If content does not align with a section, ignore it.",
                    "format_instructions": ""},
                template=BASE_SUMMARIZER_PROMPT)
        
