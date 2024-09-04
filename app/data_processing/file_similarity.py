from app.prompting.chatgpt import chat_gpt


def compare_text_data(text_data_src, text_data_dest):
    """
    Compare two text data and return a similarity score.
    """
    prompt = f"""Compare the following two text data:\n
    Source Text:\n{text_data_src}\n
    Destination Text:\n{text_data_dest}\n
    Provide a similarity score between 0 and 100, where 0 indicates no similarity and 100 indicates identical text data.
    output a single integer value.
    """
    response = chat_gpt(prompt)
    try:
        similarity_score = int(response)
    except Exception as e:
        raise ValueError("Error extracting similarity score.") from e

    return similarity_score