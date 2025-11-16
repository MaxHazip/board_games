from django.db import models


# Create your models here.
class BoardGames(models.Model):
    name = models.CharField('Название игры', max_length=35, unique=True)
    price = models.DecimalField('Цена', max_digits=20, decimal_places=2)
    description = models.TextField('Описание игры')
    players_number = models.CharField('Количество игроков', max_length=6)
    game_time = models.CharField('Среднее время игры', max_length=30)
    min_age = models.IntegerField('Минимальный возраст')
    games_genres = models.ManyToManyField('Genres')
    game_image = models.ImageField('Картинка игры', upload_to='media/')
    add_date = models.DateField("Дата добавления", default='2025-01-01')
    popularity = models.IntegerField('Популярность', default=0)


    class Meta:
        verbose_name = 'Настольная игра'
        verbose_name_plural = 'Настольные игры'

    def __str__(self):
        return f"{self.name} {self.price}"

class Genres(models.Model):
    name = models.CharField('Название жанра', max_length=35, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return f"{self.name}"
    
class Profiles(models.Model):
    first_name = models.CharField('Имя', max_length=40)
    surname = models.CharField('Фамилия', max_length=40)
    middle_name = models.CharField('Отчество', max_length=40, null=True)
    email = models.EmailField('Электронная почта', max_length=50, null=True)
    phone_number = models.CharField('Телефон', max_length=50, null=True)
    birthday = models.DateField('Дата рождения')
    bonus_card_id = models.ForeignKey('BonusCards', verbose_name='Бонусная карта', on_delete=models.CASCADE)
    order = models.ManyToManyField('BoardGames', through='Orders', through_fields=('profile_id', 'board_game_id'))
    cart_items = models.ManyToManyField('BoardGames', through='Cart', through_fields=('profile_id', 'board_game_id'), related_name='in_cart')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f"{self.first_name} {self.surname}"
    
class BonusCards(models.Model):
    balance = models.IntegerField('Баланс')
    percentage_of_return = models.CharField('Процент возврата', max_length=3)
    amount_of_purchases = models.DecimalField('Сумма покупок', max_digits=50, decimal_places=2)

    class Meta:
        verbose_name = 'Бонусная карта'
        verbose_name_plural = 'Бонусные карты'

    def __str__(self):
        return f"{self.id}"

class Orders(models.Model):
    profile_id = models.ForeignKey('Profiles', verbose_name='Профиль', on_delete=models.CASCADE)
    board_game_id = models.ForeignKey('BoardGames', verbose_name='Настольная игра', on_delete=models.CASCADE)
    amount = models.IntegerField('Количество')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f"{self.id}"

class Cart(models.Model):
    profile_id = models.ForeignKey('Profiles', verbose_name='Профиль', on_delete=models.CASCADE)
    board_game_id = models.ForeignKey('BoardGames', verbose_name='Настольная игра', on_delete=models.CASCADE)
    amount = models.IntegerField('Количество')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f"{self.id}"

class Purchased(models.Model):
    profile_id = models.ForeignKey('Profiles', verbose_name='Профиль', on_delete=models.CASCADE)
    board_game_id = models.ForeignKey('BoardGames', verbose_name='Настольная игра', on_delete=models.CASCADE)
    amount = models.IntegerField('Количество')
    cost = models.DecimalField('Сумма', max_digits=50, decimal_places=2)
    bonus_amount = models.IntegerField('Количество бонусов')

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'

    def __str__(self):
        return f"{self.id}"