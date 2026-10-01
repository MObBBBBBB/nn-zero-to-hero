import torch
import torch.nn as nn
import torch.nn.functional as F


# hyperparameters
block_size = 8
batch_size = 32
max_iters = 20000
eval_interval = 300
learning_rate = 1e-2
device = 'cuda' if torch.cuda.is_available() else 'cpu'
eval_iters = 200
# ---------------------------------------------------------------

torch.manual_seed(1337);


# import tiny shakespare
# wget https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt
# If the file path doesn't resolve at runtime, adjust it to match your IDE or editor's working directory.
with open("experiments/input.txt", 'r', encoding="UTF-8") as f:
    text = f.read()


# get all the characters in 'input.txt'
chars = sorted(set(text))
vocab_size = len(chars)
# character mapping from char to int
stoi = {ch:i for i, ch in enumerate(chars)}
itos = {i:ch for ch, i in stoi.items()}
# tokenizer
# Using lambda is for a quick call when we want to en/de-code a sequence.
encode = lambda s: [stoi[ch] for ch in s]         # endcode : take a string, return a list of integer
decode = lambda l: ''.join([itos[i] for i in l])  # decode  : take a list of integer, return a string


# encode whole input text
data = torch.tensor(encode(text), dtype=torch.long)

# split up data set to training and validation sets
n = int(0.9 * len(data))
tr_data = data[:n]
val_data = data[n:]


# build mini-batch for batched training
def get_batch(split):
    data = tr_data if split=='train' else val_data
    # Don't forget minus block_size on upper limit.
    ix = torch.randint(0, len(data) - block_size, (batch_size,))
    # Pytorch doesn't support by using tensor and integer to index a slice of a tensor.
    # (tensor[tensor: integer] is not suppoted.)
    # We can use comprehension to create every batch in a list,
    # then use torch.stack to stack these tensors to a big tensor.
    x = torch.stack([data[i:i+block_size] for i in ix])
    y = torch.stack([data[i+1:i+1+block_size] for i in ix])
    x, y = x.to(device), y.to(device)
    return x, y

@torch.no_grad()
def estimate_loss():
    # use a dict to store every loss of each date set
    out = {}
    # switch to evaluation mode
    m.eval()
    # evaluate train set and val set
    for split in ['train', 'val']:
        # losses storage 200 losses for caculating average loss
        losses = torch.zeros(eval_iters)
        # caculate loss and store
        for k in range(eval_iters):
            X, Y = get_batch(split)
            logits, loss = m(X, Y)
            losses[k] = loss.item()
        out[split] = losses.mean()
    # switch to training mode
    m.train()
    return out


# create bigram model by using nn.Module
class BigramLanguageModel(nn.Module):

    def __init__(self):
        super().__init__()
        self.token_embedding_table = nn.Embedding(vocab_size, vocab_size)

    # __call__ will call forward here to perform the forward pass
    def forward(self, idx, target=None):
        logits = self.token_embedding_table(idx)  # shape: (B, T, C)

        if target is None:
            loss = None
        else:
            # cross_entropy requires shape(B, C, T) in 3 dimensions or shape(B, C) in 2 dimensions.
            # C (the channel/embedding dimension) must be the second dimension.
            # We need reshape our tensors.

            # flatten way
            # logits = logits.view(-1, logits.shape[2])
            # target = target.view(-1)
            # transpose way
            loss = F.cross_entropy(logits.transpose(1, 2), target)
        return logits, loss

    def generate(self, sq, max_new_tokens):
        for _ in range(max_new_tokens):
            logits, loss = self(sq)
            # Focus on the last prediction, because the predictions in context has already generated.
            # We need the last prediction to predict what is the next token should be.
            logits = logits[:, -1, :]  # return a tensor with shape(B, C)
            probs = F.softmax(logits, dim=-1) # (B, C)
            idx = torch.multinomial(probs, num_samples=1) # (B, 1)
            sq = torch.cat((sq, idx), dim=1)  # (B, T+1)
        return sq


m = BigramLanguageModel().to(device)
optimizer = torch.optim.AdamW(m.parameters(), lr=learning_rate)

# training loop
for steps in range(max_iters):
    # mini-batch
    x, y = get_batch('train')

    # evaluate loss
    if steps % eval_interval == 0:
        losses = estimate_loss()
        print(f"step {steps}: train loss {losses['train']:.4f}, val loss {losses['val']:.4f}")

    # forward pass
    logits, loss = m(x, y)

    # backward pass
    optimizer.zero_grad(set_to_none=True)
    loss.backward()

    # update
    optimizer.step()

losses = estimate_loss()
print(f"train loss: {losses['train']}, val loss: {losses['val']}")


# generate something after training
sq = m.generate(torch.zeros((1, 1), dtype=torch.long, device=device), max_new_tokens=500)
print(decode(sq[0].tolist()))
