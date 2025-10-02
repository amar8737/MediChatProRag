from euriai.langchain import create_chat_model

def get_chat_model(api_key: str,model_name: str):
    """
    This function return the chat model
    """
    chat_model = create_chat_model(api_key=api_key,model_name=model_name,temperature=0.7)
    return chat_model

def ask_chat_model(chat_model,prompt:str):
    return chat_model.invoke(prompt).content
