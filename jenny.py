
import csv
import argparse

parser = argparse.ArgumentParser(
	description='Username conversion tool.'
	' Convert a CSV file formatted as First,Last to any option.'
	' Automatically converts all text to lowercase.')
'''
Input file.
'''
parser.add_argument('--file', type=str, action='store', required=True, 
						help='names_file.csv')
'''
Keep list capitalization as is.
'''
parser.add_argument('--nocap', action="store_true", required=False,
					help='Maintains capitalizion of CSV file. Does not convert to all lowercase.')
'''
Eventual option to add Output to file option.
'''
#parser.add_argument("-out", action='store', 
#                    type=argparse.FileType('w'), dest='output',
#                    help="Directs the output to a name of your choice")
'''
Eventual option to add @domain.xyz to outputs.
'''
#parser.add_argument('--domain', metavar='@domain.x', type=str, action='store', required=False,
#						help='Append @doman.x to every username.')



#name_parser = parser.add_mutually_exclusive_group(required=True)
'''
Below here are the first last syntax options.
'''
parser.add_argument('--first-last', action="store_true", required=False,
					help='first.last')
parser.add_argument('--f-last', action="store_true", required=False,
					help='f.last')
parser.add_argument('--first-l', action="store_true", required=False,
					help='first.l')
parser.add_argument('--fir-las', action="store_true", required=False,
					help='fir.las')
parser.add_argument('--firstlast', action="store_true", required=False,
					help='firstlast')
parser.add_argument('--firlas', action="store_true", required=False,
					help='firlas')
parser.add_argument('--flast', action="store_true", required=False,
					help='flast')
'''
Below here are the last first syntax options.
'''
parser.add_argument('--last-first', action="store_true", required=False,
					help='last.first')
parser.add_argument('--l-first', action="store_true", required=False,
					help='l.first')
parser.add_argument('--last-f', action="store_true", required=False,
					help='last.f')
parser.add_argument('--las-fir', action="store_true", required=False,
					help='las.fir')
parser.add_argument('--lastfirst', action="store_true", required=False,
					help='lastfirst')
parser.add_argument('--lasfir', action="store_true", required=False,
					help='lasfir')
parser.add_argument('--lfirst', action="store_true", required=False,
					help='lfirst')
parser.add_argument('--lastttttttf', action="store_true", required=False,
					help='lastttttttf')
'''
Kitchen Sink option.
'''
parser.add_argument('--sink', action="store_true", required=False,
					help='Returns formatted username list using all options. This creates 12 versions of each name.')

args = parser.parse_args()

#	return args

def opencsv(file):
    dict = []
    with open(file, 'r', encoding='utf-8-sig') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
        	dict.append([row[0],row[1]])
    return dict

def main():
	dict = opencsv(args.file)
#	if args.nocap == True:
#			for row in dict:
#				first = row[0]()
#				last = row[1]()
#	elif args.nocap == False:
	for row in dict:
		first = row[0].lower()
		last = row[1].lower()
# first,last conversions:

		#First.Last
		if args.first_last == True:
			print(first + "." + last)
		#F.Last
		if args.f_last == True:
			print(first[0] + "." + last)
		#First.L
		if args.first_l == True:
			print(first + "." + last[0])
		#Fir.Las
		if args.fir_las == True:
			print(first[0:3] + "." + last[0:3])
		#FirstLast
		if args.firstlast == True:
			print(first + last)
		#FirLas
		if args.firlas == True:
			print(first[0:3] + last[0:3])
		#FLast
		if args.flast == True:
			print(first[0] + last)

# last,first conversions:

		#Last.First
		if args.last_first == True:
			print(last + "." + first)
		#L.First
		if args.l_first == True:
			print(last[0] + "." + first)
		#Last.F
		if args.last_f == True:
			print(last + "." + first[0])
		#Las.Fir
		if args.las_fir == True:
			print(last[0:3] + "." + first[0:3])
		#LastFirst
		if args.lastfirst == True:
			print(last + first)
		#LasFir
		if args.lasfir == True:
			print(last[0:3] + first[0:3])
		#LFirst
		if args.lfirst == True:
			print(last[0] + first)
		#lasttttf
		if args.lastttttttf == True:
			print(last[0:7] + first[0])

# Kitchen Sink option:
		#First.Last
		if args.sink == True:
			print(first + "." + last)
		#F.Last
		if args.sink == True:
			print(first[0] + "." + last)
		#First.L
		if args.sink == True:
			print(first + "." + last[0])
		#Fir.Las
		if args.sink == True:
			print(first[0:3] + "." + last[0:3])
		#FirstLast
		if args.sink == True:
			print(first + last)
		#FirLas
		if args.sink == True:
			print(first[0:3] + last[0:3])
		#FLast
		if args.sink == True:
			print(first[0] + last)
		#Last.First
		if args.sink == True:
			print(last + "." + first)
		#L.First
		if args.sink == True:
			print(last[0] + "." + first)
		#Last.F
		if args.sink == True:
			print(last + "." + first[0])
		#Las.Fir
		if args.sink == True:
			print(last[0:3] + "." + first[0:3])
		#LastFirst
		if args.sink == True:
			print(last + first)
		#LasFir
		if args.sink == True:
			print(last[0:3] + first[0:3])
		#LFirst
		if args.sink == True:
			print(last[0] + first)

#output_file = args.out
#if args.out == True:
#	output_file.write()

if __name__ == "__main__":
    main()
