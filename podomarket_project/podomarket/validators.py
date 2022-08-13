import string
from django.core.exceptions import ValidationError

# 아래에 작성된 함수들은 각각 해당하는 글자가 포함되어 있는지 확인하는 함수.
# 유효성 검사를 통해 오류를 출력하는 내용은 따로 작성해야 한다.

def contains_special_characters(value):
    for char in value:
        if char in string.punctuation:
            return True    
    return False
        
def contains_uppercase_letter(value):
    for char in value:
        if char.isupper():
            return True
    return False

def contains_lowercase_letter(value):
    for char in value:
        if char.islower():
            return True
    return False

def contains_number(value):
    for char in value:
        if char.isdigit():
            return True
    return False


# 특수문자를 허용하지 않는 유효성 검사 함수

def validate_no_special_characters(value):
    if contains_special_characters(value):
        raise ValidationError("특수문자는 포함할 수 없음")
    
# 비밀번호 내용 제한하는 유효성 검사 함수    
# 비밀번호 내용 유효성 검사 함수의 적용은 settings.py에서 설정해야 한다.

class CustomPasswordValidator:
    # 8자 이상, 영문 대/소문자, 숫자 포함
    def validate(self, password, user=None):
        if (
            len(password) < 8 or
            not contains_uppercase_letter(password) or
            not contains_lowercase_letter(password) or
            not contains_number(password)
        ):
            raise ValidationError("8자 이상이며 영문 대/소문자, 숫자를 포함해야 합니다.")
    
    def get_help_text(self): # 해당 메소드는 admin 페이지에서 비밀번호 바꿀 때 사용
        return "8자 이상이며 영문 대/소문자, 숫자를 포함해야 합니다."