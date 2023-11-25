from utils.candidates import select_surnames
from creation.surname_creation import SurnameCreator
from creation.forename_creation import ForenameCreator
import time


surname_creator = SurnameCreator()
forename_creators_dict = {'male': ForenameCreator('male'), 'female': ForenameCreator('female')}


def make_creations(number, lock, gender='female', preference='remix'):  # Create names upon called by Streamlit app.
    start = time.time()  # Start time of creation.
    surnames_list, forenames_list = [], []

    if preference != 'just_forename':  # If not just forename, surnames must be needed.
        if preference == 'remix':  # If preference is remix, select from existing surnames.
            surnames_list = select_surnames(number)

        else:  # If preference is just surname or full name, create surnames.
            surnames_list = surname_creator.create(number, lock)

    if preference != 'just_surname':  # If not just surname, forenames must be needed.
        forenames_list = forename_creators_dict[gender].create(number, lock)

    if preference in ['remix', 'full_name']:  # Concat each pair into full name by empty space.
        creations_list = [forename + ' ' + surname for forename, surname in zip(forenames_list, surnames_list)]

    else:  # One of two lists must be empty if preference is just surname or forename.
        creations_list = surnames_list + forenames_list

    end = time.time()  # End time of creation.
    total_runtime, avg_runtime = round(end - start, 2), round((end - start) / number, 2)
    return creations_list, total_runtime, avg_runtime
