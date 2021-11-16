import PyPluMA

def complement(DNA):
    DNA_rev = DNA
    DNA_rev = DNA_rev.replace('A', 'Q')
    DNA_rev = DNA_rev.replace('T', 'A')
    DNA_rev = DNA_rev.replace('Q', 'T')
    DNA_rev = DNA_rev.replace('C', 'Z')
    DNA_rev = DNA_rev.replace('G', 'C')
    DNA_rev = DNA_rev.replace('Z', 'G')
    return DNA_rev

class Circular2LinearPlugin:
    def input(self, filename):
       params = open(filename, 'r')
       self.parameters = dict()
       for line in params:
          contents = line.strip().split('\t')
          self.parameters[contents[0]] = contents[1]
       self.fasta = PyPluMA.prefix()+"/"+self.parameters["fasta"]
       self.start = int(self.parameters["start"])  #Assuming indexing is from 1
       if ("reverse" in self.parameters and self.parameters["reverse"] == "true"):
           self.reverse = True
       else:
           self.reverse = False

    def run(self):
       fastafile = open(self.fasta, 'r')
       self.header = fastafile.readline().strip()
       DNA = ''
       for line in fastafile:
           DNA += line.strip()
       print(len(DNA))
       if (not self.reverse):
          print("NOT REVERSING")
          firstpart = DNA[self.start-1:]
          secondpart = DNA[:self.start-1]
          self.linDNA = firstpart+secondpart
       else:
           print("REVERSING")
           firstpart = DNA[:self.start][::-1]
           secondpart = DNA[self.start:][::-1]
           self.linDNA = firstpart+secondpart
           self.linDNA = complement(self.linDNA)
           print(self.linDNA[482:2027])
       #print(len(self.linDNA))
       #print(self.linDNA[:20])

    def output(self, filename):
       outfile = open(filename, 'w')
       outfile.write(self.header+"\n")
       outfile.write(self.linDNA)
