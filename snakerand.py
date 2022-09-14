import random
import string
from collections import defaultdict

rels = """
    aq
    aw
    as
    az
    qw
    ws
    we
    se
    sd
    sz
    sx
    xd
    xc
    ed
    er
    dr
    df
    dc
    cf
    cv
    rt
    rf
    ft
    fg
    fv
    vg
    vb
    ty
    tg
    gy
    gh
    gb
    bh
    bn
    yu
    yh
    hu
    hj
    hn
    nj
    nm
    ui
    uj
    ji
    jk
    jm
    mk
    io
    ik
    ko
    kl
    op
    ol
"""

graph = defaultdict(set)
for rel in rels.split('\n'):
    rel = rel.strip()
    if not rel:
        continue
    assert len(rel) == 2
    graph[rel[0]].add(rel[1])
    graph[rel[1]].add(rel[0])

graph = {k: list(v) for k, v in graph.items()}
start = random.choice(string.ascii_lowercase)
accum = start
for i in range(10):
    accum += random.choice(graph[accum[-1]])

print(accum)
