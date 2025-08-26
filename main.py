#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, argparse, sys, re, pathlib
LEX_PATH = pathlib.Path(__file__).parent / "lexicon.json"
def load_lex():
    with open(LEX_PATH,"r",encoding="utf-8") as f: data=json.load(f)
    by_eu5={e["eu5"].upper():e for e in data}; rev={}
    for e in data:
        for k in ["fr","en","de","es","it"]:
            rev.setdefault(k,{})[e[k].lower()]=e
    return data,by_eu5,rev
def toks(s): import re; return re.findall(r"[A-Za-z_+\-]+|[?]+", s)
def eu5_to_lang(ts,lang,by): out=[]; 
    # minimal demo
    for t in ts:
        u=t.upper()
        if u in by: out.append(by[u][lang])
        elif u=="++": out.append({"fr":"et","en":"and","de":"und","es":"y","it":"e"}[lang])
        elif u.startswith("NO-"): out.append({"fr":"pas","en":"not","de":"nicht","es":"no","it":"non"}[lang])
        else: out.append(t)
    return " ".join(out)
def lang_to_eu5(ts,lang,rev):
    out=[]; conj={"fr":"++","en":"++","de":"++","es":"++","it":"++"}
    for t in ts:
        l=t.lower()
        if l in ["et","and","und","y","e"]: out.append(conj[lang])
        elif l in ["pas","not","nicht","no","non"]: out.append("no-")
        elif l in rev[lang]: out.append(rev[lang][l]["eu5"])
        else: out.append(t.upper())
    # merge no-
    m=[]; i=0
    while i<len(out):
        if out[i]=="no-" and i+1<len(out): m.append("no-"+out[i+1]); i+=2
        else: m.append(out[i]); i+=1
    return " ".join(m)
def show_lex(data):
    print(f"{'EU5':<14} EMOJI  FR / EN / DE / ES / IT")
    for e in data: print(f"{e['eu5']:<14} {e['emoji']}  {e['fr']} / {e['en']} / {e['de']} / {e['es']} / {e['it']}")
def main():
    p=argparse.ArgumentParser(); 
    p.add_argument("--from",dest="src",default="eu5",choices=["eu5","fr","en","de","es","it"])
    p.add_argument("--to",dest="dst",default="fr",choices=["eu5","fr","en","de","es","it"])
    p.add_argument("--lexicon",action="store_true"); p.add_argument("text",nargs="*")
    a=p.parse_args(); data,by,rev=load_lex()
    if a.lexicon: show_lex(data); sys.exit(0)
    s=" ".join(a.text); ts=toks(s)
    if a.src=="eu5" and a.dst in rev: print(eu5_to_lang(ts,a.dst,by)); sys.exit(0)
    if a.dst=="eu5" and a.src in rev: print(lang_to_eu5(ts,a.src,rev)); sys.exit(0)
    print("Try EU5->FR or FR->EU5"); sys.exit(2)
if __name__=="__main__": main()