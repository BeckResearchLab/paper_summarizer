# paper_summarizer
Use LangChain to create a pipeline to summarizing academic papers

## Setup

Install via:
```
conda create --file environment.yml
pip install .
```

Fill in config file for API access at `config`

## Usage

Prepare the environment:
```
conda activate paper_summarizer
source config
```

Run the pipeline on an HTML or path to pdf
```
python main.py --html https://afwargwerhewrth.com/qwrgaerhgqwer --out_name my_summary.md
```

A summary with citation is then appended in `./deposit/my_summary.md` in the format

```
### Source
https://afwargwerhewrth.com/qwrgaerhgqwer

### Citation
a citation

### Summary
1-2 paragraphs of summary, bullets for most important conclusions

### Tags
machine learning, neuroscience, data processing
###
```

