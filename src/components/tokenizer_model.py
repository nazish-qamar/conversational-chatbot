from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer=GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.add_special_tokens({
    "pad_token": "<pad>",
    "bos_token": "<startofstring>",
    "eos_token": "<endofstring>"
})
tokenizer.add_tokens(["<bot>:"])