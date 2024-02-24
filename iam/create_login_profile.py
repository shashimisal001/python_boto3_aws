import boto3


def create_login_profile(username, password):
    """
    This function creates login profile to only an existing user and not
    new user with profile
    """
    iam = boto3.client("iam")
    res = iam.create_login_profile(
        UserName=username,
        Password=password,
        PasswordResetRequired=False
    )
    print(res)


create_login_profile("test_user", "Sam3@belgaum")
