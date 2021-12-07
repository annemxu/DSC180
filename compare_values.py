#!/usr/bin/env python
# coding: utf-8

def main(result_list):
    import pandas as pd

    alpha = 0.001
    beta = 0.15
    required_n_datasets = 5

    inhibitors = ['Akti', 'BTKi', 'Crassin', 'Dasatinib', 'GDC-0941', 'Go69', 'H89', 'IKKi', 'Imatinib',
                  'Jak1i', 'Jak2i', 'Jak3i', 'Lcki', 'Lestaurtinib', 'PP2', 'Rapamycin', 'Ruxolitinib',
                  'SB202', 'SP6', 'Sorafenib', 'Staurosporine', 'Streptonigrin', 'Sunitinib', 'Syki',
                  'Tofacitinib', 'U0126', 'VX680']

    populations = ['cd14+hladr-', 'cd14+hladrhigh', 'cd14+hladrmid', 'cd14+surf-', 'cd14-hladr-',
                   'cd14-hladrhigh', 'cd14-hladrmid', 'cd14-surf-', 'cd4+', 'cd8+', 'dendritic',
                   'igm+', 'igm-', 'nk']

    activators = ['pVO4', 'IL3', 'IL2',  'IL12', 'GCSF', 'GMCSF', 'BCR', 'IFNg', 'IFNa', 'LPS', 'PMA-IONO']

    variables = ['Time', 'Cell_length', 'CD3', 'CD45', 'BC1', 'BC2', 'pNFkB', 'pp38', 'CD4', 'BC3', 'CD20',
                 'CD33', 'pStat5', 'CD123', 'pAkt', 'pStat1', 'pSHP2', 'pZap70', 'pStat3', 'BC4', 'CD14',
                 'pSlp76', 'BC5', 'pBtk', 'pPlcg2', 'pErk', 'BC6', 'pLat', 'IgM', 'pS6', 'HLA-DR', 'BC7',
                 'CD7', 'DNA-1', 'DNA-2']
    important_variables = ['pNFkB', 'pp38', 'pStat5', 'pAkt', 'pStat1', 'pSHP2', 'pZap70', 'pStat3', 'pSlp76',
                           'pBtk', 'pPlcg2', 'pErk', 'pLat', 'pS6']

    # links predicted by backshift in paper
    paper_backshift_links = pd.read_csv('paper_backshift_links.csv').dropna().reset_index(drop=True)

    # result of backshift links
    backshift_links = pd.DataFrame(result_list, columns=['population', 'source', 'target'])
    kegg_links = pd.read_csv('pathways/kegg_links.csv')

    # add 'p' to nodes in kegg data for phosphorylation
    def add_p(name):
        return 'p' + str(name)

    kegg_links['node1'] = kegg_links['node1'].apply(add_p)
    kegg_links['node2'] = kegg_links['node2'].apply(add_p)
    kegg_links = kegg_links.replace(['pNFkBIA', 'pNFkB1', 'pNFKB2'], 'pNFkB')

    unique_backshift_links = backshift_links[['source', 'target']].groupby(['source', 'target']).size().reset_index()
    counter = 0
    neg_counter = 0
    for i in range(len(unique_backshift_links)):
        row = unique_backshift_links.iloc[i]
        source, target = row['source'], row['target']
        if len(kegg_links[(kegg_links['node1'] == source) & (kegg_links['node2'] == target)]):
            counter += 1
        elif len(kegg_links[(kegg_links['node1'] == target) & (kegg_links['node2'] == source)]):
            neg_counter += 1
    print('BACKSHIFT MATCHING WITH KEGG: ', 'Forward: ', counter, ' Backwards: ', neg_counter)

    counter = 0
    neg_counter = 0
    for i in range(len(unique_backshift_links)):
        row = unique_backshift_links.iloc[i]
        source, target = row['source'], row['target']
        if len(paper_backshift_links[(paper_backshift_links['Source'] == source) & (paper_backshift_links['Target'] == target)]):
            counter += 1
        elif len(paper_backshift_links[(paper_backshift_links['Source'] == target) & (paper_backshift_links['Target'] == source)]):
            neg_counter += 1
    print('BACKSHIFT MATCHING WITH PAPER: ', 'Forward: ', counter, ' Backwards: ', neg_counter)
