from transformers import ElectraTokenizer, ElectraForQuestionAnswering, pipeline
import streamlit as st


def get_model(model_path: str = "./model"):
    model = ElectraForQuestionAnswering.from_pretrained(model_path)
    return model


def get_tokenizer(model_path: str = "./model"):
    tokenizer = ElectraTokenizer.from_pretrained(model_path)
    return tokenizer


def get_answer(model, tokenizer, context: str, question: str) -> str:
    qa = pipeline("question-answering", tokenizer=tokenizer, model=model)
    answer = qa({"question": question, "context": context})["answer"]

    return answer
