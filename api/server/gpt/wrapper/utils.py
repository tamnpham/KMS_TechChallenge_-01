def default_preprocessing(schema: str, question: str) -> str:
    return f"schema: {schema} | question: {question} | sql:"

def default_posprocessing(result: str) -> str:
    return result.split('|')[0]