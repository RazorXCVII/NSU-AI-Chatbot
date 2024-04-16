#Importing necessary packages
from llama_index.core import PromptTemplate

#As guided by Llama Index docs
instruction_str = """\
    1. Convert the query to executable Python code using Pandas.
    2. The final line of code should be a Python expression that can be called with the `eval()` function.
    3. The code should represent a solution to the query.
    4. PRINT ONLY THE EXPRESSION.
    5. Do not quote the expression."""

new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression: """
)

#Describing what our chatbot will do
context = """Purpose: The role of agent is to assist North South University Students in their daily lives as a student by providing them support and acccurate information about their student life and NSU itself, and help make their university struggles as easier as possible."""