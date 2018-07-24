# -*- coding: utf-8 -*-
import sys, getopt
import pandas as pd


def readCSV(arquivo):
    df = pd.read_csv(arquivo)
    df = df[df.columns[:4]]
    df['JATRABALHOU'] = df['JATRABALHOU'].apply(lambda x: x.split(','))
    df['NOME'] = df['NOME'].apply(lambda x: x.strip())
    
    return df

def prep_args(args):
    has_csv = '--csv' in args
        
    args = args[:4]
    args.append(has_csv)

    return args

def check_nome(df, nome):
    for ator in df['NOME']:
        if nome == ator:
            return True
    
    return False

def create_csv(df, origem, elenco, nomeXid, idXnome):
    cols =['ORIGEM', 'DESTINO', 'TIPO', 'ID', 'LABEL', 'WEIGHT']
    exp = pd.DataFrame([], columns=cols)
    exp = exp[1:]
    
    
    for nome in elenco:
        exp = exp.append(pd.DataFrame([[nomeXid[origem], nomeXid[nome], 'undirected', nomeXid[nome], nome, df['TEMOSCAR'][nomeXid[nome]]]], columns=cols), ignore_index=True)
    

    exp.to_csv(origem + '.csv', sep=',', index=False)

def main(args):
    
    df = readCSV(args[0])
    
    if not check_nome(df, args[1]):
        print 'Não foi possível encontrar tal ator/atriz!'
        return
    
    args = prep_args(args)
    
    nomeXid = dict(zip(df['NOME'], df['ID']))
    idXnome = dict(zip(df['ID'], df['NOME']))
    
    atorId = nomeXid[args[1]]
    elenco = [idXnome[int(i)] for i in df['JATRABALHOU'][atorId]]
    
    if args[3]:
        create_csv(df, idXnome[atorId], elenco[:int(args[2])], nomeXid, idXnome)
    
    print args[1] + ' já trabalhou com:'
    print ', '.join(i + ' (ganhador de Oscar)' if df['TEMOSCAR'][nomeXid[i]] else i for i in elenco[:int(args[2])] )


if __name__ == "__main__":
    main(sys.argv[1:])

