# SalmonWrapper
A pipeline that runs the fastp tool, for basic QC and data statistics, and also runs salmon for abundance quantification. Both software are executed with the very basic commandline options. Feel free to edit and add more.



#Requirements
- [Fastp](https://github.com/OpenGene/fastp)
- [Salmon](https://combine-lab.github.io/salmon/)

#Installation
\- Checkout the source: `git clone https://github.com/kamanufred/SalmonWrapper.git`  

#Usage
Run `python SalmonWrapper.py -h` to see all the options.  

	Usage: SalmonWrapper.py [options]

	Options:
  		-h, --help            show this help message and exit
  		-i READ1, --read1=READ1
                        First read pair file
  		-I READ2, --read2=READ2
                        Second read pair file
  		-o READ1_OUT, --read1_out=READ1_OUT
                        First read pair file after qc
  		-O READ2_OUT, --read2_out=READ2_OUT
                        Second read pair file after qc
  		-g INDEX, --genomeIndex=INDEX
                        Genome index
  		-n CORES, --cores=CORES
                        Number of threads
  		-r RESULTS, --results=RESULTS
                        Results Directory

#Contact
Contact `frederick(dot)kamanu(at)gmail.com` for feedback regarding the software.  

#License    
This software is provided under the GNU General Public License. See the included file.
