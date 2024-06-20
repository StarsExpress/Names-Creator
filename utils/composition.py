from utils.candidates import select_surnames
from creation.surname_creation import SurnameCreator
from creation.forename_creation import ForenameCreator
import time


surname_creator = SurnameCreator()
forename_creators_dict = {
    'male': ForenameCreator('male'),
    'female': ForenameCreator('female'),
}


# Create names upon called by Streamlit app.
def make_creations(
        names_num: int,
        creativity: int = None,
        gender: str = 'female',
        target: str = 'remix',
):
    start = time.time()
    surnames, forenames = [], []

    if target != 'just_forename':  # If not just forename, surnames must be needed.
        if target == 'remix':  # Select from existing surnames.
            surnames = select_surnames(names_num)

        else:  # If target is just surname or full name, create surnames.
            surnames = surname_creator.create(names_num, creativity)

    if target != 'just_surname':  # If not just surname, forenames must be needed.
        forenames = forename_creators_dict[gender].create(names_num, creativity)

    if target in ['remix', 'full_name']:  # Concat each pair into full name by empty space.
        creations = [forename + ' ' + surname for forename, surname in zip(forenames, surnames)]

    else:  # One of two lists must be empty if target is just surname or forename.
        creations = surnames + forenames

    end = time.time()
    total_time, avg_time = round(end - start, 2), round((end - start) / names_num, 2)
    return creations, total_time, avg_time
