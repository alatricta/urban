default_sender = "university.help@gmail.com"

def send_email(message: str, 
                recipient: str, 
                *, sender = default_sender):
                
    if '@' not in recipient or \
        '@' not in sender or \
        not recipient.endswith(('.com', '.ru', '.net')) or \
        not sender.endswith(('.com', '.ru', '.net')):
        
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
        
    elif sender == default_sender:
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
        
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на {recipient}.')
        
    
if __name__ == '__main__':
    send_email('blablabla', 'pupkin@gmail.com')
    send_email('blablabla', 'pupkin@gmail.ru')
    send_email('blablabla', 'pupkin@gmail.net')
    send_email('blablabla', 'pupkin@gmail.biz')
    send_email('blablabla', 'pupkin@gmail.com', sender='zabor@ograda.net')
    send_email('blablabla', 'pupkin@gmail.com', sender='zabor@ograda.biz')
    send_email('blablabla', 'pupkin@gmail.com', sender='pupkin@gmail.com')
    