def Hj(Pop_city: int, Pyouth: int, Pmiddle: int, Peldery: int):
    return Pop_city * ((Pyouth * 0.6274) + (Pmiddle * 0.5542) + (Peldery * 0.576))

def Nj(Pop_city: int, Pyouth: int, Pmiddle: int, Peldery: int):
    return Pop_city * ((Pyouth * 0.2987) + (Pmiddle * 0.1048) + (Peldery * 0.157))


def Bj(Pop_city: int, Pyouth: int, Pmiddle: int, Peldery: int):
    return Pop_city * ((Pyouth * 0.0747) + (Pmiddle * 0.219) + (Peldery * 0.154))

def Gj(Pop_city: int, Pyouth: int, Pmiddle: int, Peldery: int):
    return Pop_city * ((Pmiddle * 0.122) + (Peldery * 0.113))

def forecast(H, N, B, G):
    return (G * 0.723) + (B * 0.598) + (H * 0.1425) + (N * 0.04666666)

YEARS = 2

# Seattle
pop = 1711000
Py = 0.1401
Pmid = 0.7222
Peld = 0.1378
H = Hj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)
N = Nj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)
B = Bj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)
G = Gj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)

res = forecast(H, N, B, G)
print("Seattle today", res)
print("increase", res * ((1.25)*YEARS)/300)
print("people accepted", (res * ((1.25)*YEARS)/300)*0.28)
print("NEW TOTAL", res + res * ((1.25)*YEARS)/300)
print("*"*12)

# Omaha
pop = 494700
Py = 0.1444
Pmid = 0.6557
Peld = 0.1499
H = Hj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)
N = Nj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)
B = Bj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)
G = Gj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)

res = forecast(H, N, B, G)
print("Omaha today", res)
print("increase", res * ((1.25)*YEARS)/300)
print("people accepted", (res * ((1.25)*YEARS)/300)*0.28)
print("NEW TOTAL", res + res * ((1.25)*YEARS)/300)
print("*"*12)

# Scranton
pop = 247700
Py = 0.166
Pmid = 0.6214
Peld = 0.2126
H = Hj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)
N = Nj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)
B = Bj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)
G = Gj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)

res = forecast(H, N, B, G)
print("Scranton today", res)
print("increase", res * ((1.25)*YEARS)/300)
print("NEW TOTAL", res + res * ((1.25)*YEARS)/300)
print("people accepted", (res * ((1.25)*YEARS)/300)*0.28)
print("*"*12)

# Liverpool
pop = 734980
Py = 0.1907
Pmid = 0.677
Peld = 0.1322
H = Hj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)
N = Nj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)
B = Bj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)
G = Gj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)

res = forecast(H, N, B, G)
print("Liverpool today", res)
print("increase", res * ((1.25)*YEARS)/300)
print("NEW TOTAL", res + res * ((1.25)*YEARS)/300)
print("people accepted", (res * ((1.25)*YEARS)/300)*0.28)
print("*"*12)

# Barry Whales
pop = 55200
Py = 0.159
Pmid = 0.641
Peld = 0.2002
H = Hj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)
N = Nj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)
B = Bj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)
G = Gj(Pop_city=pop, Pyouth=Py, Pmiddle=Pmid, Peldery=Peld)

res = forecast(H, N, B, G)
print("Barry Whales today", res)
print("increase", res * ((1.25)*YEARS)/300)
print("NEW TOTAL", res + res * ((1.25)*YEARS)/300)
print("people accepted", (res * ((1.25)*YEARS)/300)*0.28)
print("*"*12)

