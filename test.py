from tools import get_data
from models import Domain, Interface, DomainCash


FILE = r'indata/res_004.out'


def main():

    domains = DomainCash()

    for dmn, interfaces in get_data(FILE).items():

        bnd = [Interface(i) for i in interfaces]
        d = Domain(dmn, bnd)
        domains.add(d)
    
    print(domains)

if __name__ == "__main__":

    main()
