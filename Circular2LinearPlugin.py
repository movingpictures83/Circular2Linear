import PyPluMA

class Circular2LinearPlugin:
    def input(self, filename):
       params = open(filename, 'r')
       self.parameters = dict()
       for line in params:
          contents = line.strip().split('\t')
          self.parameters[contents[0]] = contents[1]
       self.fasta = PyPluMA.prefix()+"/"+self.parameters["fasta"]
       self.start = int(self.parameters["start"])  #Assuming indexing is from 1

    def run(self):
       fastafile = open(self.fasta, 'r')
       self.header = fastafile.readline().strip()
       DNA = ''
       for line in fastafile:
           DNA += line.strip()
       print(DNA[9390:9993])
       firstpart = DNA[self.start-1:]
       secondpart = DNA[:self.start-1]
       self.linDNA = firstpart+secondpart
       print(len(self.linDNA))


    def output(self, filename):
       outfile = open(filename, 'w')
       outfile.write(self.header+"\n")
       outfile.write(self.linDNA)
