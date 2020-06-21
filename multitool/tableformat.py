# tableformat.py


class TableFormatter:
    def headings(self, headers):
        '''
        Output the table headings
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Output single row of table data
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    '''
    Output data in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')


class MDTableFormatter(TableFormatter):
    '''
    Output data in GH Markdown format
    '''
    def headings(self, headers):
        for x, h in enumerate(headers):
            if (x == 0):
                print(f'{h} ', end='')
            else:
                print(f'| {h} ', end='')
        print()
        for i, h in enumerate(headers):
            if (i == 0):
                print('-'*len(h) + ' ', end='')
            else:
                print('| ' + '-'*len(h) + ' ', end='')
        print()

    def row(self, rowdata):
        for x, row in enumerate(rowdata):
            if (x == 0):
                print(f'{row} ', end='')
            else:
                print(f'| {row} ', end='')
        print()


def create_formatter(name):
    '''Create formatter object in specified format'''
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    elif name == 'md':
        return MDTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')


def print_table(data, headers, formatter):
    '''Generic table formatting function using formatters'''
    formatter.headings(headers)
    for obj in data:
        rowdata = [str(getattr(obj, name)) for name in headers]
        formatter.row(rowdata)


class FormatError(Exception):
    pass
