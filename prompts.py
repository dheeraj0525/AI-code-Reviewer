def code_review_prompt(code: str, language: str) -> str:
    return f"""
You are a senior software engineer.

Analyze the following {language} code.
Tasks:
1. Identify syntax errors
2. Identify logical issues
3. Explain mistakes in simple language
4. Provide corrected code

Code:
{code}

Respond in this format:
- Errors:
- Explanation:
- Corrected Code:
"""