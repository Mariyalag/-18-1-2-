from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'third_task/home.html')

def cards(request):
    cards_info = {
        'past': 'Карта прошлого помогает понять, какие события и эмоции повлияли на ваше текущее состояние.',
        'present': 'Карта настоящего позволяет осознать текущие чувства и ситуации, в которых вы находитесь.',
        'future': 'Карта будущего открывает перспективы и возможности, которые могут появиться в вашей жизни.'
    }
    return render(request, 'third_task/cards.html', {'cards_info': cards_info})

def contact(request):
    return render(request, 'third_task/contact.html')

def testimonials(request):
    testimonials_list = [
        "Отличный опыт! Помогли разобраться в своих чувствах.",
        "Очень профессионально и внимательно. Рекомендую!",
        "МАК-карты открыли мне глаза на многие вещи."
    ]
    return render(request, 'third_task/testimonials.html', {'testimonials': testimonials_list})

def blog(request):
    articles = [
        {
            "title": "Как МАК-карты помогают в психологии",
            "content": (
                "МАК-карты (метафорические ассоциативные карты) — это эффективный инструмент в психологии, "
                "который помогает людям лучше понять свои чувства, переживания и внутренние конфликты. "
                "Они представляют собой набор карт с изображениями, символами или словами, которые вызывают "
                "ассоциации и эмоции. Вот несколько способов, как МАК-карты могут быть полезны в психологии:\n"

                "1. Самовыражение: МАК-карты позволяют клиентам выразить свои мысли и чувства, которые "
                "часто трудно verbalizovat. Это особенно полезно для людей, испытывающих трудности в "
                "коммуникации.\n"

                "2. Углубленное понимание: Использование карт помогает выявить скрытые аспекты личности и "
                "внутренние конфликты, что способствует более глубокому самопознанию.\n"

                "3. Процесс терапии: В сессиях с психологом карты могут служить отправной точкой для "
                "обсуждения, помогая клиентам открыться и углубиться в свои переживания.\n"

                "4. Работа с метафорами: МАК-карты активно используют метафоры, что позволяет клиентам "
                "переосмыслить свои проблемы и найти новые решения.\n"

                "5. Креативный подход: Этот инструмент делает процесс терапии более увлекательным и менее "
                "формальным, что может снизить уровень тревожности у клиентов.\n"

                "Таким образом, МАК-карты являются мощным средством для самопознания и развития, "
                "помогая людям открывать новые горизонты в понимании себя и своих эмоций."
            )
        },
        {
            "title": "5 советов по саморазвитию",
            "content": (
                "1. Постановка целей: Определите краткосрочные и долгосрочные цели. Записывайте их и "
                "регулярно отслеживайте прогресс.\n"
                
                "2. Чтение и обучение: Регулярно читайте книги, статьи и проходите курсы по интересующим вас "
                "темам для расширения кругозора и повышения квалификации.\n"
                
                "3. Рефлексия: Проводите время на самоанализ. Оценивайте свои достижения, ошибки и уроки, "
                "которые вы из них извлекли.\n"
                
                "4. Практика новых навыков: Применяйте на практике то, что изучили. Регулярная практика "
                "помогает закрепить знание и развить уверенность в себе.\n"
                
                "5. Забота о здоровье: Поддерживайте физическое и психическое здоровье через регулярные "
                "физические нагрузки, здоровое питание и достаточный сон. Здоровье — основа для успешного "
                "саморазвития."
            )
        },
    ]
    return render(request, 'third_task/blog.html', {'articles': articles})