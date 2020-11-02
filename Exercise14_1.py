def sed(pattern, replace, file1, file2): #define function with four input parameters
    source=open(file1, 'r') #reads the first file into a string variable
    result=open(file2, 'w') #writes the results into an existing file, or creates it if it doesnt exist
    #print(type(result)) #debug statement
    
    for line in source:
        line = line.replace(pattern, replace) #for every time the 'pattern' string appears in source file, replace it with the 'replace' string
        result.write(line) #appends the replacement string to the result file
    
    source.close() #close the files so result can be displayed without ending the notebook experiment
    result.close() 
    
    test_the_file=open('file2.txt').read() #open the newly created (or modified) file
    #print(type(test_the_file)) debug statement for sanity check
    print(test_the_file) 




