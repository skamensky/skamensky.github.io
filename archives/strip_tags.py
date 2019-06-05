'''
simple command line script to strip script tags from archived html files in order to reduce page load time and remove trackers. Self documenting :)
'''
from bs4 import BeautifulSoup
import argparse
import os

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile", help="path of the file for which you want to strip tags",type=str)
    parser.add_argument("outputfile", help="path of file that will be outputted",type=str)
    parser.add_argument("--tags",nargs='*', help="tags you want to strip. Defaults to 'script'. Input like so (without quotes): '--tags script img style'",type=str,default=['script'])
    parser.add_argument("--encoding",help="html file encoding. Defaults to utf-8",type=str,default='utf-8')
    args = parser.parse_args()
    
    input_file = args.inputfile
    output_file = args.outputfile
    tags = args.tags
    encoding = args.encoding
    
    with open(input_file,encoding=encoding) as html_input_file:
        soup = BeautifulSoup(html_input_file,'html.parser')
        for tag in tags:
            #thanks to https://stackoverflow.com/a/5598705/4188138 for this
            [element.extract() for element in soup.findAll(tag)]
    
    #make parent directory of output file if it doesn't exist
    os.makedirs(os.path.dirname(output_file),exist_ok=True)
    
    with open(output_file,'w+',encoding='utf-8') as html_output_file:
        html_output_file.write(str(soup.html))