from api import PetFriends
from settings import valid_email, valid_password, invalid_email, invalid_password, correct_filter, incorrect_filter

pf = PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result

def test_get_api_key_for_invalid_user(email=invalid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status >= 400 and status <= 499
    assert 'key' not in result

def test_get_api_key_for_valid_user_with_invalid_pass(email=valid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status >= 400 and status <=499
    assert 'key' not in result

def test_get_api_key_for_no_email(email='', password=invalid_password):
    status, result = pf.get_api_key(email, password)
    assert status >= 400 and status <=499
    assert 'key' not in result

def test_get_api_key_for_valid_user_with_no_pass(email=valid_email, password=''):
    status, result = pf.get_api_key(email, password)
    assert status >= 400 and status <=499
    assert 'key' not in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0

def test_get_all_pets_with_valid_key_incorrect_filter(filter=incorrect_filter):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status != 200
    assert 'pets' not in result

def test_get_all_pets_with_valid_key_correct_filter(filter=correct_filter):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert 'pets' in result


def test_add_new_pet_with_invalid_data(name='Pes', animal_type='dog', age='4', pet_photo=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status != 200
    #assert 'name' in result
