from creators.surname_creator import SurnamesCreator
from creators.forenames_creator import ForenamesCreator


def test_creators():
    """Test three creators functionality."""
    num_names, top_k = 5, 10
    surnames_creator = SurnamesCreator()
    female_forenames_creator = ForenamesCreator("female")
    male_forenames_creator = ForenamesCreator("male")

    print(f"Surnames:\n{surnames_creator.create(num_names, top_k)}")
    print(f"\nFemale forenames:\n{female_forenames_creator.create(num_names, top_k)}")
    print(f"\nMale forenames:\n{male_forenames_creator.create(num_names, top_k)}")


if __name__ == '__main__':
    test_creators()
