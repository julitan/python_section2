import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:
    def set_info(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print('--------------')
        print("Name: " + self.name)
        print("Phone: " + self.phone)
        print("-------------")


#user1 = UserInfo.set_info("jsjeong", "010-4379-7601")
#user1_print = UserInfo.print_info()

user1 = UserInfo()
user2 = UserInfo()

print(id(user1))
print(id(user2))

user1.set_info("jsjeong", "1111")
user2.set_info("jhpark", "2222")

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)

print(user1.name, user1.phone, user2.name, user2.phone)
