def overzicht(codes):
  overzicht = {}
  overzicht = {
    'Engelstalige landen': 0,
    'Franstalige landen': 0,
    'Duitstalige landen': 0,
    'Japan': 0,
    'Russischtalige landen': 0,
    'China': 0,
    'Overige landen': 0,
    'fouten': 0,
}
  for code in codes:
    groep = code[3]
    if code.startswith('978') or code.startswith('979'):
      if groep == '0' or groep == '1':
        overzicht['Engelstalige landen'] += 1
      elif groep == '2':
        overzicht['Franstalige landen'] += 1
      elif groep == '3':
        overzicht['Duitstalige landen'] += 1
      elif groep == '4':
        overzicht['Japan'] += 1
      elif groep == '5':
        overzicht['Russischtalige landen'] += 1
      elif groep == '7':
        overzicht['China'] += 1
      else:
        overzicht['Overige landen'] += 1
    else:
      overzicht['fouten'] += 1

  for k, v in overzicht.items():
    print(f'{k}: {v}')



codes = [
    '9789743159664', '9785301556616', '9797668174969', '9781787559554',
    '9780817481461', '9785130738708', '9798810365062', '9795345206033', 
    '9792361848797', '9785197570819', '9786922535370', '9791978044523', 
    '9796357284378', '9792982208529', '9793509549576', '9787954527409', 
    '9797566046955', '9785239955499', '9787769276051', '9789910855708', 
    '9783807934891', '9788337967876', '9786509441823', '9795400240705', 
    '9787509152157', '9791478081103', '9780488170969', '9795755809220', 
    '9793546666847', '9792322242176', '9782582638543', '9795919445653', 
    '9796783939729', '9782384928398', '9787590220100', '9797422143460', 
    '9798853923096', '9784177414990', '9799562126426', '9794732912038', 
    '9787184435972', '9794455619207', '9794270312172', '9783811648340', 
    '9799376073039', '9798552650309', '9798485624965', '9780734764010', 
    '9783635963865', '9783246924279', '9797449285853', '9781631746260', 
    '9791853742292', '9781796458336', '9791260591924', '9789367398012' 
]


overzicht(codes)

