# Simple sentence parser
Parses a sentence using predefined terminals and non-terminals.

## Usage
Install requirements using,
```
pip install -r requirements.txt
```
Run the program by,
```
python parser.py [txt_file]
```

## Sample use
```
python parser.py sentences/10.txt
```
10.txt contains
```
I had a little moist red paint in the palm of my hand.
```
This outputs
```
              S
  ____________|______________________
 |                                   VP
 |    _______________________________|____
 |   |                                    NP
 |   |                          __________|____________________
 |   |                         NP                              |
 |   |                _________|______________                 |
 |   |               NP                       |                |
 |   |    ___________|_______________         |                |
 |   |   |          AdjP             |        |                |
 |   |   |     ______|____           |        |                |
 |   |   |    |          AdjP        |        PP               PP
 |   |   |    |       ____|____      |     ___|___          ___|___
 NP  |   |    |      |        AdjP   |    |       NP       |       NP
 |   |   |    |      |         |     |    |    ___|___     |    ___|___
 N   V  Det  Adj    Adj       Adj    N    P  Det      N    P  Det      N
 |   |   |    |      |         |     |    |   |       |    |   |       |
 i  had  a  little moist      red  paint  in the     palm  of  my     hand

Noun Phrase Chunks
i
a little moist red paint
the palm
my hand
              S
  ____________|______________________
 |                                   VP
 |    _______________________________|____
 |   |                                    NP
 |   |                ____________________|___________
 |   |               NP                               PP
 |   |    ___________|_______________      ___________|____
 |   |   |          AdjP             |    |                NP
 |   |   |     ______|____           |    |        ________|___
 |   |   |    |          AdjP        |    |       |            PP
 |   |   |    |       ____|____      |    |       |         ___|___
 NP  |   |    |      |        AdjP   |    |       NP       |       NP
 |   |   |    |      |         |     |    |    ___|___     |    ___|___
 N   V  Det  Adj    Adj       Adj    N    P  Det      N    P  Det      N
 |   |   |    |      |         |     |    |   |       |    |   |       |
 i  had  a  little moist      red  paint  in the     palm  of  my     hand

Noun Phrase Chunks
i
a little moist red paint
the palm
my hand
```