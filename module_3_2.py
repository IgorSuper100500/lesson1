def send_email(message, recipient, sender="university.help@gmail.com"):
    if recipient.count('@') and (recipient.count('.com') or recipient.count('.ru') or recipient.count('.net')):

        if sender.count('@') and (sender.count('.com') or sender.count('.ru') or sender.count('.net')):
            if sender == recipient:
                print('Нельзя отправить письмо самому себе!')
            else:
                if sender != 'university.help@gmail.com':
                    print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса ', sender, ' на адрес ',
                          recipient)
                else:
                    print(f'Письмо успешно отправлено с адреса ', sender, ' на адрес ', recipient)
        else:
            print(f'Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)
    else:
        print(f'Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
