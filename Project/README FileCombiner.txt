README FileCombiner.py

To use the file_combiner see instructions below. The file_combiner asks for a string of letters that you want to sort by. For example if you want to sort by SPS or 60' then this will be your input. The file_combiner will take all files that contains that string and place them in a new file called SPS, that you can easily copy and paste into excel or origin. The file names (or column headers) are put in a separate file called 'columnsSPS', or equivalently. The files need to be of same size for the code to work. If you want to run the code again with the same sorting string, you first need to delete the old files, otherwise the code reads them again and since they are a different size the code crashes. The data should have '.' as the decimal. 

---Instructions---
1. place the file of the code ('file_combiner_final.py') in the same folder as the datafiles that you want to combine.
2. enter the terminal or your favourite shell, go to the folder that you want to combine files in.
3. run the code: ' python file_combiner_final.py '
4. enter the name of the folder that you are in. Make sure there are no spaces in the name.
5. enter the sorting string that you want to sort by.
6. Now you should be able to find the files in your folder and copy-paste the contents. 