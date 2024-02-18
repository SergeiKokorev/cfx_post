from __future__ import annotations

from typing import Sequence


class Interface:

    def __init__(self, interface: str):
        self._interface = interface

    @property
    def interface(self):
        return self._interface

    @interface.setter
    def interface(self, interface: str):
        if not isinstance(interface, str):
            raise TypeError(f'Unsupported interface type. Need' \
                f'\'str\' type, given {type(interface)}')

    def __str__(self):
        return self._interface


class Domain:

    def __init__(self, domain: str, interfaces: Sequence[Interface] = []):
        self._domain = domain
        self._interfaces = interfaces

    @property
    def interfaces(self) -> Sequence[str]:
        return [interface.interface for interface in self._interfaces]

    @property
    def domain(self) -> str:
        return self._domain
    
    @domain.setter
    def domain(self, domain: str) -> None:
        if not isinstance(domain, str):
            raise TypeError(f'Unsupported type for domain.' \
                'Allowed signature \'str\', given {type(domain)}')
        self._domain = domain

    def get_interfaces(self) -> Sequence[Interface]:
        return self._interfaces

    def add(self, interface: Interface) -> None:

        if not isinstance(interface, Interface):
            error = f'Unsupported interface type. ' \
                f'Support type interface Interface, given {type(interface)}'
            raise TypeError()
        self._interfaces.append(interface)

    def delete(self, idx: int) -> None:

        try:
            self._interfaces.pop(idx)
        except IndexError as er:
            raise IndexError(er)
        except TypeError as er:
            raise TypeError(er)

    def data(self) -> dict:
        return {self._domain: self.interfaces}

    def __str__(self) -> str:
        out = f'{self._domain}\n'

        for interface in self.interfaces:
            out += f'\t{interface}\n'

        return out


class DomainCash:

    _cash = []

    def add(self, domain: Domain) -> bool:
        
        if not isinstance(domain, Domain):
            raise TypeError('Unsupported domain type')
        self._cash.append(domain)

        return True

    def delete(self, idx: int) -> Domain:

        if not isinstance(index, int):
            raise TypeError(f'Unsupported type for domain index.')
        if index > len(self._cash):
            raise IndexError(f'Index {index} out of range. Domain axis {len(self._cash)}')

        return self._cash.pop(index)

    def __str__(self):
        out = ''
        for dmn in self._cash:
            out += str(dmn)
        
        return out
