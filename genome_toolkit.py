class genomeToolkit:
    def __init__(self):
      print("genome toolkit initiated")

    def count_kmer(self, sequence, kmer):
        """Counts the number of times a specific k-mer appears in a 
        given sequence, including overlapping k-mers.
        
        Parameters:
            sequence (str): the DNA sequence being searched.
            kmer (str): The specific k-mer being searched for.
        
        Returns:
            int: the number of times k-mer appears in the sequence.
        """
        kmer_count = 0
        for position in range(len(sequence) - len(kmer) + 1):
            if sequence[position:position + len(kmer)] == kmer:
                kmer_count += 1
        return kmer_count

    def find_most_frequent_kmers(self, sequence, k_len):
        """
        Finds the most frequent k-mers in a DNA string.

        Parameters:
            sequence (str): the DNA being searched in.
            k_len (int): the length of k_mers to search for
        
        Returns:
            list: a list of the most frequent k-mers in the DNA string.
        """
        # creates a dictionary to store k-mer frequencies.
        kmer_frequencies = {}

        #loops to iterate through DNA string and extract k-mers
        # of fixed length, updating frequencies in the dictionary.
        for i in range(len(sequence) - k_len + 1):
            kmer = sequence[i: i + k_len]
            if kmer in kmer_frequencies:
                kmer_frequencies[kmer] += 1
            else:
                kmer_frequencies[kmer] = 1
        pass

        #stores the highest frequency kmer in the dictionary
        highest_frequency = max(kmer_frequencies.values())

        return [
            kmer for kmer, frequency in kmer_frequencies.items()
            if frequency == highest_frequency
        ]
        
