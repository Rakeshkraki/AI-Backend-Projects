#without fixture
# def test_user_name():
#     user = {
#         "id": 1,
#         "name": "Rakesh",
#         "email": "rakesh@example.com"
#     }
#
#     assert user["name"] == "Rakesh"
#
#
# def test_user_email():
#     user = {
#         "id": 1,
#         "name": "Rakesh",
#         "email": "rakesh@example.com"
#     }
#
#     assert user["email"] == "rakesh@example.com"
# #with fixture

def test_user_name(user):
    assert user["name"] == "Rakesh"


def test_user_email(user):
    assert user["email"] == "rakesh@example.com"