from functions.level_4.two_students import get_student_by_tg_nickname


def test__get_student_by_tg_nickname__with_match(students, create_student):
    matched_student = create_student(telegram_account='@ivan-ivanov')
    assert get_student_by_tg_nickname(telegram_username='ivan-ivanov', students=students) == matched_student


def test__get_student_by_tg_nickname__no_matched_students(students):
    assert get_student_by_tg_nickname(telegram_username='vanya_ivanov', students=students) is None


def test__get_student_by_tg_nickname__no_students_with_tg_account(create_student):
    students = [create_student()]
    assert get_student_by_tg_nickname(telegram_username='vanya_ivanov', students=students) is None
