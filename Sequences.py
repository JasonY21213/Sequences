# creat a supperclass
class Sequence:
    def __init__(self, id, seq):
        self._id = id
        self._seq = seq.upper()

    def __str__(self):
        return f'Sequence object: ID; {self.id}, Seq; {self.seq}'

    def __len__(self):
        return len(self.seq)

    def __iter__(self):
        return iter(self.seq)

    @property
    def id(self):
        return self._id

    @property
    def seq(self):
        return self._seq

    def make_fasta(self):
        return f'>{self.id}\n{self.seq}\n'

# creat the protein sequence class
class ProteinSequence(Sequence):
    def __init__(self, id, seq, descr = ''): # describe 默认值
        super().__init__(id, seq)
        self._descr = descr

    @property
    def descr(self):
        return self._descr
    
    def calc_hydrophobic_content(self, dp=2):
        hydrophobic = 'AILMFWYV'
        count = sum(self.seq.count(aa) for aa in hydrophobic)
        return round(count / len(self.seq) * 100, dp)

    def get_protein_len(self):
        return len(self.seq)

# create the DNA sequence class
class DNASequence(Sequence):
    # gc content method
    def calc_gc_content(self, dp=2):
        c_count = self.seq.count('C')
        g_count = self.seq.count('G')
        gc_content = (c_count + g_count) / len(self.seq)
        return round(gc_content, dp)

    # translation method
    def translate_cds(seq):
        bases = "tcag".upper()
        codons = [a + b + c for a in bases for b in bases for c in bases]
        amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
        codon_table = dict(zip(codons, amino_acids))
        seq = seq.upper()
        protein = ''

        for i in range(0, len(seq), 3):
            codon = seq[i:i+3]
            if len(codon) == 3:
                protein += codon_table[codon]

        return protein

    def get_protein_len(self):
        return len(self.seq) // 3