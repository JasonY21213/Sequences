class FastaParser:
    def __init__(self, filename):
        self._filename = filename

    @property
    def filename(self):
        return self._filename

    def read_fasta(self, sequence_class):
        with open(self.filename, 'r') as file:
            seq_id = None
            sequence = ''

            for line in file:
                line = line.rstrip()
                if line.startswith('>'):
                    if seq_id is not None:                  # 如果已经保存了一个 seqid，就先把已保存的上两行的 seqid 和 seq 序列传给外部代码
                        yield sequence_class(seq_id, sequence)
                    seq_id = line[1:]                       # 保存新的 seqid 并重置 seq 序列
                    sequence = ''
                else:
                    sequence += line                        # 如果不是 > 开头，就保存成 seq 序列
            if seq_id is not None:                          # 处理最后一条序列
                yield sequence_class(seq_id, sequence)