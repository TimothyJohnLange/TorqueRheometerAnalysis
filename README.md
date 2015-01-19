Kinetic analysis of Gear Rheometer results
==========================================

These files can be used to analyse the results of tests on a compounder Gear Rheometer.

Instructions
------------

1. Insert the directory for the data on your machine in the config_sample.json file and change the name of the file to config.json

2. Calculate the mean and standard deviation of the torque and temperature data using the 'Calculation_mean_std.ipynb' ipython notebook

3. Insert the calculated mean and standard deviation in to the joined_curves function in the 'curve_func_2.py' file where indicated

4. The limits for the parameters can be set using the first function in the 'model_parameters.py' file. The parameters to be varied can also be set here

5. The fitting routine runs with the 'Fit_parameters_to_multi_files.ipynb' ipython notebook. Simply run the code which outputs a PDF with figures of all the fits and a CSV file with the fitted parameters and other relevant information. The PDF and CSV file names (ie 'all_curves_.pdf' or 'all_parameters_.csv) can be renamed as required  