# Component specification


1. `Retriever`
  - _Inputs_: URL or PDF file
  - _Outputs_: string text
  - Not sure if this requires any LLM at all. May be tools to make this easy in langchain

2. `SummaryPromptTemplate`
  - _Inputs_: any parameterization for things for LLM to focus on, boolean options like add citation, bullet points or prose, etc.

3. `SummaryOutputParser`
  - _Inputs_: Markdown options
  - Not sure if we need this, but handles taking LLM output and formatting to desired format using REGEX

4. `Summarizer`
  - _Inputs_: Prompt Template, OutputParser, Document Text
  - _Outputs_: Summary text
  - Langchain has tools already to help with this, things that automatically break up big documents into chunks and distill using LLM