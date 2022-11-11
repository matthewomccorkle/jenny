# Why ?


This fork is an update to the AD-Username Generator by w0Tx.

You can find their original project here: [https://github.com/w0Tx/generate-ad-username](https://github.com/w0Tx/generate-ad-username).

I created this as a way to learn Python and also as a method for generating usernames from a CSV file. 
<br>
### Note: Currently outputs all names as lowercase to stdout.
<br>

Future Options:
```
-o : Output the usernames to a file.
--nocap : Maintain capitalization of input CSV file (disable conversion to lowercase).
```

# Install:

```
git clone https://github.com/matthewomccorkle/jenny.git
```

# Usage

### 1 . Format your CSV

CSV file format should have names seperated by commas (,).
**Example CSV:**

```
First,Last
First2,Last2
First3,Last3
```
### 2. Run jenny.py

**Help Menu**
```
python3 jenny.py -h

options:
  -h, --help    show this help message and exit
  -file FILE    names_file.csv
  --first-last  first.last
  --f-last      f.last
  --first-l     first.l
  --fir-las     fir.las
  --firstlast   firstlast
  --firlas      firlas
  --last-first  last.first
  --l-first     l.first
  --last-f      last.f
  --las-fir     las.fir
  --lastfirst   lastfirst
  --lasfir      lasfir
  --sink        Returns formatted username list using all options. This creates 12 versions of each name.
```
**first.last example:**
```
python3 jenny.py -f example.csv --first-last

john.doe
jane.neena
william.smith
julian.asange
```

**specify multiple syntax choices example:**
```
python3 jenny.py --file example.csv --first-last --lasfir --fir-las
john.doe
joh.doe
doejoh
jane.neena
jan.nee
neejan
william.smith
wil.smi
smiwil
julian.asange
jul.asa
asajul
```

**Kitchen Sink example:**  

```
# python3 jenny.py -f example.csv --sink
john.doe
j.doe
john.d
joh.doe
johndoe
johdoe
doe.john
d.john
doe.j
doe.joh
doejohn
doejoh
jane.neena
j.neena
jane.n
jan.nee
janeneena
jannee
neena.jane
n.jane
neena.j
nee.jan
neenajane
neejan
william.smith
w.smith
william.s
wil.smi
williamsmith
wilsmi
smith.william
s.william
smith.w
smi.wil
smithwilliam
smiwil
julian.asange
j.asange
julian.a
jul.asa
julianasange
julasa
asange.julian
a.julian
asange.j
asa.jul
asangejulian
asajul
```

**Redirect output to file**
```
$ python3 jenny.py --file example.csv --first-last >> first.last

$ cat first.last 
john.doe
jane.neena
william.smith
julian.asange
