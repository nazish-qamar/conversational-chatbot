import json

from src.logger import logging

def extract_dialogs(dataset):
    dialogs = []
    for rows in dataset:
        for dialog in rows['dialog']:
            dialogs.append(dialog['text'])
    return dialogs


def add_tokens_to_dialogs(dialogs):
    try:
        for idx, i in enumerate(dialogs):
            dialogs[idx] = "<startofstring>" + i + " <bot>: " + dialogs[idx + 1] + " <endofstring>"
    except:
        logging.info("Reached the last dialog.")

    dialogs = dialogs[:3000]
    return dialogs


def process_output(reply:str):
    reply = reply.split("bot:")[-1]
    reply = reply.replace("<pad>", "")
    reply = reply.replace("<startofstring>", "")
    reply = reply.replace("<endofstring>", "")
    return reply


def infer_tokenizer_len(path:str):
    added_tokens_file = path + "/added_tokens.json"
    with open(added_tokens_file, 'r') as f:
        data = json.load(f)

    return max(data.values()) + 1
