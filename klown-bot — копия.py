import discord
from discord.ext import commands
import random
import json
import datetime
from encoder import Message, MyEncoder

client = commands.Bot( command_prefix= '!')

data = {"messages": []}

anekdoty = [
    'Идея для стартапа: Пуховики для веганов на тополином пуху.',
    'Если теперь Справедливая Россия - за правду, за что же она была раньше?',
    '- Почему тевтонские рыцари поперлись в озеро? - Они ничего не видели, у них забрало запотело.',
    'В Сочи прошли переговоры Лукашенко и Путина. Александр Григорьевич подарил Путину белорусский пармезан и хамон, а Владимир Владимирович в ответ подарил три миллиарда долларов.',
    'Бабушка в аптеке разговаривает с провизором: - Дочка, дай мне таблеток! - Вам каких? - Да любых, у меня все закончились.',
    'Роскосмос анонсировал запуск первого в мире беспилотного самогонного аппарата.',
    'Электрические скаты в девятнадцатом веке работали на угле и пару.',
    '23 февраля - это такой праздник, когда мужикам вручают микро подарки, от которых они должны прочувствовать за собой макро долг.',
    '- Сёма, на 23 подарка не будет, ты не служил! - Ну я же поздравляю тебя с 8 марта, хоть ты и не рожала.',
    '- Решено! Это лето я проведу на колёсах! - Путешествовать будешь? - Не совсем.',
    'Засыпают муж с женой. Вдруг шкаф заговорил: – Ну что, твой спит? – Да вроде. – отвечает жена. – Ну я пойду?Тут муж просыпается: – Куда пошел, я за тебя еще кредит не отдал!',
    'ПОЛИТКОРРЕКТНЫЙ АНЕКДОТ. Некая личность приходит в некое место и говорит что-то другой личности. Вторая личность что-то отвечает, первая слушает ответ и снова что-то говорит, обращаясь ко второй. И то, что она говорит, по-настоящему смешно.',
    '— Дорогой, когда мы поженимся, у нас будет трое детей. — Откуда ты знаешь? — Так они ведь уже живут у моей мамы.',
    '-Слушай, а чего волхвы принесли новорожденному Иисусу? -Даров -Привет',
    '— Папа, папа, не надо меня шлепать! — закричал сынишка. Но папа-комиссар достал маузер и шлепнул сынишку.',
    'Звонок в квартиру из ЖЭКа: — У вас унитаз работает? Хорошо... к вам сейчас трое соседей срать придут.',
    '— Дорогая, это тебе на Новый год, открывай скорее! — Это твоя ширинка. — Открывай, говорю.',
    'старый телефон отслужил своё ушел на пенсию, и увлекся рыбалкой. сидит на берегу, сидит и как заорет: – БЛЯТЬ, СЕТЬ НЕ ЛОВИТ, СУКА',
    'Плохие лимоны после смерти попадают в лимонад.',
    'Маша любила петь... eё рекорд был 40 Петь в месяц.',
    'Коллеги, сегодня я вас всех собрал, потому что вы - пазл.',
    'А в городе Рыбинск День Святого Валентина так и называется – нерест.',
    'Работник атомной станции понял, что что-то не так, когда открыл пиво взглядом.',
    'Работница почты России идет домой неделю.',
    'Дэвид Бэкхем на даче копает огород в майке с фамилией Алдонин.',
    'Сын Елены Малышевой пришел на утренник в костюме тромба и остановил хоровод.',
    'Ин биг фэмели ду нот хрум-хрум фэйс!',
    'Новости культуры и спорта. В Боливии застрелен министр культуры и спорта.',
    'Оказывается, о моей работе ещё Чуковский писал: "И такая дребедень целый день - то тюлень позвонит, то олень".',
    'Ин дер гроссе фамилие дас клювен клац-клац нихт',
    'Злюкен собакен яйцен клац-клац)',
    'Андрей козловский упал с лестницы и перднул',
    'Все, что для хохла хорошо, то свинье - смерть.',
    'Цены на товары в России выше чем в соседней Украине в 2 раза, потому что на Украине только один главный вор.',
    '— Мыкола, шо, в первую очередь, ты взял бы с собой на необитаемый остров? — Шмат сала и рогалик. — Зачем? — Блин, ты тупой? Кушать!',
    'Хорошо хохлам: из двух извечных вопросов — "Что делать?" и "Кто виноват?" — по крайней мере на второй они уже для себя ответили.',
    'Небольшая деревушка. К ней быстро приближается отряд вооруженных до зубов свиней. У первого встречного обалдевшего мужика свиной командир деловито спрашивает: — Хохлы в деревне есть?',
    'Хохлушка проходит медосмотр. После посещения гинеколога читает у себя в карточке: Здорова. — Вот жлоб! Не мог написать, что мала?',
    'Садится хохол в поезд, заходит в вагон, нашел свое купе. Открывает дверь, а там три негра сидят! Хохол: — Ой, хлопцы! А шо тут горело?'
]




@client.event
async def on_message(message):
    split_message = message.content.split()
    if len(split_message) == 0:
        return None
    msg = Message(message.author, message.content)
    data["messages"].append(msg)
    await client.process_commands(message)
    
    

@client.event
async def on_disconnect():
    time = datetime.datetime.now()
    print('Klown disconnect at {}'.format(time))
    with open('users_data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, cls=MyEncoder, indent=4, ensure_ascii=False)


@client.command(name='малчат')

@commands.is_owner()
async def bot_shutdown(ctx):
    await ctx.bot.logout()



@client.event
async def on_ready():
    print('Клоун на месте.')

@client.command(name="ржака")
async def humor(context):
    await context.channel.send(random.choice(anekdoty))




client.run("token")
