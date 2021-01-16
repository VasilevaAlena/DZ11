import requests


token = input('Введите ваш токен: ')

class VkFriends:
    url = 'https://api.vk.com/method/'

    def __init__(self, user_id):
        self.user_id = user_id
        self.params = {
            'access_token': token,
            'v': '5.126'
        }

    def __and__(self, other_user):
        friends_url = self.url + 'friends.getMutual'
        friends_params = {
            'source_uid': self.user_id,
            'target_uid': other_user.user_id
        }
        res = requests.get(friends_url, params={**self.params, **friends_params})
        mutal_user_lust = res.json()['response']
        return mutal_user_lust

    def __str__(self):
        print('https://vk.com/id' + self.user_id)


user1 = VkFriends('154010681')
user2 = VkFriends('29414115')
print(user1 & user2)
user1.__str__()
user2.__str__()
