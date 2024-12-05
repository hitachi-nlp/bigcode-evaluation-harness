import logging

from vllm import LLM


def is_vllm_model(model):
    return isinstance(model, LLM)
