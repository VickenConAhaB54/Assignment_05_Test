import os
import numpy
from numpy import max
import numpy as np
from numpy import average
def average_inflammations(patient_id, file_name='inflammation-01.csv'):
    '''
    Return the average number of inflammations for a patient in a data file.
    patient_id -- id of the patient
    file_name  -- data file name, must be under directory 'data'
    '''

    # Concatenate directory name with file name
    data_dir = 'C:/users/Dell/Documents/GitHub/python-homework-5/data'
    complete_file_name = os.path.join(data_dir, file_name)

    # Load data
    inflammations = np.loadtxt(fname=complete_file_name, delimiter=',')

    # Compute and return the average
    avg = numpy.average(inflammations[patient_id])
    return avg
def max_inflammations(patient_id, file_name='inflammation-01.csv'):
    '''
    Return the max number of inflammations for a patient in a data file;
    patient_id -- id of the patient
    file_name  -- data file name, must be under directory 'data'
    '''

    # Concatenate directory name with file name
    data_dir = 'C:/users/Dell/Documents/GitHub/python-homework-5/data'
    complete_file_name = os.path.join(data_dir, file_name)

    # Load data
    inflammations = np.loadtxt(fname=complete_file_name, delimiter=',')

    # Compute and return the max
    Max = numpy.max(inflammations[patient_id])
    return Max
def acute_patient(file_name='inflammation-01.csv'):
    '''
    Return the id of the patient with the highest average number of 
    inflammations in the dataset.
    patient_id -- id of the patient
    file_name  -- data file name, must be under directory 'data'
    '''

    data_dir = 'C:/users/Dell/Documents/GitHub/python-homework-5/data'
    complete_file_name = os.path.join(data_dir, file_name)

    # Load data
    SDAR = np.loadtxt(fname=complete_file_name, delimiter=',')

    # Compute and return the averagepython-homework-5
    a=np.array (SDAR)
    b= average(a, axis=1)
    Cal = b.argmax()
    return Cal