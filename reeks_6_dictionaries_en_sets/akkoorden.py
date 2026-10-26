def ontleding_fout(akkoord):
  startcijfer = -1

  if (len(akkoord) > 1 and akkoord[1] == '#'):
    grondnoot = akkoord[:2]
    startcijfer = 2
  else:
    grondnoot = akkoord[:1]
    startcijfer = 1


  if (akkoord[startcijfer:] == ''):
    return (grondnoot, 'majeur')
  else:
    if (akkoord[startcijfer:] == 'm'):
      return (grondnoot, 'mineur')
    if (akkoord[startcijfer:] == '7'):
      return (grondnoot, 'dominant septiem')
    if (akkoord[startcijfer:] == 'm7'):
      return (grondnoot, 'mineur septiem')
    if (akkoord[startcijfer:] == 'M7'):
      return (grondnoot, 'majeur septiem')


def ontleding(akkoord):
  startcijfer = -1
  
  if (len(akkoord) > 1 and akkoord[1] == '#'):
    grondnoot = akkoord[:2]
    startcijfer = 2
  else:
    grondnoot = akkoord[:1]
    startcijfer = 1

  return (grondnoot, akkoord[startcijfer:])


def noten(grondnoot, lijstIntervallen):
  alleTonen = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

  akkoord = []

  startInterval = alleTonen.index(grondnoot)
  for interval in lijstIntervallen:
    akkoord.append(alleTonen[((startInterval + interval) % len(alleTonen))])

  return akkoord

def akkoord(verkortAkkoord, akkoordTypes, akkoordSymbolen):
  grondnoot, akkoordType = ontleding(verkortAkkoord)

  intervallen = akkoordTypes[akkoordSymbolen[akkoordType]]

  return tuple(noten(grondnoot, intervallen))



print(ontleding('F'))
print(ontleding('Gm7'))
print(ontleding('D#M7'))


print(noten('F', [0, 4, 7]))
print(noten('G', [0, 3, 7, 10]))
print(noten('D#', [0, 4, 7, 11]))


akkoordtypes = {'majeur':[0, 4, 7], 'mineur':[0, 3, 7], 'dominant septiem':[0, 4, 7, 10], 'mineur septiem':[0, 3, 7, 10], 'majeur septiem':[0, 4, 7, 11]}

akkoordsymbolen = {'':'majeur', 'm':'mineur', '7':'dominant septiem', 'm7':'mineur septiem', 'M7':'majeur septiem'}

print(akkoord('F', akkoordtypes, akkoordsymbolen))
print(akkoord('Gm7', akkoordtypes, akkoordsymbolen))
print(akkoord('D#M7', akkoordtypes, akkoordsymbolen))

