""" Code for the FAIRplus cookbook identifier mapping with BridgeDB recipe

"""

import requests
import pandas as pd

url = "https://webservice.bridgedb.org/"
single_request = url+"{org}/xrefs/{source}/{identifier}{}"
batch_request = url+"{org}/xrefsBatch/{source}{}"

def to_df(response, batch=False):
    """ Using a request object generates a pandas dataframe from the text response.
    
    Using the given response from BridgeDB's webservices we retrieve the data and split it into
    4 columns. 
    
    Parameters
    ----------
    response : requests.Response object 
        Response of the webservices after having performed a GET or POST call
    batch: bool, optional
        Whether the mapping is being done for only one identifier or multiple
        
    Returns
    -------
    result_df : pandas DataFrame
        DataFrame containing the mappings in an easier to read and modify format
        
    """
    
    if batch:
        records = []
        for tup in to_df(response).itertuples():
            if tup[3] != None:
                for mappings in tup[3].split(','):
                    target = mappings.split(':', 1)
                    if len(target) > 1:
                        records.append((tup[1], tup[2], target[1], target[0]))
                    else:
                        records.append((tup[1], tup[2], target[0], target[0]))
        return pd.DataFrame(records, columns = ['original', 'source', 'mapping', 'target'])
        
    return pd.DataFrame([line.split('\t') for line in response.text.split('\n')])

def get_mappings(file, org, source, case = 1, target = ''):
    """ Calculates mappings of identifiers from organism `org` and `source` identifier
    
    This method calculates the mappings of identifiers stored in `file` corresponding to organism
    `org`. If case == 1 then file should contain a TSV file with a list of identifiers from 
    `source`. If case == 2 the file should contain a TSV file containing pairs of identifiers 
    with the first element corresponding to a local identifier and the second one corresponding to
    `source`.
    
    Parameters
    ----------
    file : str
        Path to the TSV file containing the identifiers to be mapped
    org : str
        Name of the organism for which we are mapping
    source : str
        Name of the source dataset to which our identifiers correspond. It should be one of the
        data sources accepted by BridgeDb [see here](shorturl.at/fvP24)
    case : {1, 2}, optional
        1 indicates we are trying to map from one of the available data sources. 2 indicates 
        we are trying to map from a local identifier to a different data source using a pre-defined
        mapping (e.g. we have a local identifier mapped to Ensembl and we want to use BridgeDb to 
        map the local identifier to Entrez)
    target : str, optional
        Specifies the name of the data source to which we want to map our `source` dataset. If ''
        all possible mappings will be returned
        
    Returns
    -------
    result_df : pandas DataFrame
        DataFrame containing the mappings in an easier to read and modify format 
    
    
    """
    
    if len(target) > 0:
        target = '?dataSource='+target
    
    names = ['source']
        
    if case == 2:
        names = ['local'] + names
        
    data = pd.read_csv(file, sep='\t', header=None, names=names)
    
    response = requests.post(batch_request.format(target, org=org, source=source), data = data.source.to_csv(index=False, header=False))
    mapping = to_df(response, batch=True)
    
    if case == 2: 
        return mapping.join(data.set_index('source'), on='original')
    else:
        return mapping
        

