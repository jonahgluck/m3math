import torch.nn as nn
import numpy as np
import torchtext
import collections
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

tokenizer = torchtext.data.utils.get_tokenizer('basic_english')

counter = collections.Counter()

def encode_tokens(x):
    tokens = tokenizer(x)
    return [vocab.get_stoi()[t] for t in tokens]


#dfx = pd.read_csv("/Users/jonah/Downloads/m3/omaha_monster_remote.csv")
#dfy = pd.read_csv("/Users/jonah/Downloads/m3/omaha_monster_notremote.csv")
dfy = pd.read_csv("/Users/jonah/Downloads/m3/seattle_monster_remote.csv")
#dfx = pd.read_csv("/Users/jonah/Downloads/m3/seattle_notremote_monster.csv")
dfx = pd.read_csv("/Users/jonah/Downloads/m3/scranton_remote_monster.csv")
#dfy = pd.read_csv("/Users/jonah/Downloads/m3/scranton_notremote_monster.csv")
#dfx = pd.read_csv("/Users/jonah/Downloads/m3/barrywhales_totaljobs_notremote.csv")
#dfx = pd.read_csv("/Users/jonah/Downloads/m3/liverpool_totaljobs_remote.csv")

col = dfx.iloc[:,0]


x = []
for seq in col:
    seq = seq.lower().split("\n")
    for line in seq:
        counter.update(tokenizer(line))
        tokenized = tokenizer(line)
        for i in range(len(tokenized)):
            n_gram_seq = tokenized[:i+1]
            x.append(n_gram_seq)

vocab = torchtext.vocab.vocab(counter, min_freq=1)
print(f"Vocab length: {len(vocab)}")
xn = [encode_tokens(tok) for _in in x for tok in _in]


col = dfy.iloc[:,0]

y = []
for seq in col:
    seq = seq.lower().split("\n")
    for line in seq:
        counter.update(tokenizer(line))
        tokenized = tokenizer(line)
        for i in range(len(tokenized)):
            n_gram_seq = tokenized[:i+1]
            y.append(n_gram_seq)

vocab = torchtext.vocab.vocab(counter, min_freq=1)
print(f"Vocab length: {len(vocab)}")
yn = [encode_tokens(tok) for _in in y for tok in _in]
#assume wfh:= virtual, work from home, home, remote
#wfh = ["virtual", "home", "remote"]
wfh = ["home", "remote"]
wfh = [encode_tokens(idx) for idx in wfh][0]
uxn, uyn = [], []
uxn.append([xn[i][0] for i in range(len(xn))])
uyn.append([yn[i][0] for i in range(len(yn))])

xn = uxn[0]
yn = uyn[0]

corr = np.correlate(xn, yn, 'full')

remote_count = 0
for val in xn:
    if val == wfh:
        remote_count+=1


print(remote_count)


plt.plot(corr)
plt.savefig('corr.png')

corr_df = pd.DataFrame(data=corr)
corr_df.to_csv('corr.csv')


