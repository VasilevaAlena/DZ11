import requests


token = input('Введите ваш токен: ')

class VkFriends:
    url = 'https://api.vk.com/method/'

    def __init__(self, user_id, version):
        self.user_id = user_id
        self.version = version
        self.params = {
            'access_token': token,
            'v': self.version
        }

    def get_friends(self):
        friends_url = self.url + 'friends.get'
        friends_params = {
            'user_id': self.user_id,
            'fields': 'domain'
        }
        res = requests.get(friends_url, params={**self.params, **friends_params})
        list_friends = []
        info_friends = res.json()['response']['items']

        for info_friend in info_friends:
            profile_friends = ('https://vk.com/' + info_friend['domain'])
            list_friends.append(profile_friends)
        return list_friends


user1 = VkFriends('154010681', '5.126')
user2 = VkFriends('29414115', '5.126')
user1_friends = set(user1.get_friends())
user2_friends = set(user2.get_friends())
general_friends = user1_friends & user2_friends

print(f'У user1 и user2 общих друзей - {len(general_friends)}. \n Ссылки на их профиль: \n {general_friends}')
