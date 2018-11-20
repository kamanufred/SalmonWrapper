#!/usr/bin/env python

import sys
import os
import itertools
from optparse import OptionParser

#fastq main class
#-----------------------------------------------------------------------------------------
class RNASeq(object):
	"""
	Class that initialized parameters and runs RNASeq QC and abundance quantification
	"""

	def __init__(self,inread1,inread2,outread1,outread2,index,cores,resultDir):
		"""
		Initialize the user-defined parameters for the analysis
		"""
		self.inread1 = inread1
		self.inread2 = inread2
		self.outread1 = outread1
		self.outread2 = outread2
		self.index = index
		self.cores = cores
		self.resultDir = resultDir
		os.mkdir(self.resultDir)

	def RunFastp(self):
		"""
		Run fastq with basic options
		"""
		res_json = self.resultDir + ".json"
		res_html = self.resultDir + ".html"
		os.system("fastp -i %s -I %s -o %s -O %s -j %s -h %s" % \
				 (self.inread1,self.inread2,self.outread1, \
				  self.outread2,res_json,res_html))
		
		#clean up
		os.system("mv %s %s %s %s %s" % (res_json, res_html,\
										 self.outread1, self.outread2, self.resultDir))
		
		return

	def RunSalmon(self):
		"""
		Run Salmon with basic options
		"""
		read1 = self.resultDir + "/" + self.outread1
		read2 = self.resultDir + "/" + self.outread2
		salmon_out = self.resultDir + "_salmon"
		os.system("salmon quant -p %s -i %s -l A -1 %s -2 %s -o %s " % \
				  (self.cores,self.index,read1,read2,salmon_out))
		#clean up
		os.system("mv %s %s " % (salmon_out,self.resultDir))





#Setting commandline options
#-----------------------------------------------------------------------------------------
def commandline_options():
	"""
	Commandline arguments input
	"""
	parser = OptionParser(usage="usage: %prog [options]")
	parser.add_option("-i", "--read1",
					  type="string",
					  dest="read1",
					  help="First read pair file")
	parser.add_option("-I", "--read2",
						type="string",
						dest="read2",
						help="Second read pair file")
	parser.add_option("-o", "--read1_out",
						type="string",
						dest="read1_out",
						help="First read pair file after qc")
	parser.add_option("-O", "--read2_out",
						type="string",
						dest="read2_out",
						help="Second read pair file after qc")
	parser.add_option("-g", "--genomeIndex",
						type="string",
						dest="index",
						help="Genome index")
	parser.add_option("-n", "--cores",
						type="string",
						dest="cores",
						help="Number of threads")
	parser.add_option("-r", "--results",
						type="string",
						dest="results",
						help="Results Directory")

	(options, args) = parser.parse_args()
	options_args_parser = [options,args,parser]

	return options_args_parser


#Main
#-----------------------------------------------------------------------------------------
def main():
	options, args, parser = commandline_options()
	read1 = options.read1
	read2 = options.read2
	read1_out = options.read1_out
	read2_out = options.read2_out
	index = options.index
	cores = options.cores
	resultDir = options.results
	
	wrapper_object = RNASeq(read1,read2,read1_out,read2_out,index,cores,resultDir)
	wrapper_object.RunFastp()
	wrapper_object.RunSalmon()


#Execute main
#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
	main()


