from ccdc import io

def get_density(refcode):
	csd_reader = io.EntryReader('CSD')
	entry = csd_reader.entry(refcode)

	published_density = entry.calculated_density
#	smiles = entry.molecule.smiles
#	return [refcode, smiles, published_density]
	print(refcode, published_density)

# Since each string might have more than one structures, with 2-digit number, we will try to get them all
name = "CTMTNA"
get_density(name)
for i in range(1,10):
    try:
        get_density(name+"0"+str(i))
    except:
        pass
        
for i in range(11,100):
    try:
        get_density(name+str(i))
    except:
        pass
