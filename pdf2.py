from fpdf import FPDF
from fpdf import XPos, YPos
import webbrowser
import random
import os
import math
from num2words import num2words as n2w

# Создание экземпляра документа в формате А4
def invoice_creator(count, tariff, total, inn, legal_name, invoice_no, discount, email):
    INVOICE_NO = invoice_no
    BUYER = legal_name
    TOTAL = total
    PROPIS_TOTAL = n2w(total, lang='ru')
    if math.isnan(inn):
        inn = ''
    else:
        inn = int(inn)

    pdf = FPDF(format='A4')

    # Добавление страницы
    pdf.add_page()

    # Установка шрифта
    pdf.add_font('Roboto', '', 'Roboto-Regular.ttf')
    pdf.add_font('Roboto', 'B', 'Roboto-Bold.ttf')
    pdf.set_font('Roboto', '', 10)
    # Установка серого цвета текста (128, 128, 128) - это оттенок серого
    pdf.set_text_color(128, 128, 128)

    # Текст для добавления
    text = """ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ 
    "СМАРТВЕНДАНАЛИТИКА"
    115093, Москва г, Большая Серпуховская ул, дом 44, квартира ПОМ1 ОФ401"""

    # Установка позиции для текста в правом верхнем углу
    # X и Y координаты могут быть подобраны экспериментально для оптимального расположения
    pdf.set_xy(100, 10)

    # Добавление текста
    pdf.multi_cell(0, 5, text, align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Возвращение к черному цвету текста
    pdf.set_text_color(0, 0, 0)

    pdf.cell(5, 10, "", 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(10)

    customer_x = pdf.x
    pdf.cell(10, 10, "Образец для заполнения платежного поручения", 0, align='L', new_x=XPos.LMARGIN, new_y=YPos.NEXT)


    pdf.cell(0, 0, "", 0, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(14)
    top = pdf.y + 6
    pdf.x=customer_x+1 ###
    offset = pdf.x
    table_x = pdf.x
    pdf.cell(60, 6, "ИНН 9705141529", 1)
    pdf.cell(40, 6, "КПП 770501001", 1)
    pdf.cell(70, 18, "Сч. № 40702810138000017632", 1)
    #pdf.ln(0)  # Move to the next line
    pdf.cell(14)
    text_1 = '''Получатель 
ОБЩЕСТВО С ОГРАНИЧЕННОЙ 
ОТВЕТСТВЕННОСТЬЮ "СМАРТВЕНДАНАЛИТИКА"'''
    pdf.y = top
    pdf.x = offset 
    pdf.multi_cell(100, 4, text_1, 1, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(14)
    pdf.x = offset ####
    text_2="""Банк получателя
    ПАО Сбербанк, г. Москва"""
    pdf.cell(100, 16, text_2, 1)
    top = pdf.y + 8
    offset = pdf.x
    pdf.cell(70, 8, "БИК 044525225", 1)
    pdf.y = top
    pdf.x = offset 
    pdf.cell(70, 8, "Сч. № 30101810400000000225", 1)
    pdf.cell(20, 18, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.set_font('Roboto', 'B', 14)
    #text_invoce_date = f"Счёт на оплату № {number} от {date} г."
    pdf.cell(190, 6, f"Счёт на оплату № ЛК-{INVOICE_NO} от 14 ноября 2023 г.", 0, align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(5, 5, new_x=XPos.LMARGIN, new_y=YPos.NEXT) # Move to the next line
    #text_customer = f'{client_name}'
    pdf.set_font('Roboto', '', 10)
    pdf.x = customer_x
    pdf.cell(40, 10, f"Плательщик: {BUYER}, ИНН: {inn}", 0, align='L', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.x = table_x
    pdf.set_font('Roboto', 'B', 8)
    pdf.cell(7, 10, "№", 1, align='C')
    pdf.cell(74, 10, "Наименование товара, работ, услуг", 1, align='C')
    kostyl1 = pdf.y
    pdf.multi_cell(10, 5, "Ед.\n изм.", 1, align='C')
    pdf.y= kostyl1
    pdf.cell(12, 10, "Кол-во", 1, align='C')
    pdf.multi_cell(24, 5, "Цена без НДС,\n руб.", 1, align='C')
    pdf.y= kostyl1
    pdf.multi_cell(17, 5, "Скидка, \n руб.", 1, align='C')
    x_for_total = pdf.x # added 14.11
    pdf.y= kostyl1
    pdf.multi_cell(26, 5, "Сумма без НДС,\n руб.", 1, align='C')
    pdf.ln(0)
    pdf.x = table_x
    pdf.set_font('Roboto', '', 8)
    pdf.y = kostyl1 + 10
    pdf.cell(7, 10, "1", 1, align='C')
    pdf.cell(74, 10, "Оплата права использования программы Смартвенд", 1, align='L')
    pdf.cell(10, 10, "шт", 1, align='C')
    pdf.cell(12, 10, f"{count}", 1, align='C')
    # total_x = pdf.x
    pdf.cell(24, 10, f"{tariff}", 1, align='C')
    total_x = pdf.x
    pdf.cell(17, 10, f"{discount},00", 1, align='R')
    amount_x = pdf.x + 29
    pdf.cell(26, 10, f"{TOTAL},00", 1, align='R')
    pdf.cell(10 ,5, "", new_x=XPos.RIGHT, new_y=YPos.NEXT )
    pdf.x = total_x - 10
    #pdf.ln(0)
    text_total = """
Итого без НДС
Итого НДС
Всего к оплате"""
    total_y=pdf.y
    pdf.multi_cell(28, 7, text_total, 0, align='R')
    pdf.x = amount_x - 12
    pdf.y = total_y
    text_amounts = f"""
{total},00
0,00
{total},00"""
    pdf.x = x_for_total # added 14.11
    pdf.multi_cell(26, 7, text_amounts, 0, align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(14)
    pdf.x = customer_x
    text_addit = f"""
Всего наименований 1, на сумму {TOTAL} руб. в т.ч. НДС (0%) 0,00 руб.
{PROPIS_TOTAL.capitalize()} рублей 00 копеек
    """
    pdf.multi_cell(150, 5, text_addit, 0, align='L',new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(5)
    pdf.set_font('Roboto', 'B', 8)
    pdf.x = customer_x
    pdf.multi_cell(100, 5, "Дополнительная информация", 0, align='L',new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(7,10)
    pdf.set_font('Roboto', '', 8)
    pdf.x = customer_x
    text_assign = f"""В назначении платежа, пожалуйста, укажите «Оплата по счету ЛК-{INVOICE_NO} от 14.11.2023 за право использования программы Смартвенд»"""
    pdf.multi_cell(180, 5, text_assign, 0, align='L',new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.x = customer_x
    pdf.cell(170,5, border='B', align='C')
    pdf.ln(0)
    pdf.ln(0)
    pdf.ln(0)
    pdf.ln(0)
    pdf.ln(0)
    pdf.ln(0)
    pdf.ln(0)
    pdf.ln(0)
    pdf.ln(0)
    pdf.ln(0)
    pdf.cell(30,30)
    lasty = pdf.y
    lastx = pdf.x
    pdf.cell(160, 5, "Генеральный директор                                                                    _________________                         _________________")
    pdf.y = lasty
    pdf.x = lastx + 118
    pdf.cell(50,5,'/ Никитин А.Г. /')
    pdf.image("seal.png",lastx+33,lasty-13, 47,44)
    pdf.image("sign.png",lastx+79,lasty-17, 20,20)


    # # Sanitize the legal name to make it a valid filename
    # filename = "".join(c for c in legal_name if c.isalnum() or c in (' ', '_')).rstrip()
    # pdf_output = f'invoices\{filename}_invoice.pdf'
    # # Ensure the invoices directory exists
    # os.makedirs(os.path.dirname(pdf_output), exist_ok=True)
    # # Сохранение PDF файла
    # pdf_output = f'\invoices\{filename}_invoice.pdf'
    # pdf.output(pdf_output)
        # Sanitize the legal name to make it a valid filename
    filename = "".join(c for c in legal_name if c.isalnum() or c in (' ', '_')).rstrip()
    
    # Use an absolute path (adjust the path according to your system)
    invoice_dir = 'E:\\A_LaundryM\\смартвенд\\скрипт счета\\invoices'
    pdf_output = os.path.join(invoice_dir, f'Счет № {INVOICE_NO} от 14.11.2023 для {email} .pdf')

    # Print the path for debugging
    print(f'Saving invoice to: {pdf_output}')

    # Ensure the invoices directory exists
    os.makedirs(os.path.dirname(pdf_output), exist_ok=True)

    # Save the PDF file
    pdf.output(pdf_output)

#webbrowser.open_new('blank_a4_pdf.pdf')