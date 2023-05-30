import json

from src.logger import logging


def extract_dialogs(dataset):
    dialogs = []
    for rows in dataset:
        for dialog in rows['dialog']:
            dialogs.append(dialog['text'])
    return dialogs


def add_tokens_to_dialogs(dialogs, token_config):
    try:
        botstr = " " + token_config['bot_token'] + ": "
        endstr = " " + token_config['end_token']
        for idx, i in enumerate(dialogs):
            dialogs[idx] = token_config['start_token'] + i + botstr + dialogs[idx + 1] + endstr
    except:
        logging.info("Reached the last dialog.")

    # uncomment the line below to train with smaller dataset
    # dialogs = dialogs[:3000]
    return dialogs


def process_output(reply: str):
    reply = reply.split("bot:")[-1]
    reply = reply.replace("<pad>", "")
    reply = reply.replace("<startofstring>", "")
    reply = reply.replace("<endofstring>", "")
    return reply


def infer_tokenizer_len(path: str):
    added_tokens_file = path + "/added_tokens.json"
    with open(added_tokens_file, 'r') as f:
        data = json.load(f)

    return max(data.values()) + 1
