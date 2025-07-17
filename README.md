Content
=======
This package contains writers for SRU files for the Swedish tax agency
(Skatteverket)
See: SKV 269 Teknisk beskrivning för elektronisk redovisning av Inkomstdeklaration 1 samt bilagor till Inkomstdeklaration 1, 2, 3 och 4

1. infosru.py:
   Writer for info.sru

Example
=======
This example shows how to create a sru file that contains several blanketts.

```python
import sys 
import pandas as pd
import pysru_accounting.infosru as infosru
import pysru_accounting.blankettsru as blankettsru

org = '123456-1234'


df = pd.read_csv(sys.argv[1], skiprows=1)
df = df.set_index('year')

print(df)

#### write the info SRU
p = infosru.InfoSRU ()
p.filename('blanketter.sru')
p.organisation_nr (org)
p.name('Sven Svensson')
p.postcode('12345')
p.town('Stockholm')
p.print ()
p.write('info.sru')

########## INK2

years = df.index

ink2 = blankettsru.BlankettSRU()
for y in years:
    # add INK2 for that year
    ink2.blankett(f'INK2-{y}P4')
    ink2.orgnr(org)
    ink2.name('Sven Svensson')
    ink2.uppgift_num(7011, str(y)+'0101')
    ink2.uppgift_num(7012, str(y)+'1231')
    ink2.uppgift_num(7114, df.loc[y, '7114']) # 1.2 Underskott
    ink2.generate()
    ink2.print()
    ink2.clear_uppgift()

    # add INK2R for that year
    ink2rcodes = [7230, 7281, 7301, 7302, 7513, 7550]
    ink2.blankett(f'INK2R-{y}P4')
    ink2.orgnr(org)
    ink2.name('Sven Svensson')
    ink2.uppgift_num(7011, str(y)+'0101')
    ink2.uppgift_num(7012, str(y)+'1231')

    for code in ink2rcodes:
        ink2.uppgift_num(code, df.loc[y, str(code)])

    ink2.generate()
    ink2.print()
    ink2.clear_uppgift()

    # add INK2S for that year
    ink2scodes = [7750, 7653, 7763, 7770]
    ink2.blankett(f'INK2S-{y}P4')
    ink2.orgnr(org)
    ink2.name('Sven Svensson')
    ink2.uppgift_num(7011, str(y)+'0101')
    ink2.uppgift_num(7012, str(y)+'1231')

    for code in ink2scodes:
        print(code)
        v = df.loc[y, str(code)]
        if not pd.isna(v):
            ink2.uppgift_num(code, df.loc[y, str(code)])

    ink2.generate()
    ink2.print()
    ink2.clear_uppgift()

ink2.write(f'blanketter.sru')



```
