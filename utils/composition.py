from utils.candidates import select_surnames
from creation.surname_creation import SurnameCreator
from creation.forename_creation import ForenameCreator
import time


surname_creator = SurnameCreator()
forename_creators_dict = {'male': ForenameCreator('male'), 'female': ForenameCreator('female')}


# Create names upon called by Streamlit app.
def make_creations(number_of_names, creativity=None, gender='female', target='remix'):
    start = time.time()  # Start time of creation.
    surnames_list, forenames_list = [], []

    if target != 'just_forename':  # If not just forename, surnames must be needed.
        if target == 'remix':  # If target is remix, select from existing surnames.
            surnames_list = select_surnames(number_of_names)

        else:  # If target is just surname or full name, create surnames.
            surnames_list = surname_creator.create(number_of_names, creativity)

    if target != 'just_surname':  # If not just surname, forenames must be needed.
        forenames_list = forename_creators_dict[gender].create(number_of_names, creativity)

    if target in ['remix', 'full_name']:  # Concat each pair into full name by empty space.
        creations_list = [forename + ' ' + surname for forename, surname in zip(forenames_list, surnames_list)]

    else:  # One of two lists must be empty if target is just surname or forename.
        creations_list = surnames_list + forenames_list

    end = time.time()  # End time of creation.
    total_time, avg_time = round(end - start, 2), round((end - start) / number_of_names, 2)
    return creations_list, total_time, avg_time
