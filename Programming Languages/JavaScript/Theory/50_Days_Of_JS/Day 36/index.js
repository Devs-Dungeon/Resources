const transcription = (dna) => {
	// code here
    let rna='';
    for(let i=0;i<dna.length;i++)
    {
        if(dna[i]==='G') rna += 'C';
        else if(dna[i]==='C') rna += 'G';
        else if(dna[i]==='T') rna += 'A';
        else rna += 'U';
    }
	return rna;
}
