"""Expresses the output desired of the summary.

LangChain has builtin support for JSON output, build on this to create
rich text for the user's file from the JSON
"""
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

from typing import List
from collections import OrderedDict

ACCEPTABLE_PAPER_SECTIONS = OrderedDict([
    ("Motivation", "State of the literature that the authors are trying to address"),
    ("Methods", "Techniques, steps, tools, and parameters used by the authors to accomplish their goal"),
    ("Data Used", "Any third party data that the authors used."),
    ("Results", "What the authors produced using to address the goal."),
    ("Data Produced", "Any data that the authors produced."),
    ("Software Produced", "Any open source software that the authors produced, such as models or tools"),
    ("Conclusion", "Analysis and takeaways from the results, any future work that can be done."),
])

class PaperOutputParser(StructuredOutputParser):

    @classmethod
    def from_sections(cls, sections: List[str]) -> PaperOutputParser:
        """Creates a PaperOutputParser from a list of sections the user wants to include in the summary."""
        # enforce section ordering
        new_sections = []
        for section in ACCEPTABLE_PAPER_SECTIONS.keys():
            if section not in sections:
                pass
            else:
                new_sections.append(section)
        if len(new_sections) != len(sections):
            raise ValueError(f"Sections {sections} not all valid, please choose from {list(ACCEPTABLE_PAPER_SECTIONS.keys())}")
        
        schemas = [ResponseSchema(name=section, description=ACCEPTABLE_PAPER_SECTIONS[section]) for section in new_sections]
        return cls.from_response_schemas(schemas)

    def parse(self, text: str) -> Any:
        dic = super().parse(text)
        sections = [schema.name for scema in self.response_schemas]
        md = ""
        for section in sections:
            md += f"## {section}\n"
            md += dic[section]
        return md