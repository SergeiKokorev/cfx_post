import re


def get_data(fname: str) -> dict:

    dmn_pattern = re.compile(r'domain:[\s\w\d]*')
    bnd_pattern = re.compile(r'boundary:[\s\w\d]*')
    end_dmn = re.compile(r'domain\smodel:\s')

    dmn_found = False
    domains = {}    

    with open(fname, 'r') as f:

        for line in f.readlines():

            if re.fullmatch(pattern=dmn_pattern, string=line.lower().strip()):
                dmn = line.split(':')[1].strip()
                domains[dmn] = []
                dmn_found = True
            if dmn_found:
                if re.fullmatch(pattern=bnd_pattern, string=line.lower().strip()):
                    bnd = line.split(':')[1].strip()
                    domains[dmn].append(bnd)
            if re.fullmatch(pattern=end_dmn, string=line.lower().strip()):
                dmn_found = False
    
    return domains
