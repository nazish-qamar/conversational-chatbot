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

    dialogs = dialogs[:-1]
    return dialogs